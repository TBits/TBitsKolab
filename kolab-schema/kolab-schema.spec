Name:       kolab-schema
Version:    3.3
Release:    1%{?dist}
Summary:    LDAP Schema Extensions for Kolab Groupware

Group:      Applications/System
License:    GPL+
URL:        http://www.kolab.org

# From http://git.kolab.org/kolab-schema/snapshot/482e4131744a9f6aed1c8611796af2d5c1d2af1f.tar.gz
Source0:    %{name}-%{version}.tar.gz

BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:  noarch

%description
LDAP Schema Extensions for Kolab Groupware

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc kolab3.schema kolab3.ldif

%changelog
* Wed Sep  9 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3-1
- New version allowing 'alias' attribute for 'kolabGroupOfUniqueNames'
  objectclass.

* Fri Nov 20 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2-1
- New version including a kolabResource objectClass

* Wed Feb 12 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1-1
- Version compatible with UCS

* Thu Jun 21 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0-0.1
- First package
