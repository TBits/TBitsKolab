%if 0%{?suse_version}
%define nspr_name       mozilla-nspr
%else
%define nspr_name       nspr
%endif
%define nspr_version    4.6

%if 0%{?suse_version}
%define nss_name        mozilla-nss
%else
%define nss_name        nss
%endif
%define nss_version     3.11

%define svrcore_name    svrcore
%define svrcore_version 4.0.3

%define major           6
%define minor           0
%define submin          7
%define libsuffix       %{major}0

Summary:          Mozilla LDAP C SDK
Name:             mozldap
Version:          %{major}.%{minor}.%{submin}
Release:          1%{?dist}
License:          MPLv1.1 or GPLv2+ or LGPLv2+
URL:              http://www.mozilla.org/directory/csdk.html
Group:            System Environment/Libraries
Requires:         %{nspr_name} >= %{nspr_version}
Requires:         %{nss_name} >= %{nss_version}
%if 0%{?suse_version}
Requires:         lib%{svrcore_name}0 >= %{svrcore_version}
%else
Requires:         %{svrcore_name} >= %{svrcore_version}
%endif
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:    %{nspr_name}-devel >= %{nspr_version}
BuildRequires:    %{nss_name}-devel >= %{nss_version}
BuildRequires:    %{svrcore_name}-devel >= %{svrcore_version}
BuildRequires:    gcc-c++
BuildRequires:    cyrus-sasl-devel

Source0:          ftp://ftp.mozilla.org/pub/mozilla.org/directory/c-sdk/releases/v%{version}/src/%{name}-%{version}.tar.gz

%description
The Mozilla LDAP C SDK is a set of libraries that
allow applications to communicate with LDAP directory
servers.  These libraries are derived from the University
of Michigan and Netscape LDAP libraries.  They use Mozilla
NSPR and NSS for crypto.


%package tools
Summary:          Tools for the Mozilla LDAP C SDK
Group:            System Environment/Base
Requires:         %{name} = %{version}-%{release}
BuildRequires:    %{nspr_name}-devel >= %{nspr_version}
BuildRequires:    %{nss_name}-devel >= %{nss_version}
BuildRequires:    %{svrcore_name}-devel >= %{svrcore_version}

%description tools
The mozldap-tools package provides the ldapsearch,
ldapmodify, and ldapdelete tools that use the
Mozilla LDAP C SDK libraries.


%package devel
Summary:          Development libraries and examples for Mozilla LDAP C SDK
Group:            Development/Libraries
Requires:         %{name} = %{version}-%{release}
Requires:         %{nspr_name}-devel >= %{nspr_version}
Requires:         %{nss_name}-devel >= %{nss_version}
Requires:         %{svrcore_name}-devel >= %{svrcore_version}
Requires:         pkgconfig

%description devel
Header and Library files for doing development with the Mozilla LDAP C SDK

%prep
%setup -q

%build
cd c-sdk

%configure \
%ifarch x86_64 ppc64 ia64 s390x sparc64
    --enable-64bit \
%endif
    --with-sasl \
    --enable-clu \
    --with-system-svrcore \
    --enable-optimize \
    --disable-debug

# Enable compiler optimizations and disable debugging code
BUILD_OPT=1
export BUILD_OPT

# Generate symbolic info for debuggers
XCFLAGS="$RPM_OPT_FLAGS"
export XCFLAGS

PKG_CONFIG_ALLOW_SYSTEM_LIBS=1
PKG_CONFIG_ALLOW_SYSTEM_CFLAGS=1

export PKG_CONFIG_ALLOW_SYSTEM_LIBS
export PKG_CONFIG_ALLOW_SYSTEM_CFLAGS

make \
%ifarch x86_64 ppc64 ia64 s390x sparc64
    USE_64=1
%endif

%install
%{__rm} -rf $RPM_BUILD_ROOT

# Set up our package file
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/pkgconfig
%{__cat} c-sdk/mozldap.pc.in \
    | sed -e "s,%%libdir%%,%{_libdir},g" \
          -e "s,%%prefix%%,%{_prefix},g" \
          -e "s,%%major%%,%{major},g" \
          -e "s,%%minor%%,%{minor},g" \
          -e "s,%%submin%%,%{submin},g" \
          -e "s,%%libsuffix%%,%{libsuffix},g" \
          -e "s,%%bindir%%,%{_libdir}/%{name},g" \
          -e "s,%%exec_prefix%%,%{_prefix},g" \
          -e "s,%%includedir%%,%{_includedir}/%{name},g" \
          -e "s,%%NSPR_VERSION%%,%{nspr_version},g" \
          -e "s,%%NSS_VERSION%%,%{nss_version},g" \
          -e "s,%%SVRCORE_VERSION%%,%{svrcore_version},g" \
          -e "s,%%MOZLDAP_VERSION%%,%{version},g" \
    > $RPM_BUILD_ROOT%{_libdir}/pkgconfig/%{name}.pc

# There is no make install target so we'll do it ourselves.

%{__mkdir_p} $RPM_BUILD_ROOT%{_includedir}/%{name}
%if "%{_libexecdir}" != "%{_libdir}"
%{__mkdir_p} $RPM_BUILD_ROOT%{_libexecdir}/%{name}
%endif
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/%{name}

# Copy the binary libraries we want
for file in libssldap%{libsuffix}.so libprldap%{libsuffix}.so libldap%{libsuffix}.so libldif%{libsuffix}.so
do
  %{__install} -m 755 ../dist/lib/$file $RPM_BUILD_ROOT%{_libdir}
done

# Copy the binaries we want
for file in ldapsearch ldapmodify ldapdelete ldapcmp ldapcompare ldappasswd
do
  %{__install} -m 755 ../dist/bin/$file $RPM_BUILD_ROOT%{_libexecdir}/%{name}
%if "%{_libexecdir}" != "%{_libdir}"
  pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
  ln -s ../../..%{_libexecdir}/%{name}/$file $file
  popd
%endif
done

# Copy the include files
for file in ../dist/public/ldap/*.h
do
  %{__install} -p -m 644 $file $RPM_BUILD_ROOT%{_includedir}/%{name}
done

# Copy the developer files
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r c-sdk/ldap/examples $RPM_BUILD_ROOT%{_datadir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/%{name}/etc
%{__install} -m 644 c-sdk/ldap/examples/xmplflt.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/etc
%{__install} -m 644 c-sdk/ldap/libraries/libldap/ldaptemplates.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/etc
%{__install} -m 644 c-sdk/ldap/libraries/libldap/ldapfilter.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/etc
%{__install} -m 644 c-sdk/ldap/libraries/libldap/ldapsearchprefs.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/etc

%pre
%if "%{_libexecdir}" != "%{_libdir}"
for file in ldapsearch ldapmodify ldapdelete ldapcmp ldapcompare ldappasswd; do
    if [ -f "%{_libdir}/%{name}/${file}" -a ! -L "%{_libdir}/%{name}/${file}" ]; then
        rm -rf %{_libdir}/%{name}/${file}
    fi
done
%endif

%clean
%{__rm} -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc c-sdk/README.rpm
%{_libdir}/libssldap*.so
%{_libdir}/libprldap*.so
%{_libdir}/libldap*.so
%{_libdir}/libldif*.so

%files tools
%defattr(-,root,root,-)
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/ldapsearch
%{_libexecdir}/%{name}/ldapmodify
%{_libexecdir}/%{name}/ldapdelete
%{_libexecdir}/%{name}/ldapcmp
%{_libexecdir}/%{name}/ldapcompare
%{_libexecdir}/%{name}/ldappasswd
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/ldapsearch
%{_libdir}/%{name}/ldapmodify
%{_libdir}/%{name}/ldapdelete
%{_libdir}/%{name}/ldapcmp
%{_libdir}/%{name}/ldapcompare
%{_libdir}/%{name}/ldappasswd
%endif

%files devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_datadir}/%{name}

%changelog
* Sat Apr 07 2018 Christoph Erhardt <kolab@sicherha.de> - 6.0.7-1
- Bump version to 6.0.7.

* Wed Oct 30 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 6.0.5-11
- Move the commands from a lib_t labeled directory to a bin_t labeled
  directory.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 6.0.5-4
- actually fix license tag (whoops)

* Mon Aug 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 6.0.5-3
- fix license tag
- enable sparc64

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 6.0.5-2
- Autorebuild for GCC 4.3

* Wed Sep 26 2007 Rich Megginson <rmeggins@redhat.com> - 6.0.5-1
- bump to version 6.0.5 - this version allows the use of SASL
- with IPv6 numeric addresses, as well as some memory leak fixes

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 6.0.4-2
- Rebuild for selinux ppc32 issue.

* Wed Jun 20 2007 Rich Megginson <rmeggins@redhat.com> - 6.0.4-1
- bump version to 6.0.4 - this version has some memory leak
- fixes for SASL related code, fixes for control handling with
- referral chasing, and packaging improvements
- use -p when installing include files to preserve timestamps

* Thu May 24 2007 Rich Megginson <rmeggins@redhat.com> - 6.0.3-3
- We only need cyrus-sasl-devel as a BuildRequires in the main package

* Mon May 21 2007 Rich Megginson <rmeggins@redhat.com> - 6.0.3-2
- added cyrus-sasl-devel and pkgconfig to devel package Requires

* Tue Mar 13 2007 Rich Megginson <richm@stanfordalumni.org> - 6.0.3-1
- bumped version to 6.0.3
- minor build fixes for some platforms

* Mon Jan 15 2007 Rich Megginson <richm@stanfordalumni.org> - 6.0.2-1
- Fixed exports file generation for Solaris and Windows - no effect on linux
- bumped version to 6.0.2

* Tue Jan  9 2007 Rich Megginson <richm@stanfordalumni.org> - 6.0.1-2
- Remove buildroot = "/" checking
- Remove buildroot removal from %%build section

* Mon Jan  8 2007 Rich Megginson <richm@stanfordalumni.org> - 6.0.1-1
- bump version to 6.0.1
- added libldif and ldif.h

* Fri Dec  8 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 6.0.0-2
- Rename to mozldap.
- move configure step to %%build section.
- clean up excessive use of %%defines, make more Fedora like.
- fix mismatching soname issue.
- generic specfile cosmetics.

* Thu Oct  5 2006 Rich Megginson <richm@stanforalumni.org> - 6.0.0-1
- Bump version to 6.0.0 - add support for submit/patch level (3rd level) in version numbering

* Tue Apr 18 2006 Richard Megginson <richm@stanforalumni.org> - 5.17-3
- make more Fedora Core friendly - move each requires and buildrequires to a separate line
- remove --with-nss since svrcore implies it; fix some macro errors; macro-ize nspr and nss names
- fix directory attrs in devel package

* Tue Jan 31 2006 Rich Megginson <rmeggins@redhat.com> - 5.17-2
- use --with-system-svrcore to configure

* Mon Dec 19 2005 Rich Megginson <rmeggins@redhat.com> - 5.17-1
- Initial revision

