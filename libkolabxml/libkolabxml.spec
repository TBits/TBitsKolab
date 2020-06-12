# Needed for opensuse build system
%if 0%{?opensuse_bs}
#!BuildIgnore:  fedora-logos-httpd
#!BuildIgnore:	httpd
%endif

%{?!mono_arches: %global mono_arches %{ix86} x86_64 sparc sparcv9 ia64 %{arm} alpha s390x ppc ppc64}

%ifarch %{mono_arches}
# No linux system is actually using the csharp bindings
%global with_csharp 0
%endif
%global with_java 1
%global with_php 1
%global with_python 1

%{expand: %(if [ `php-config --vernum` -gt 70000 ]; then echo %%global with_php7 1; else echo %%global with_php7 0; fi)}

%if 0%{?with_php} > 0
%if 0%{?suse_version}
%global php php5
%{!?php_extdir: %global php_extdir %{_libdir}/php5/extensions}
%{!?php_inidir: %global php_inidir %{_sysconfdir}/php5/conf.d/}
%else
%global php php
%{!?php_extdir: %global php_extdir %{_libdir}/php/modules}
%{!?php_inidir: %global php_inidir %{_sysconfdir}/php.d/}
%endif
%{!?php_apiver: %global php_apiver  %((echo 0; php -i 2>/dev/null | sed -n 's/^PHP API => //p') | tail -1)}
%endif

%if 0%{?with_python} > 0
%{!?python2_sitelib: %global python2_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

# Filter out private python and php libs. Does not work on EPEL5,
# therefor we use it conditionally
%if 0%{?with_php} > 0
%if 0%{?with_python} > 0
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_provides_in %{php_extdir}/.*\.so$
%filter_setup
}
%else
%{?filter_setup:
%filter_provides_in %{php_extdir}/.*\.so$
%filter_setup
}
%endif
%else
%if 0%{?with_python} > 0
%{?filter_setup:
%filter_provides_in %{python2_sitearch}/.*\.so$
%filter_setup
}
%endif
%endif

%if 0%{?suse_version}
Name:           libkolabxml1
%else
Name:           libkolabxml
%endif
Version:        1.2.0
Release:        14.7%{?dist}.kolab_16
Summary:        Kolab XML format collection parser library

Group:          System Environment/Libraries
License:        LGPLv3+
URL:            http://www.kolab.org

Source0:        libkolabxml-%{version}.tar.gz

Patch1002:      at11.0-boost-this_thread-hidden-sleep_until.patch

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:  boost-devel
BuildRequires:  cmake >= 2.6
%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires:  extra-cmake-modules
%endif
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  make
%if 0%{?suse_version}
BuildRequires:  qt-devel
%else
%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires:  qt5-qtbase-devel
%else
BuildRequires:  qt4-devel
%endif
%endif
BuildRequires:  swig
BuildRequires:  uuid-devel
BuildRequires:  xsd

%if 0%{?suse_version}
BuildRequires:  libxerces-c-devel
%else
BuildRequires:  xerces-c-devel
%endif

Provides:       libkolabxml%{?_isa} = %{version}

%if 0%{?with_csharp} < 1
Obsoletes:      csharp-kolabformat < %{version}-%{release}
Provides:       csharp-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_java} < 1
Obsoletes:      java-kolabformat < %{version}-%{release}
Provides:       java-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_php} < 1
Obsoletes:      php-kolabformat < %{version}-%{release}
Provides:       php-kolabformat = %{version}-%{release}
%endif

%if 0%{?with_python} < 1
Obsoletes:      python-kolabformat < %{version}-%{release}
Provides:       python-kolabformat = %{version}-%{release}
%endif

%description
The libkolabxml parsing library interprets Kolab XML formats (xCal, xCard)
with bindings for Python, PHP and other languages. The language bindings
are available through sub-packages.

%if 0%{?suse_version}
%package -n libkolabxml-devel
%else
%package devel
%endif
Summary:        Kolab XML library development headers
Group:          Development/Libraries
Requires:       libkolabxml%{?_isa} = %{version}
Requires:       boost-devel
Requires:       cmake >= 2.6
%if 0%{?rhel} >= 8 || 0%{?fedora}
Requires:       extra-cmake-modules
%endif
Requires:       e2fsprogs-devel
Requires:       gcc-c++
Requires:       libcurl-devel
%if 0%{?with_php} > 0
Requires:       php-devel >= 5.3
%if 0%{?plesk}
Requires:       plesk-php56-devel
Requires:       plesk-php70-devel
Requires:       plesk-php71-devel
Requires:       plesk-php72-devel
Requires:       plesk-php73-devel
Requires:       plesk-php74-devel
%endif
%endif
%if 0%{?with_python} > 0
%if 0%{?rhel} >= 8
Requires:       python2-devel
%else
Requires:       python-devel
%endif
%endif
%if 0%{?suse_version}
Requires:       qt-devel
%else
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       qt5-qtbase-devel
%else
Requires:       qt4-devel
%endif
%endif
Requires:       swig
Requires:       uuid-devel
%if 0%{?suse_version}
Requires:       libxerces-c-devel
%else
Requires:       xerces-c-devel
%endif
Requires:       xsd

%if 0%{?suse_version}
%description -n libkolabxml-devel
%else
%description devel
%endif
Development headers for the Kolab XML libraries.

%if 0%{?with_csharp} > 0
%package -n csharp-kolabformat
Summary:        C# Bindings for libkolabxml
Group:          System Environment/Libraries
Requires:       libkolabxml%{?_isa} = %{version}
%if 0%{?suse_version}
Obsoletes:      mono-%{name} < %{version}
Provides:       mono-%{name} = %{version}
%endif
BuildRequires:  mono-core

%description -n csharp-kolabformat
C# bindings for libkolabxml
%endif

%if 0%{?with_java} > 0
%package -n java-kolabformat
Summary:        Java Bindings for libkolabxml
Group:          System Environment/Libraries
Requires:       libkolabxml%{?_isa} = %{version}
%if 0%{?suse_version}
Obsoletes:      java-%{name} < %{version}
Provides:       java-%{name} = %{version}
%endif

%description -n java-kolabformat
Java bindings for libkolabxml
%endif

%if 0%{?with_php} > 0
%package -n php-kolabformat
Summary:        PHP bindings for libkolabxml
Group:          System Environment/Libraries
Provides:       php-bindings(libkolabxml) = %{version}-%{release}
Requires:       libkolabxml%{?_isa} = %{version}
%if 0%{?rhel} > 5 || 0%{?fedora} > 15
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
%else
Requires:       php-api = %{php_apiver}
%endif
%if 0%{?suse_version}
Obsoletes:      php-%{name} < %{version}
Provides:       php-%{name} = %{version}
%endif
# openSUSE apparently does not have its -devel subpackages require the base
# package
BuildRequires:  php >= 5.3
BuildRequires:  php-devel >= 5.3
%if 0%{?plesk}
BuildRequires:  plesk-php56-devel
BuildRequires:  plesk-php70-devel
BuildRequires:  plesk-php71-devel
BuildRequires:  plesk-php72-devel
BuildRequires:  plesk-php73-devel
BuildRequires:  plesk-php74-devel
%endif

%description -n php-kolabformat
The PHP kolabformat package offers a comprehensible PHP library using the
bindings provided through libkolabxml.
%endif

%if 0%{?plesk}
%package -n plesk-php56-kolabformat
Summary:        libkolabxml bindings for Plesk's PHP 5.6
Group:          System Environment/Libraries
Provides:       php-bindings(libkolabxml) = %{version}-%{release}
Requires:       libkolabxml%{?_isa} = %{version}
Requires:       plesk-php56

%description -n plesk-php56-kolabformat
libkolabxml bindings for Plesk's PHP 5.6

%package -n plesk-php70-kolabformat
Summary:        libkolabxml bindings for Plesk's PHP 7.0
Group:          System Environment/Libraries
Provides:       php-bindings(libkolabxml) = %{version}-%{release}
Requires:       libkolabxml%{?_isa} = %{version}
Requires:       plesk-php70

%description -n plesk-php70-kolabformat
libkolabxml bindings for Plesk's PHP 7.0

%package -n plesk-php71-kolabformat
Summary:        libkolabxml bindings for Plesk's PHP 7.1
Group:          System Environment/Libraries
Provides:       php-bindings(libkolabxml) = %{version}-%{release}
Requires:       libkolabxml%{?_isa} = %{version}
Requires:       plesk-php71

%description -n plesk-php71-kolabformat
libkolabxml bindings for Plesk's PHP 7.1

%package -n plesk-php72-kolabformat
Summary:        libkolabxml bindings for Plesk's PHP 7.2
Group:          System Environment/Libraries
Provides:       php-bindings(libkolabxml) = %{version}-%{release}
Requires:       libkolabxml%{?_isa} = %{version}
Requires:       plesk-php72

%description -n plesk-php72-kolabformat
libkolabxml bindings for Plesk's PHP 7.2

%package -n plesk-php73-kolabformat
Summary:        libkolabxml bindings for Plesk's PHP 7.3
Group:          System Environment/Libraries
Provides:       php-bindings(libkolabxml) = %{version}-%{release}
Requires:       libkolabxml%{?_isa} = %{version}
Requires:       plesk-php73

%description -n plesk-php73-kolabformat
libkolabxml bindings for Plesk's PHP 7.3

%package -n plesk-php74-kolabformat
Summary:        libkolabxml bindings for Plesk's PHP 7.4
Group:          System Environment/Libraries
Provides:       php-bindings(libkolabxml) = %{version}-%{release}
Requires:       libkolabxml%{?_isa} = %{version}
Requires:       plesk-php74

%description -n plesk-php74-kolabformat
libkolabxml bindings for Plesk's PHP 7.4
%endif # if 0%{?plesk}

%if 0%{?with_python} > 0
%package -n python-kolabformat
Summary:        Python bindings for libkolabxml
Group:          System Environment/Libraries
Requires:       libkolabxml%{?_isa} = %{version}
%if 0%{?suse_version}
Obsoletes:      python-%{name} < %{version}
Provides:       python-%{name} = %{version}
%endif
%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires:  python2-devel
%else
BuildRequires:  python-devel
%endif

%description -n python-kolabformat
The PyKolab format package offers a comprehensive Python library using the
bindings provided through libkolabxml.
%endif

%prep
%setup -q -c -n libkolabxml-%{version}
pwd
ls -l

%if 0%{?with_at}
%patch1002 -p1
%endif

%if 0%{?plesk}
cp -a libkolabxml-%{version} libkolabxml-%{version}-5.6

cp -a libkolabxml-%{version} libkolabxml-%{version}-7.0
sed -i "s/-php/-php7/g" libkolabxml-%{version}-7.0/src/php/CMakeLists.txt

cp -a libkolabxml-%{version} libkolabxml-%{version}-7.1
sed -i "s/-php/-php7/g" libkolabxml-%{version}-7.1/src/php/CMakeLists.txt

cp -a libkolabxml-%{version} libkolabxml-%{version}-7.2
sed -i "s/-php/-php7/g" libkolabxml-%{version}-7.2/src/php/CMakeLists.txt

cp -a libkolabxml-%{version} libkolabxml-%{version}-7.3
sed -i "s/-php/-php7/g" libkolabxml-%{version}-7.3/src/php/CMakeLists.txt

cp -a libkolabxml-%{version} libkolabxml-%{version}-7.4
sed -i "s/-php/-php7/g" libkolabxml-%{version}-7.4/src/php/CMakeLists.txt
%endif

%if 0%{?with_php7}
pushd %{name}-%{version}
sed -i "s/-php/-php7/g" src/php/CMakeLists.txt
popd
%endif

%build
pushd %{name}-%{version}
python utils/zonetabconversion.py
popd

%if 0%{?plesk}
cp %{name}-%{version}/tztable.h %{name}-%{version}-5.6/.
cp %{name}-%{version}/tztable.h %{name}-%{version}-7.0/.
cp %{name}-%{version}/tztable.h %{name}-%{version}-7.1/.
cp %{name}-%{version}/tztable.h %{name}-%{version}-7.2/.
cp %{name}-%{version}/tztable.h %{name}-%{version}-7.3/.
cp %{name}-%{version}/tztable.h %{name}-%{version}-7.4/.
%endif

pushd %{name}-%{version}
rm -rf build
mkdir -p build
pushd build
%if 0%{?suse_version}
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ;
FFLAGS="${FFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FFLAGS ;
FCFLAGS="${FCFLAGS:-%optflags%{?_fmoddir: -I%_fmoddir}}" ; export FCFLAGS ;
%{?__global_ldflags:LDFLAGS="${LDFLAGS:-%__global_ldflags}" ; export LDFLAGS ;}
cmake \
    -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \
    -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
    -DLIB_INSTALL_DIR:PATH=%{_libdir} \
    -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
    -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
%if "%{?_lib}" == "lib64"
    %{?_cmake_lib_suffix64} \
%endif
    -DBUILD_SHARED_LIBS:BOOL=ON \
%else # if 0${?suse_version}
%cmake \
%endif
    -DBoost_NO_BOOST_CMAKE=TRUE \
    -Wno-fatal-errors -Wno-errors \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_PREFIX_PATH=%{_libdir} \
%if 0%{?rhel} >= 8 || 0%{?fedora}
    -DQT5_BUILD=ON \
%endif
    -DINCLUDE_INSTALL_DIR=%{_includedir} \
%if 0%{?with_csharp} > 0
    -DCSHARP_BINDINGS=ON \
    -DCSHARP_INSTALL_DIR=%{_datadir}/%{name}/csharp/ \
%endif
%if 0%{?with_java} > 0
    -DJAVA_BINDINGS=ON \
    -DJAVA_INSTALL_DIR=%{_datadir}/%{name}/java/ \
%endif
%if 0%{?with_php} > 0
    -DPHP_BINDINGS=ON \
    -DPHP_INSTALL_DIR=%{php_extdir} \
%endif
%if 0%{?with_python} > 0
    -DPYTHON_BINDINGS=ON \
    -DPYTHON_INCLUDE_DIRS=%{python2_include} \
    -DPYTHON_INSTALL_DIR=%{python2_sitearch} \
%endif
    ..
make
popd
popd

%if 0%{?plesk}
for version in 5.6 7.0 7.1 7.2 7.3 7.4; do
    pushd %{name}-%{version}-${version}
    rm -rf build
    mkdir -p build
    pushd build
    %cmake \
        -DBoost_NO_BOOST_CMAKE=TRUE \
        -Wno-fatal-errors -Wno-errors \
        -DCMAKE_SKIP_RPATH=ON \
        -DCMAKE_PREFIX_PATH=%{_libdir} \
%if 0%{?rhel} >= 8 || 0%{?fedora}
        -DQT5_BUILD=ON \
%endif
        -DINCLUDE_INSTALL_DIR=%{_includedir} \
%if 0%{?with_php} > 0
        -DPHP_BINDINGS=ON \
        -DPHP_INCLUDE_DIR=/opt/plesk/php/${version}/include/php/ \
        -DPHP_EXECUTABLE=/opt/plesk/php/${version}/bin/php \
        -DPHP_INSTALL_DIR=/opt/plesk/php/${version}/lib64/php/modules/ \
%endif
        ..
    make
    popd
    popd
done
%endif

%install
rm -rf %{buildroot}
pushd %{name}-%{version}
pushd build
make install DESTDIR=%{buildroot} INSTALL='install -p'
popd

%if 0%{?with_php} > 0
mkdir -p \
    %{buildroot}/%{_datadir}/%{php} \
    %{buildroot}/%{php_inidir}/
mv %{buildroot}/%{php_extdir}/kolabformat.php %{buildroot}/%{_datadir}/%{php}/kolabformat.php
cat > %{buildroot}/%{php_inidir}/kolabformat.ini << EOF
extension=kolabformat.so
EOF
%endif
popd

%if 0%{?plesk}
for version in 5.6 7.0 7.1 7.2 7.3 7.4; do
    pushd %{name}-%{version}-${version}
    pushd build
    make install DESTDIR=%{buildroot} INSTALL='install -p'
    popd

    mkdir -p \
        %{buildroot}/opt/plesk/php/${version}/share/php/ \
        %{buildroot}/opt/plesk/php/${version}/etc/php.d/ \
        %{buildroot}/opt/plesk/php/${version}/etc/php-fpm.d/

    mv \
        %{buildroot}/opt/plesk/php/${version}/lib64/php/modules/kolabformat.php \
        %{buildroot}/opt/plesk/php/${version}/share/php/kolabformat.php

    echo "extension=kolabformat.so" > %{buildroot}/opt/plesk/php/${version}/etc/php.d/kolabformat.ini
    cp %{buildroot}/opt/plesk/php/${version}/etc/php.d/kolabformat.ini \
        %{buildroot}/opt/plesk/php/${version}/etc/php-fpm.d/
    popd
done
%endif

%check
pushd %{name}-%{version}/build
# Make sure libkolabxml.so.* is found, otherwise the tests fail
export LD_LIBRARY_PATH=$( pwd )/src/
pushd tests
./bindingstest ||:
./conversiontest ||:
./parsingtest ||:
popd
%if 0%{?with_php} > 0
php -d enable_dl=On -dextension=src/php/kolabformat.so src/php/test.php ||:
%endif
%if 0%{?with_python} > 0
python src/python/test.py ||:
%endif
popd

%if 0%{?plesk}
for version in 5.6 7.0 7.1 7.2 7.3 7.4; do
    pushd %{name}-%{version}-${version}/build/
    export LD_LIBRARY_PATH=$( pwd )/src/
    /opt/plesk/php/${version}/bin/php -d enable_dl=On -dextension=src/php/kolabformat.so src/php/test.php ||:
    popd
done
%endif

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc %{name}-%{version}/DEVELOPMENT %{name}-%{version}/NEWS %{name}-%{version}/README
%{_libdir}/*.so.*

%if 0%{?suse_version}
%files -n libkolabxml-devel
%else
%files devel
%endif
%defattr(-,root,root,-)
%{_includedir}/kolabxml
%{_libdir}/*.so
%{_libdir}/cmake/Libkolabxml

%if 0%{?with_csharp} > 0
%files -n csharp-kolabformat
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/csharp
%endif

%if 0%{?with_java} > 0
%files -n java-kolabformat
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/java
%endif

%if 0%{?with_php} > 0
%files -n php-kolabformat
%defattr(-,root,root,-)
%{_datadir}/%{php}/kolabformat.php
%{php_extdir}/kolabformat.so
%config(noreplace) %{php_inidir}/kolabformat.ini

%if 0%{?plesk}
%files -n plesk-php56-kolabformat
%defattr(-,root,root,-)
/opt/plesk/php/5.6/lib64/php/modules/kolabformat.so
/opt/plesk/php/5.6/share/php/kolabformat.php
/opt/plesk/php/5.6/etc/php.d/kolabformat.ini
/opt/plesk/php/5.6/etc/php-fpm.d/kolabformat.ini

%files -n plesk-php70-kolabformat
%defattr(-,root,root,-)
/opt/plesk/php/7.0/lib64/php/modules/kolabformat.so
/opt/plesk/php/7.0/share/php/kolabformat.php
/opt/plesk/php/7.0/etc/php.d/kolabformat.ini
/opt/plesk/php/7.0/etc/php-fpm.d/kolabformat.ini

%files -n plesk-php71-kolabformat
%defattr(-,root,root,-)
/opt/plesk/php/7.1/lib64/php/modules/kolabformat.so
/opt/plesk/php/7.1/share/php/kolabformat.php
/opt/plesk/php/7.1/etc/php.d/kolabformat.ini
/opt/plesk/php/7.1/etc/php-fpm.d/kolabformat.ini

%files -n plesk-php72-kolabformat
%defattr(-,root,root,-)
/opt/plesk/php/7.2/lib64/php/modules/kolabformat.so
/opt/plesk/php/7.2/share/php/kolabformat.php
/opt/plesk/php/7.2/etc/php.d/kolabformat.ini
/opt/plesk/php/7.2/etc/php-fpm.d/kolabformat.ini

%files -n plesk-php73-kolabformat
%defattr(-,root,root,-)
/opt/plesk/php/7.3/lib64/php/modules/kolabformat.so
/opt/plesk/php/7.3/share/php/kolabformat.php
/opt/plesk/php/7.3/etc/php.d/kolabformat.ini
/opt/plesk/php/7.3/etc/php-fpm.d/kolabformat.ini

%files -n plesk-php74-kolabformat
%defattr(-,root,root,-)
/opt/plesk/php/7.4/lib64/php/modules/kolabformat.so
/opt/plesk/php/7.4/share/php/kolabformat.php
/opt/plesk/php/7.4/etc/php.d/kolabformat.ini
/opt/plesk/php/7.4/etc/php-fpm.d/kolabformat.ini

%endif # if 0%{?plesk}

%endif # if 0%{?with_php}

%if 0%{?with_python} > 0
%files -n python-kolabformat
%defattr(-,root,root,-)
%{python2_sitearch}/kolabformat.py*
%{python2_sitearch}/_kolabformat.so
%endif

%changelog
* Tue May 14 2019 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.2.0
- Release of version 1.2.0

* Thu May 28 2015 Christian Mollekopf <mollekopf@kolabsys.com> - 1.2
- New upstream release
- Removed dependency on kdepimlibs and kdelibs which is not required

* Mon Jan 13 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.1-2
- Require php-kolab for php-kolabformat, and void
  /etc/php.d/kolabformat.ini (#2667)

* Wed Oct 30 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.1-1
- New upstream release

* Mon Oct 14 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.0-1
- New upstream release

* Sun May 19 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.1
- Snapshot as required by the latest versions of roundcubemail-plugins-kolab
  and iRony

* Thu Apr 11 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.8.4-1
- New upstream release

* Tue Feb 26 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.8.3-1
- New upstream release with file format handling

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.8.1-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.8.1-3
- Rebuild for Boost-1.53.0

* Wed Aug 22 2012 Dan Horák <dan[at]danny.cz> - 0.8.1-2
- build csharp subpackage only when Mono exists

* Wed Aug 15 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.8.1-1
- New upstream version 0.8.1
- Revert s/qt-devel/qt4-devel/ - just require the latest qt-devel
- Revert s/kdelibs-devel/kdelibs4-devel/ - also require the latest
  kdelibs (frameworks FTW!)

* Sun Aug 12 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.7.0-3
- drop BR: gcc-c++
- s/qt-devel/qt4-devel/ s/kdelibs-devel/kdelibs4-devel/
- fix build against boost-1.50

* Wed Jul 25 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7.0-2
- Fix build on ppc64
- New upstream version

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6.0-3
- Correct dependency on php

* Tue Jun 26 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6.0-2
- Also remove xsd-utils requirement for -devel sub-package

* Mon Jun 25 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6.0-1
- Actual 0.6.0 release

* Sat Jun 23 2012 Christoph Wickert <wickert@kolabsys.com> - 0.6-1
- Update to 0.6 final
- Run ldconfig in %%post and %%postun
- Mark kolabformat.ini as config file
- Export LD_LIBRARY_PATH so tests can be run in %%check
- Add php dependencies to php-kolabformat package
- Make base package requirements are arch-specific
- Filter unwanted provides of php-kolabformat and python-kolabformat

* Wed Jun 20 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-0.4
- Some other cleanups to prevent review scrutiny from blocking
  inclusion
- Drop build requirement for xsd-utils

* Sat Jun  9 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-0.2
- Git snapshot release

* Wed May 23 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5-5
- Correct use of Python keyword None
- Snapshot version with attendee cutype support

* Tue May 22 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5-3
- Snapshot version with attendee delegation support

* Sat May 12 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.5-2
- Snapshot version with build system changes

* Wed May  9 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.4.0-3
- Fix PHP kolabformat module packaging

* Wed May  2 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.4.0-2
- New version

* Fri Apr 20 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.0-1
- New version

* Mon Apr  9 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3-0.1
- First package

