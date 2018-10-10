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

Name:           chwala
Version:        0.5.3
Release:        1%{?dist}
Summary:        Glorified WebDAV, done right

Group:          Applications/Internet
License:        AGPLv3+
URL:            http://chwala.org
Source0:        https://mirror.kolabenterprise.com/pub/releases/%{name}-%{version}.tar.gz
Source2:        chwala.logrotate

Patch1:         chwala-0.5.3-suhosin.session.encrypt-php_flag.patch

BuildArch:      noarch

Requires:       php-pear(HTTP_Request2)
Requires:       php-Smarty >= 3.1.7

Requires(post): roundcubemail(core)

%if 0%{?plesk} < 1
Requires:       roundcubemail
Requires:       roundcubemail-plugins-kolab
%endif

%if 0%{?suse_version}
Requires:       http_daemon
%else
Requires:       webserver
%endif

%if 0%{?suse_version}
BuildRequires:  roundcubemail
BuildRequires:  roundcubemail-plugins-kolab
%endif

%description
Chwala is the implementation of a modular, scalable, driver-backed file-
and media-storage, that with using an API, provides generated UI components
based on context and content, for the purpose of integration with 3rd
party applications.

%prep
%setup -q

%patch1 -p1

%build

%install
mkdir -p \
%if 0%{?plesk} < 1
    %{buildroot}/%{_ap_sysconfdir}/conf.d \
%endif
    %{buildroot}/%{_datadir}/%{name} \
    %{buildroot}/%{_localstatedir}/cache/%{name} \
    %{buildroot}/%{_localstatedir}/lib/%{name} \
    %{buildroot}/%{_localstatedir}/log/%{name}

%if 0%{?plesk} < 1
install -pm 644 doc/chwala.conf %{buildroot}/%{_ap_sysconfdir}/conf.d/chwala.conf
%endif

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp -pr %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/chwala

sed -i \
    -e 's/apache apache/%{httpd_user} %{httpd_group}/g' \
    %{buildroot}%{_sysconfdir}/logrotate.d/chwala

rm -rf public_html/skins/default/images/mimetypes/_css.sh
cp -a lib public_html %{buildroot}/usr/share/%{name}

pushd %{buildroot}/%{_datadir}/%{name}

mkdir -p lib/drivers/kolab/plugins

pushd lib/drivers/kolab/plugins
%if 0%{?plesk} < 1
ln -s ../../../../../roundcubemail/plugins/kolab_auth kolab_auth
%endif
ln -s ../../../../../roundcubemail/plugins/kolab_folders kolab_folders
ln -s ../../../../../roundcubemail/plugins/libkolab libkolab
popd

pushd lib
ln -s ../../roundcubemail/program/lib/Roundcube Roundcube
popd

ln -s ../../..%{_localstatedir}/cache/%{name} cache
ln -s ../../..%{_sysconfdir}/roundcubemail config
ln -s ../../..%{_localstatedir}/lib/%{name} temp
ln -s ../../..%{_localstatedir}/log/%{name} logs
popd

%post
if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
    if [ ! -z "`grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null`" ]; then
%if 0%{?with_systemd}
        /bin/systemctl condrestart %{httpd_name}.service
%else
        /sbin/service %{httpd_name} condrestart
%endif
    fi
fi

/usr/share/roundcubemail/bin/updatedb.sh \
    --dir /usr/share/doc/%{name}-%{version}/SQL/ \
    --package %{name} >/dev/null 2>&1 || :

%files
%doc README.md LICENSE doc/SQL/
%if 0%{?plesk} < 1
%config(noreplace) %{_ap_sysconfdir}/conf.d/%{name}.conf
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_datadir}/%{name}
%attr(0750,%{httpd_user},%{httpd_group}) %{_localstatedir}/cache/%{name}
%attr(0750,%{httpd_user},%{httpd_group}) %{_localstatedir}/lib/%{name}
%attr(0750,%{httpd_user},%{httpd_group}) %{_localstatedir}/log/%{name}

%changelog
* Fri Aug 10 2018 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5.3-1
- Release 0.5.3

* Wed Dec 20 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5.2-1
- Release 0.5.2

* Mon Jul 24 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5.1-1
- Release 0.5.1

* Wed May 31 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5.0-1
- Release 0.5.0

* Wed May 10 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5-0.2.git
- Fix log rotation on Plesk systems

* Tue Nov 15 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5-0.1.git
- Check in 0.5 snapshot

* Mon Dec  7 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.4-0.1.git
- Check in 0.4 snapshot

* Fri Mar 27 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.1-1
- Release of version 0.3.1

* Sat Feb 14 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.0-2
- Use filder state check when accessing file folder (#4478)

* Sun Jan 11 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.0-1
- Release of version 0.3.0

* Thu Jan 23 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2-3
- Correct any suhosin.session.encrypt setting using .htaccess
- Correct source of chwala.conf

* Tue Nov 26 2013 Daniel Hoffend <dh@dotlan.net> - 0.2-1.1
- added logrotate script

* Sun Nov 24 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2-1
- New upstream version

* Tue Oct 29 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-0.5
- Require only "webserver" or "http_daemon"

* Fri Aug  9 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-0.4
- New snapshot

* Tue May  7 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-0.2
- A first version of chwala
