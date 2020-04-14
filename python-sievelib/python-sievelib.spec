%if 0%{?fedora}
%global with_python3 1
%{!?python3_version: %global python3_version %(%{__python3} -c "import sys; sys.stdout.write(sys.version[:3])")}
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

Name:           python-sievelib
Version:        0.5.2
Release:        2.30%{?dist}.kolab_16
Summary:        Managesieve library in Python

Group:          Development/Tools

License:        BSD
URL:            http://kolab.org/about/python-sievelib/
Source0:        sievelib-%{version}.tar.gz

BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  python-devel >= 2.4
%else
BuildRequires:  python2-devel >= 2.4
%endif
BuildRequires:  python-setuptools

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-docutils
BuildRequires:  python3-jinja2
BuildRequires:  python3-pygments
BuildRequires:  python3-nose
%endif # with_python3

%description
Client-side Sieve and Managesieve library written in Python.

* Sieve : An Email Filtering Language
  (`RFC 5228 <http://tools.ietf.org/html/rfc5228>`_)
* ManageSieve : A Protocol for Remotely Managing Sieve Scripts
  (`Draft <http://tools.ietf.org/html/draft-martin-managesieve-12>`_)

%if 0%{?with_python3}
%package -n     python3-sievelib
Summary:        Managesieve library in Python
Group:          Development/Tools

%description -n python3-sievelib
Client-side Sieve and Managesieve library written in Python.

* Sieve : An Email Filtering Language
  (`RFC 5228 <http://tools.ietf.org/html/rfc5228>`_)
* ManageSieve : A Protocol for Remotely Managing Sieve Scripts
  (`Draft <http://tools.ietf.org/html/draft-martin-managesieve-12>`_)
%endif # with_python3

%prep
%setup -q -n sievelib-%{version}

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif # with_python3

%build
%{__python} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf %{buildroot}

# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python} setup.py install --skip-build --root %{buildroot}

%check

%files
%doc COPYING
%{python_sitelib}/*

%if 0%{?with_python3}
%files -n python3-sievelib
%doc COPYING
%{python3_sitelib}/*
%endif # with_python3

%changelog
* Tue Aug 26 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5.2-2
- Fix Python 3 compatibility,
- Better verbosity in debug mode,
- Fix mixed use of tabs and spaces for indentation

* Tue Aug 19 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5.2-1
- Initial package
