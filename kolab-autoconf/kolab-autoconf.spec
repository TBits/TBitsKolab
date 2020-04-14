# Needed for opensuse build system
%if 0%{?opensuse_bs}
#!BuildIgnore:  boa
#!BuildIgnore:  cherokee
#!BuildIgnore:  nginx
#!BuildIgnore:  httpd-itk
#!BuildIgnore:  lighttpd
#!BuildIgnore:  thttpd

#!BuildIgnore:  fedora-logos-httpd
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

Name:       kolab-autoconf
Version:    1.3.2
Release:        108.tbits%(date +%%Y%%m%%d)%{?dist}
Summary:    Autodiscovery for clients of Kolab Groupware

Group:      Applications/Internet
License:    GPLv3+
URL:        https://kolab.org

Source0:    http://mirror.kolabsys.com/pub/releases/%{name}-%{version}.tar.gz

%if 0%{?plesk} < 1
Requires:   php-kolab-net-ldap3
%endif

Obsoletes:  kolab-autodiscover < %{version}-%{release}
Provides:   kolab-autodiscover = %{version}-%{release}
BuildArch:  noarch

%description


%prep
%setup -q

%build

%install
%{__mkdir_p} \
    %{buildroot}/%{_ap_sysconfdir}/conf.d/ \
    %{buildroot}/%{_datadir}/%{name}/ \
    %{buildroot}/%{_var}/log/%{name}

%{__cp} -a lib public_html %{buildroot}/%{_datadir}/%{name}/

pushd %{buildroot}/%{_datadir}/%{name}/
ln -s ../../..%{_var}/log/%{name} logs
popd

%if 0%{?plesk} < 1
%{__install} -pm 644 docs/%{name}.conf %{buildroot}/%{_ap_sysconfdir}/conf.d/%{name}.conf
%endif

%files
%defattr(-,root,root,-)
%doc docs/*
%if 0%{?plesk} < 1
%dir %{_ap_sysconfdir}
%dir %{_ap_sysconfdir}/conf.d
%config(noreplace) %{_ap_sysconfdir}/conf.d/%{name}.conf
%endif
%{_datadir}/%{name}
%attr(0750,%{httpd_user},%{httpd_group}) %{_var}/log/%{name}

%changelog
* Mon Mar  2 2020 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.3.2-1
- Release of version 1.3.2

* Wed Apr 10 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.3.1-2
- Fix init_ldap()

* Mon Mar 18 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.3.1-1
- Release 1.3.1

* Wed Jun 27 2018 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.3.0-1
- Release version 1.3.0

* Mon Oct  9 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.3-1
- Release version 1.3

* Tue Sep 26 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2-1
- Release of version 0.2

* Tue Sep  9 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-1
- Initial version
