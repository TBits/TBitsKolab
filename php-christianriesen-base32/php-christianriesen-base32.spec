# Spec file for php-christianriesen-base32
#
# Copyright (c) 2013-2014 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
#%%global gh_commit    6a8aec204688d36681e0185fbaf1974b97e4a070
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     christianriesen
%global gh_project   christianriesen-base32
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{gh_project}
Summary:        Base32 Encoder/Decoder for PHP according to RFC 4648
Version:        1.2.1
Release:        1%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz
License:        MIT
Group:          Development/Libraries

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.4
%endif

Provides:       php-composer(christianriesen/base32) = %{version}-%{release}

# From composer.json
Requires:       php(language) >= 5.4

%description
Base32 Encoder/Decoder for PHP according to RFC 4648.

%prep
%setup -q -n %{gh_project}-%{?gh_commit:%{gh_commit}}%{!?gh_commit:%{version}}

%build
# nothing to build

%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Base32/
cp -pr src/* %{buildroot}%{_datadir}/php/Base32/.

%check

%files
%defattr(-,root,root,-)
%doc composer.json LICENSE README.md
%{_datadir}/php/Base32


%changelog
* Mon Jul  6 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.2.1-1
- First package
