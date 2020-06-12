%if 0%{?fedora} < 13 && 0%{?rhel} < 6
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%endif

Name:           python-icalendar
Version:        3.8.2
Release:        1.32%{?dist}.kolab_16
Summary:        Parser/generator of iCalendar files following the RFC 2445

Group:          Development/Libraries
# test.py is GPLv2
# parser is GPL
# doctest.py is Public Domain
# rest is LGPLv2
License:        LGPLv2 and GPLv2 and GPLv2+ and Public Domain
URL:            http://codespeak.net/icalendar/
# source releases are done on pypi (homepage states 1.2 as latest version)
Source0:        http://pypi.python.org/packages/source/i/icalendar/icalendar-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:	python-devel
Requires:       python-pytz
%else
BuildRequires:  python2-devel
Requires:       pytz
%endif
BuildRequires:	python-setuptools
Requires:       python-dateutil

%description
iCalendar specification (RFC 2445) defines calendaring format used
by many applications (Zimbra, Thunderbird and others). This
module is a parser/generator of iCalendar files for use with
Python. It follows the RFC 2445 (iCalendar) specification.
The aim is to make a package that is fully compliant with RFC 2445,
well designed, simple to use and well documented.

%prep
%setup -q -n icalendar-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --prefix=%{_prefix} --root $RPM_BUILD_ROOT

%check

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/icalendar
%{python_sitelib}/*.egg-info

%changelog
* Thu Aug  21 2014 Thomas Bruederli <bruederli@kolabsys.com> - 3.8.2
- New upstream version

* Sun Jun  9 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.4-1
- New upstream version

* Sat Aug  4 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.1-0.3.beta2
- Suppress stdout print statement

* Tue Jul 17 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.1-0.2.beta2
- Make sure parameters to properties properly propagate through the stack

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug  5 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-3
- Install examples
- Fix tests for Python 2.7 and run them
- Add GPLv2 for parser.py to licenses

* Wed Aug  4 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-2
- State correct licenses

* Tue Aug  3 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-1
- Initial package version

