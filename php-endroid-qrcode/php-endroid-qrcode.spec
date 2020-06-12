# Spec file for php-endroid-qrcode
#
# Copyright (c) 2013-2014 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
#%%global gh_commit    6a8aec204688d36681e0185fbaf1974b97e4a070
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     endroid
%global gh_project   endroid-qrcode
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{gh_project}
Summary:        Endroid QR Code Generator
Version:        1.5.4
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

# From composer.json
Requires:       php(language) >= 5.4
Requires:       php-gd

%description
This library based on QRcode Perl CGI & PHP scripts by Y.
Swetake helps you generate images containing a QR code.

%prep
%setup -q -n %{gh_project}-%{?gh_commit:%{gh_commit}}%{!?gh_commit:%{version}}

%build
# nothing to build

%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Endroid/QrCode/
cp -pr assets %{buildroot}%{_datadir}/php/Endroid/.
cp -pr src/* %{buildroot}%{_datadir}/php/Endroid/QrCode/.

%check

%files
%defattr(-,root,root,-)
%doc composer.json LICENSE README.md
%dir %{_datadir}/php/Endroid
%{_datadir}/php/Endroid/assets
%{_datadir}/php/Endroid/QrCode


%changelog
* Mon Jul  6 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.5.4-1
- First package
