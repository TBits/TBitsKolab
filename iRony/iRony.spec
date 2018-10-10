# Needed for opensuse build system
%if 0%{?opensuse_bs}
#!BuildIgnore:  boa
#!BuildIgnore:  cherokee
#!BuildIgnore:  nginx
#!BuildIgnore:  httpd-itk
#!BuildIgnore:  lighttpd
#!BuildIgnore:  thttpd

#!BuildIgnore:  php-mysqlnd
%endif

%{!?php_inidir: %global php_inidir %{_sysconfdir}/php.d}

%if 0%{?suse_version} < 1 && 0%{?fedora} < 1 && 0%{?rhel} < 7
%global with_systemd 0
%else
%global with_systemd 1
%endif

%if 0%{?suse_version}
%global httpd_group www
%global httpd_name apache2
%global httpd_user wwwrun
%else
%if 0%{?plesk}
%global httpd_group roundcube_sysgroup
%global httpd_name httpd
%global httpd_user roundcube_sysuser
%else
%global httpd_group apache
%global httpd_name httpd
%global httpd_user apache
%endif
%endif

%global _ap_sysconfdir %{_sysconfdir}/%{httpd_name}

Name:           iRony
Version:        0.4.0
Release:	    0.20170502.git%{?dist}
Summary:        DAV for Kolab Groupware

Group:          Applications/Internet
License:        AGPLv3+
URL:            http://kolab.org

# From 7ebe1adc8b7c0f818d837d682b2b85202aac9303
Source0:        iRony-%{version}.tar.gz
Source1:        iRony.conf
Source2:        iRony.logrotate

BuildArch:      noarch

Requires:       chwala
Requires:       php-sabre-dav >= 2.1.3
Requires:       php-sabre-vobject >= 3.2.4
Requires:       roundcubemail(core) >= 1.1
%if 0%{?plesk} < 1
Requires:       roundcubemail-plugin-kolab_auth >= 3.3
%endif
Requires:       roundcubemail-plugin-kolab_folders >= 3.3
Requires:       roundcubemail-plugin-libcalendaring >= 3.3
Requires:       roundcubemail-plugin-libkolab >= 3.3
%if 0%{?suse_version}
Requires:       http_daemon
%else
Requires:       webserver
%endif

# Build requirements needed of *SUSE, which otherwise bails over
# dead-end symbolic links and/or files and directories not owned
# by any package.
BuildRequires:  chwala
BuildRequires:  composer
BuildRequires:  roundcubemail
BuildRequires:  roundcubemail-plugins-kolab
BuildRequires:  php-sabre-dav >= 2.1.3
BuildRequires:  php-sabre-vobject >= 3.2.4

%if 0%{?fedora} >= 21
# Fedora 21 has qca2 and qca, qca2 has been renamed to qca, required by kdelibs
BuildRequires: qca
%endif

%description
iRony is the CardDAV, CalDAV and WebDAV storage access provider for the
Kolab Groupware solution.

%prep
%setup -q

%build
rm -rf composer.json
mv composer.json-dist composer.json
mkdir -p $HOME/.composer/
echo '{}' > $HOME/.composer/composer.json
%if 0%{?fedora} >= 25
# workaround for misbehaving Kolab modules for PHP7, probably a swig issue
export USE_ZEND_ALLOC=0
%endif
composer -vvv dumpautoload --optimize

%install
mkdir -p \
%if 0%{?plesk} < 1
    %{buildroot}/%{_ap_sysconfdir}/conf.d \
%endif
    %{buildroot}/%{_sysconfdir}/%{name} \
    %{buildroot}/%{_datadir}/%{name} \
    %{buildroot}/%{_localstatedir}/cache/%{name} \
    %{buildroot}/%{_localstatedir}/lib/%{name} \
    %{buildroot}/%{_localstatedir}/log/%{name}

%if 0%{?plesk} < 1
install -pm 644 %{SOURCE1} %{buildroot}/%{_ap_sysconfdir}/conf.d/%{name}.conf
%endif

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp -pr %SOURCE2 %{buildroot}%{_sysconfdir}/logrotate.d/iRony

sed -i \
    -e 's/apache apache/%{httpd_user} %{httpd_group}/g' \
    %{buildroot}%{_sysconfdir}/logrotate.d/iRony

mkdir %{buildroot}/usr/share/%{name}/lib

cp -a public_html vendor %{buildroot}/usr/share/%{name}
cp -a lib/Kolab %{buildroot}/usr/share/%{name}/lib/

pushd %{buildroot}/%{_datadir}/%{name}

ln -s ../../..%{_localstatedir}/cache/%{name} temp
ln -s ../../..%{_localstatedir}/log/%{name} logs

mkdir config
pushd config
ln -s ../../../..%{_sysconfdir}/%{name}/dav.inc.php
ln -s ../../../..%{_sysconfdir}/roundcubemail/defaults.inc.php
ln -s ../../../..%{_sysconfdir}/roundcubemail/config.inc.php
popd

rm -rf lib/Roundcube
pushd lib/
ln -s ../../chwala/lib FileAPI
ln -s ../../roundcubemail/program/lib/Roundcube Roundcube
ln -s ../../roundcubemail/plugins plugins
popd

popd

install -pm 640 config/dav.inc.php.sample %{buildroot}/%{_sysconfdir}/%{name}/dav.inc.php

%post
if [ -f "/etc/php.d/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
    if [ ! -z "`grep ^apc.enabled=1 /etc/php.d/apc{,u}.ini`" ]; then
        /sbin/service httpd condrestart
    fi
fi

%files
%doc README.md
%if 0%{?plesk} < 1
%{_ap_sysconfdir}/conf.d/%{name}.conf
%endif
%attr(0750,root,%{httpd_group}) %dir %{_sysconfdir}/%{name}
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/dav.inc.php
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_datadir}/%{name}
%attr(0770,%{httpd_user},%{httpd_group}) %{_localstatedir}/cache/%{name}
%attr(0770,%{httpd_user},%{httpd_group}) %{_localstatedir}/lib/%{name}
%attr(0770,%{httpd_user},%{httpd_group}) %{_localstatedir}/log/%{name}

%changelog
* Wed May 10 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.4.0-2
- Fix log rotation on Plesk

* Tue May  2 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.4.0-1
- Release of version 0.4.0

* Thu Jan  8 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.0-1
- Release of version 0.3.0

* Thu Jan  8 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.9-1
- Release of version 0.2.9
- Fixes bugs #2442, #2787, #2788, #2973, #3049, #3059, #3496,
  #3537, #3598, #3739, #3776, #3837, #4128, #4129

* Thu Apr  3 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.8-1
- New snapshot

* Tue Feb 11 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.7-1
- Fix memory usage on very large result sets (#2827)

* Thu Jan  9 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.6-1
- New upstream release

* Sat Nov 30 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.5-1
- New upstream release

* Tue Nov 26 2013 Daniel Hoffend <dh@dotlan.net> - 0.2.4-3
- Added logrotate script

* Mon Nov 11 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.4-2
- Expect a list of spouses (#2473)

* Fri Nov  1 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.4-1
- New upstream version

* Tue Oct 29 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.3-3
- Require "http_daemon" (*SUSE) or "webserver"

* Wed Oct 16 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.3-2
- Ship fix for #2335

* Tue Oct  8 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.3-1
- New upstream version

* Thu Sep 19 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.1-1
- New upstream release 0.2.1, resolves;

    2238 Custom field data gets lost when updating an object in Roundcube
    2239 Error when saving a task with alarms

* Wed Sep 11 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2.0-1
- Upstream release 0.2.0

* Wed Sep  4 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-0.10
- Ship fix for #2109

* Fri Jul 12 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-0.8
- Remove duplicate vendorized libs
- Correct permissions on temp/ and logs/ directory, and create the links
- A second version of iRony

* Tue May  7 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-0.3
- A first version of iRony
