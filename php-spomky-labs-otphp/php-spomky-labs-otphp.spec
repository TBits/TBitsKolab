# Spec file for php-spomky-labs-otphp
#
# Copyright (c) 2013-2014 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
#%%global gh_commit    6a8aec204688d36681e0185fbaf1974b97e4a070
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     spomky-labs
%global gh_project   spomky-labs-otphp
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{gh_project}
Summary:        Generate One Time Passwords
Version:        4.0.2
Release:        2.23%{?dist}.kolab_16

URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz
License:        MIT
Group:          Development/Libraries

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.4
%endif

Provides:       php-composer(spomky-labs/otphp) = %{version}

# From composer.json
Requires:       php(language) >= 5.4
Requires:       php-composer(christianriesen/base32)

%description
A php library for generating one time passwords according to RFC 4226
(HOTP Algorithm) and the RFC 6238 (TOTP Algorithm).

%prep
%setup -q -n %{gh_project}-%{?gh_commit:%{gh_commit}}%{!?gh_commit:%{version}}

%build
# nothing to build

%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/OTPHP/
cp -pr lib/* %{buildroot}%{_datadir}/php/OTPHP/.

%check

%files
%defattr(-,root,root,-)
%doc composer.json LICENCE README.md
%{_datadir}/php/OTPHP


%changelog
* Mon Jul  6 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 4.0.2-1
- First package
