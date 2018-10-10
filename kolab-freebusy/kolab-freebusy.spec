#!BuildIgnore: lighttpd
#!BuildIgnore: nginx
#!BuildIgnore: php-mysql
#!BuildIgnore: thttpd
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
%global httpd_group apache
%global httpd_name httpd
%global httpd_user apache
%endif

%global _ap_sysconfdir %{_sysconfdir}/%{httpd_name}

Name:           kolab-freebusy
Version:        1.1.0
Release:        2%{?dist}
Summary:        Kolab Free/Busy Web Presentation Layer

Group:          Applications/Internet
License:        AGPLv3+
URL:            http://kolab.org/about/kolab-freebusy
Source0:        http://mirror.kolabsys.com/pub/releases/%{name}-%{version}.tar.gz
Source1:        kolab-freebusy.logrotate

BuildArch:      noarch

BuildRequires:  composer
%if 0%{?fedora}
# fix issue:
# have choice for php-composer(justinrainbow/json-schema) >= 2.0 needed by composer: php-justinrainbow-json-schema4 php-justinrainbow-json-schema
# have choice for php-composer(justinrainbow/json-schema) < 5 needed by composer: php-justinrainbow-json-schema4 php-justinrainbow-json-schema php-JsonSchema
BuildRequires:  php-justinrainbow-json-schema4
%endif

BuildRequires:  php-Monolog
BuildRequires:  php-sabre-dav >= 2.1.3
BuildRequires:  roundcubemail(core)
BuildRequires:  roundcubemail-plugins-kolab

%if 0%{?suse_version}
Requires:       http_daemon
Requires:       php
%else
Requires:       webserver
Requires:       php-common >= 5.3
%endif

Requires:       kolab-utils
Requires:       logrotate
Requires:       php-ldap
Requires:       php-Monolog
Requires:       php-pear(Net_LDAP3)
Requires:       php-sabre-dav >= 2.1.3
Requires:       roundcubemail(core)
Requires:       roundcubemail-plugins-kolab

%if 0%{?fedora} >= 21
# Fedora 21 has qca2 and qca, qca2 has been renamed to qca, required by kdelibs
BuildRequires: qca
%endif

%description
This software enables a multi-sourced publication of Free/Busy information
for its users.

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
    %{buildroot}/%{_ap_sysconfdir}/conf.d/ \
    %{buildroot}/%{_sysconfdir}/%{name}/ \
    %{buildroot}/%{_datadir}/%{name}/config \
    %{buildroot}/%{_localstatedir}/cache/%{name}/ \
    %{buildroot}/%{_localstatedir}/log/%{name}/

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp -pr %SOURCE1 %{buildroot}%{_sysconfdir}/logrotate.d/kolab-freebusy

sed -i -e 's/apache apache/%{httpd_user} %{httpd_group}/g' \
    %{buildroot}%{_sysconfdir}/logrotate.d/kolab-freebusy

install -pm 644 doc/kolab-freebusy.conf %{buildroot}/%{_ap_sysconfdir}/conf.d/%{name}.conf

cp -a lib %{buildroot}/%{_datadir}/%{name}/lib

rm -rf %{buildroot}/%{_datadir}/%{name}/lib/plugins
rm -rf %{buildroot}/%{_datadir}/%{name}/lib/Roundcube
pushd %{buildroot}/%{_datadir}/%{name}/lib/
ln -s ../../roundcubemail/plugins/ plugins
ln -s ../../roundcubemail/program/lib/Roundcube/ Roundcube
popd

cp -a public_html %{buildroot}/%{_datadir}/%{name}/public_html
cp -a vendor %{buildroot}/%{_datadir}/%{name}/vendor

cp -a config/config.ini.sample %{buildroot}/%{_sysconfdir}/%{name}/config.ini

pushd %{buildroot}/%{_datadir}/%{name}/config
ln -s ../../../..%{_sysconfdir}/%{name}/config.ini config.ini
ln -s ../../../..%{_sysconfdir}/roundcubemail/config.inc.php config.inc.php
ln -s ../../../..%{_sysconfdir}/roundcubemail/defaults.inc.php defaults.inc.php
popd

pushd %{buildroot}/%{_datadir}/%{name}/
ln -s ../../..%{_localstatedir}/log/%{name} logs
popd

find %{buildroot}/%{_datadir}/%{name} -type f -name ".*" -delete

%pre
# This is replaced by an actual directory
if [ -L "%{_datadir}/kolab-freebusy/config" ]; then
    rm -rf "%{_datadir}/kolab-freebusy/config"
fi

%post
if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
    if [ ! -z "`grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini`" ]; then
%if 0%{?with_systemd}
        /bin/systemctl condrestart %{httpd_name}.service
%else
        /sbin/service %{httpd_name} condrestart
%endif
    fi
fi

%files
%defattr(-,root,root,-)
%doc README.md
%if 0%{?suse_version}
%dir %{_ap_sysconfdir}
%dir %{_ap_sysconfdir}/conf.d
%endif
%config(noreplace) %{_ap_sysconfdir}/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0750,root,%{httpd_group}) %dir %{_sysconfdir}/%{name}/
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/config.ini
%{_datadir}/%{name}/
%attr(0770,root,%{httpd_group}) %{_localstatedir}/cache/%{name}
%attr(0770,root,%{httpd_group}) %{_localstatedir}/log/%{name}

%changelog
* Wed Feb  7 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.1.0-2
- Repack of tagged version

* Thu Jun 15 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1.0-1
- Release 1.1.0

* Thu May 25 2017 Timotheus Pokorra <tp@tbits.net> - 1.1-0.1
- Fix build error on Fedora 25, composer needs php-justinrainbow-json-schema4

* Mon Feb 23 2015 Daniel Hoffend <dh@dotlan.net> - 1.0.7-3
- seperate httpd.conf from .spec file

* Sun Feb 22 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.7-2
- Correctly render Free/Busy for recurring events with exceptions (#4665)

* Sun Feb 15 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.7-1
- Release of version 1.0.7

* Fri Jan 23 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.6-1
- Release 1.0.6

* Wed Aug 20 2014 Daniel Hoffend <dh@dotlan.net> - 1.0.5-2
- added fix for loading Net_LDAP3

* Thu Aug 14 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.5-1
- Release version 1.0.5

* Wed May 21 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.4-1
- New upstream version, enabling real-time Free/Busy directly
  from IMAP data.

* Tue Nov 26 2013 Daniel Hoffend <dh@dotlan.net> - 1.0.2-5
- Added logrotate script

* Fri Nov 15 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.2-4
- Depend on kolab-utils

* Tue Oct 29 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.2-3
- Do not require PHP itself

* Tue Apr 30 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.2-2
- Ship fix for lower-casing attributes (#1777)

* Thu Feb 21 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.2-1
- Repack of original sources

* Mon Feb 18 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-1
- First package
