
%{!?__pear:         %{expand: %%global __pear %{_bindir}/pear}}

# Needed for openSUSE
%if 0%{?suse_version}
%global php php5
%{!?pear_cfgdir:    %global pear_cfgdir %(%{__pear} config-get cfg_dir  2> /dev/null || echo undefined)}
%{!?pear_datadir:   %global pear_datadir %(%{__pear} config-get data_dir 2> /dev/null || echo undefined)}
%{!?pear_docdir:    %global pear_docdir %(%{__pear} config-get doc_dir  2> /dev/null || echo undefined)}
%{!?pear_metadir:   %global pear_metadir %(%{__pear} config-get metadata_dir 2> /dev/null || echo undefined)}
%{!?pear_phpdir:    %global pear_phpdir %(%{__pear} config-get php_dir  2> /dev/null || echo undefined)}
%{!?pear_testdir:   %global pear_testdir %(%{__pear} config-get test_dir 2> /dev/null || echo undefined)}
%{!?pear_wwwdir:    %global pear_wwwdir %(%{__pear} config-get www_dir  2> /dev/null || echo undefined)}
%{!?pear_xmldir:    %global pear_xmldir %{_localstatedir}/lib/pear/pkgxml}
%else
%global php php
%endif

%global pear_name Net_LDAP3

# Not yet an actual PEAR package ...
%if 0%{?suse_version}
Name:               php5-Net_LDAP3
%else
Name:               php-kolab-net-ldap3
%endif
Version:            1.1.3
Release:            2.1%{?dist}.kolab_16
Summary:            Object oriented interface for searching and manipulating LDAP-entries
Group:              Development/Libraries
License:            GPLv3+
URL:                https://kolab.org

Source0:            pear-Net-LDAP3-%{version}.tar.gz

BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:          noarch

Requires:           mozldap-tools >= 6.0.5
Requires:           php-ldap
Requires:           php-pear(Net_LDAP2)
Obsoletes:          php-pear(%{pear_name}) < %{version}-%{release}
Provides:           php-pear(%{pear_name}) = %{version}-%{release}
Obsoletes:          php-Net-LDAP3 < %{version}-%{release}

%description
Net_LDAP3 is an LDAPv3 compatible enhancement to Net_LDAP2

%prep
%setup -q -n pear-Net-LDAP3-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_datadir}/%{php}
cp -a lib/Net %{buildroot}/%{_datadir}/%{php}/.

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%if 0%{?suse_version}
%dir %{_datadir}/%{php}
%endif
%dir %{_datadir}/%{php}/Net
%{_datadir}/%{php}/Net/LDAP3.php
%dir %{_datadir}/%{php}/Net/LDAP3
%{_datadir}/%{php}/Net/LDAP3/Result.php

%changelog
* Mon Oct 21 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.1.3-1
- Release of version 1.1.3

* Sat Oct 19 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.1.2-1
- Release of version 1.1.2

* Fri Aug 23 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.1.1-1
- Release of version 1.1.1

* Wed Jun  5 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.1.0-1
- Release of version 1.1.0

* Wed Jun 20 2018 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.7-1
- Release of version 1.0.7

* Thu May 03 2018 Christoph Erhardt <kolab@sicherha.de> - 1.0.6-2
- Fix upgrade path

* Wed May 02 2018 Christoph Erhardt <kolab@sicherha.de> - 1.0.6-1
- New upstream release 1.0.6
- Add upstream patches

* Thu Oct 22 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.4-2
- Ensure multi-valued attributes have sequential indexes

* Thu Oct 15 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.4-1
- New upstream release 1.0.4

* Fri Mar 27 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.3-1
- New upstream release 1.0.3

* Fri Jan 23 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.2-1
- New upstream release 1.0.2

* Sun Dec 07 2014 Christoph Wickert <cwickert@fedoraproject.org> - 1.0.1-3
- Use the right properties for /mozldap/ldapsearch calls
- Add possibility to return user attributes from login() (#3858)
- Fix handling of special characters in RDN attributes (#3905)

* Wed Oct  1 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.1-2
- Correct variable naming in parse_aclrights()

* Wed Sep 10 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.1-1
- New upstream release w/ Oracle DSEE aclRights support for
  effectiveRights.

* Fri Aug 29 2014 Daniel Hoffend <dh@dotlan.net> - 1.0.0-2
- Fix PHP Fatal Error Call
- Don't log ldap passwords

* Thu Aug 14 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.0-1
- Package for Fedora/EPEL

