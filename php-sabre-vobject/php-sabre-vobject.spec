# Spec file for php-sabre-vobject
#
# Copyright (c) 2013-2014 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/3.0/
#
# Please, preserve the changelog entries
#
#%%global gh_commit    a064447d7e76dc564ffcf3a830057c2f0c17bfbd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     fruux
%global gh_project   sabre-vobject
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{gh_project}
Summary:        Library to parse and manipulate iCalendar and vCard objects
Version:        3.5.3
Release:        8.28%{?dist}.kolab_16

URL:            http://sabre.io/vobject/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz
License:        BSD
Group:          Development/Libraries

# replace composer autloader by PSR-O trivial one
Patch0:         %{gh_project}-bin.patch
Patch1:         T41247.patch
Patch2:         vobject_encoding_performance.patch

BuildArch:      noarch
%if %{with_tests}
BuildRequires:  php(language) >= 5.3.1
BuildRequires:  php-phpunit-PHPUnit
%endif

# From composer.json
#        "php"          : ">=5.3.1",
#        "ext-mbstring" : "*"
Requires:       php(language) >= 5.3.1
Requires:       php-mbstring
# From phpcompatinfo report for version 3.2.0
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xml

Provides:       php-composer(sabre/vobject) = %{version}


%description
The VObject library allows you to easily parse and manipulate iCalendar
and vCard objects using PHP. The goal of the VObject library is to create
a very complete library, with an easy to use API.

This project is a spin-off from SabreDAV, where it has been used for several
years. The VObject library has 100% unittest coverage.


%prep
%setup -q -n %{gh_project}-%{?gh_commit:%{gh_commit}}%{!?gh_commit:%{version}}

%patch0 -p0 -b .psr0
%patch1 -p1 -b .T41247
%patch2 -p1 -b .vobject_encoding_performance

: Create trivial PSR0 autoloader for tests
cat <<EOF | tee psr0.php
<?php
spl_autoload_register(function (\$class) {
    \$file = str_replace('\\\\', '/', \$class).'.php';
    @include \$file;
});
define('SABRE_TEMPDIR', __DIR__ . '/temp/');
mkdir(SABRE_TEMPDIR);
EOF


%build
# nothing to build


%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/Sabre/
cp -pr lib %{buildroot}%{_datadir}/php/Sabre/VObject

# Install the command
install -Dpm 0755 bin/vobject \
         %{buildroot}/%{_bindir}/vobject


%check
%if %{with_tests}
: Run upstream test suite against installed library
cd tests
phpunit \
  --bootstrap=../psr0.php \
  --include-path=%{buildroot}%{_datadir}/php \
  -d date.timezone=UTC || :
%else
: Skip upstream test suite
%endif


%files
%doc ChangeLog.md composer.json LICENSE README.md
%{_datadir}/php/Sabre
%{_bindir}/vobject


%changelog
* Tue Sep 18 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 3.5.3-3
- Improve encoding performance

* Wed Nov 15 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 3.5.3-2
- Avoid unintentional RRULE changes upon SNOOZE (T41247)

* Sun Dec  4 2016 Daniel Hoffend <dh@dotlan.net> - 3.5.3-1
- update to 3.5.3

* Wed Aug  5 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.4.5-1
- update to 3.4.5

* Wed Jul 16 2014 Remi Collet <remi@fedoraproject.org> - 3.2.4-1
- update to 3.2.4

* Wed Jun 18 2014 Remi Collet <remi@fedoraproject.org> - 3.2.3-1
- update to 3.2.3
- add provides php-composer(sabre/vobject)
- url is now http://sabre.io/vobject/

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  9 2014 Remi Collet <remi@fedoraproject.org> - 3.2.2-1
- update to 3.2.2

* Tue May  6 2014 Remi Collet <remi@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Sun Apr  6 2014 Remi Collet <remi@fedoraproject.org> - 3.2.0-1
- update to 3.2.0

* Thu Feb 20 2014 Remi Collet <remi@fedoraproject.org> - 3.1.3-1
- update to 3.1.3

* Tue Dec 31 2013 Remi Collet <remi@fedoraproject.org> - 2.1.3-1
- Initial packaging
