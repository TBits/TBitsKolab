Name:           libcalendaring
Version: 4.9.2
Release: 8.4%{?dist}.kolab_16
Summary:        Library for Calendaring

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.kolab.org/about/libcalendaring

Source0:        libcalendaring-4.9.2.tar.gz

Patch0001:      0001-Correct-shebangs.patch
# ical3 support for CentOS 7.6 from https://cgit.kolab.org/libcalendaring/commit/?id=fc5d939abcc32c03f3513ae9239b2b3c765329f5
Patch0002:      0002-ical3-support.patch
Patch0003:      0003-debug-messages.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc-c++
BuildRequires:  libical-devel
BuildRequires:  make
%if 0%{?fedora} >= 25
# we need perl for kabc/scripts/makeaddressee
BuildRequires:  perl
%endif
%if 0%{?suse_version}
BuildRequires:  qt-devel
%else
BuildRequires:  qt4-devel
%endif
%if 0%{?fedora} == 24
# have choice for python-requests-kerberos needed by koji: python2-requests-kerberos python-requests-kerberos
BuildRequires:  python2-requests-kerberos
%endif

#Requires:	

%description
Advanced calendaring library for Kolab, based on parts of KDE >= 4.9

%package devel
Summary:        Development headers
Group:          System Environment/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
These are development headers. Don't bother.

%prep
%setup -q

%patch0001 -p1
%patch0002 -p1
%patch0003 -p1

%build
mkdir build
pushd build
%if 0%{?suse_version}
cmake \
%else
%cmake \
%endif
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DLIB_INSTALL_DIR=%{_libdir} \
    -DQT_NO_DEBUG_OUTPUT=1 \
    -DQT_NO_WARNING_OUTPUT=1 \
    ..

popd

%install
pushd build
make install DESTDIR=%{buildroot}
popd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libcalendaring-*.so.*

%files devel
%{_includedir}/calendaring
%{_libdir}/libcalendaring*.so
%{_libdir}/libcalendaring*.a

%changelog
* Fri Mar 20 2020 Christian Mollekopf <mollekopf@kolabsys.com> - 4.9.2-2
- adding patch to remove unnecessarily noisy debug messages

* Tue Jan 08 2018 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 4.9.2-1
- adding patch to build on CentOS 7.6 and Fedora 28 with ical3

* Mon Feb 23 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 4.9.1-1
- New upstream version 4.9.1

* Fri Aug  3 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 4.9.0-1
- New upstream version 4.9.0

* Wed Jul 25 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 4.9-1
- This too is a package
