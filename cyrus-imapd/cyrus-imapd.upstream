%if 0%{?opensuse_bs} && 0%{?suse_version} < 1
#!BuildIgnore:  systemd
%endif

%if 0%{?suse_version} < 1 && 0%{?fedora} < 1 && 0%{?rhel} < 7
%global with_systemd 0
%else
%global with_systemd 1
%{!?_unitdir: %global _unitdir /usr/lib/systemd/system}
%endif

%global ssl_pem_file %{_sysconfdir}/pki/%{name}/%{name}.pem

%global uid 76
%global gid 76

%global _cyrususer cyrus
%global _cyrusgroup mail
%global _cyrexecdir %{_exec_prefix}/lib/%{name}

%global tag_version 2.5.15
%global revision    28
%global git_hash    g7d1550bfa

##
## Options
##

%global with_bdb        0
%global with_mysql      0
%global with_pgsql      0

%global with_dav        0
%global with_tcpwrap    0
%global with_zlib       0

Name:               cyrus-imapd
Summary:            A high-performance mail server with IMAP, POP3, NNTP and SIEVE support
Version:            %{tag_version}.%{revision}
Release:            1.8%{?dist}.kolab_16
License:            BSD
Group:              System Environment/Daemons
URL:                http://www.cyrusimap.org

Source0:            ftp://ftp.andrew.cmu.edu/pub/cyrus/%{name}-%{tag_version}-%{revision}-%{git_hash}.tar.gz
Source1:            cyrus-imapd.imap-2.3.x-conf
Source2:            cyrus-imapd.cvt_cyrusdb_all
Source3:            cyrus-imapd.magic

# Distribution specific sources
Source11:           cyrus-imapd.logrotate
Source12:           cyrus-imapd.pam-config
Source13:           cyrus-imapd.cron-daily

# SysVinit
Source21:           cyrus-imapd.init
Source22:           cyrus-imapd.sysconfig

# Systemd support
Source31:           cyrus-imapd.service
Source32:           cyr_systemd_helper

##
## Patches
##
Patch0003:          0003-Canonification-for-multiple-domains.patch

BuildRoot:          %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

##
## Build Requirements
##
BuildRequires:      autoconf
BuildRequires:      automake
BuildRequires:      bison
BuildRequires:      cyrus-sasl-devel
%if 0%{?suse_version}
BuildRequires:      cunit-devel
BuildRequires:      cyrus-sasl-digestmd5
%else
BuildRequires:      CUnit-devel
BuildRequires:      cyrus-sasl-md5
%endif
BuildRequires:      cyrus-sasl-plain

%if 0%{?with_bdb}
%if 0%{?suse_version}
BuildRequires:      db-devel
%else
%if 0%{?fedora} > 15 || 0%{?rhel} > 6
BuildRequires:      libdb-devel
%else
BuildRequires:      db4-devel
%endif
%endif
%endif

BuildRequires:      flex
#BuildRequires:      gcc-c++
BuildRequires:      gcc

%if 0%{?suse_version} >= 1310
BuildRequires:      groff-full
%else
BuildRequires:      groff
%endif

%if 0%{?suse_version}
BuildRequires:      libjansson4-devel
%else
BuildRequires:      jansson-devel
%endif
BuildRequires:      krb5-devel

%if 0%{?with_dav}
BuildRequires:      libical-devel
%endif

BuildRequires:      libtool
BuildRequires:      libuuid-devel

%if 0%{?with_mysql}
BuildRequires:      mysql-devel
%endif

%if 0%{?suse_version}
BuildRequires:      openldap2-devel
%else
BuildRequires:      openldap-devel
%endif

BuildRequires:      openssl-devel
BuildRequires:      perl(ExtUtils::MakeMaker)

%if 0%{?suse_version}
BuildRequires:      perl
%else
BuildRequires:      perl-devel
%endif

BuildRequires:      pkgconfig

%if 0%{?with_pgsql}
BuildRequires:      postgresql-devel
%endif

%if 0%{?with_dav}
BuildRequires:      sqlite-devel
%endif

%if 0%{?with_systemd}
%if 0%{?suse_version}
BuildRequires:      systemd
%endif
%endif

%if 0%{?with_tcpwrap}
%if 0%{?suse_version}
BuildRequires:      tcpd-devel
%else
BuildRequires:      tcp_wrappers
%endif
%endif

BuildRequires:      transfig
%if 0
# Disable the xapian-core requirement
BuildRequires:      xapian-core-devel
%endif

%if 0%{?suse_version}
PreReq:             /usr/sbin/groupadd
PreReq:             /usr/sbin/useradd
%endif

%if 0%{?suse_version}
Requires:           db-utils
%else
Requires:           db4-utils
%endif

Requires:           file
Requires:           perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Requires(post):     coreutils
Requires(post):     e2fsprogs
Requires(post):     findutils
Requires(post):     grep
Requires(post):     make
Requires(post):     openssl
Requires(post):     perl
Requires(preun):    coreutils

%if 0%{?with_systemd}
%if 0%{?suse_version}
PreReq:             %fillup_prereq
%{?systemd_requires}
%else
%if 0%{?opensuse_bs} == 0
Requires(post):     systemd-units
Requires(preun):    systemd-units, coreutils
Requires(postun):   systemd-units
%endif
%endif
%else
%if 0%{?suse_version}
PreReq:             %fillup_prereq
PreReq:             %insserv_prereq
%else
Requires(preun):    chkconfig
Requires(preun):    initscripts
Requires(post):     chkconfig
Requires(post):     initscripts
Requires(postun):   initscripts
%endif
%endif

Obsoletes:          %{name}-perl < %{version}-%{release}
Provides:           %{name}-perl = %{version}-%{release}
Obsoletes:          %{name}-utils < %{version}-%{release}
Provides:           %{name}-utils = %{version}-%{release}

%description
The %{name} package contains the core of the Cyrus IMAP server.
It is a scaleable enterprise mail system designed for use from
small to large enterprise environments using standards-based
internet mail technologies.

A full Cyrus IMAP implementation allows a seamless mail and bulletin
board environment to be set up across multiple servers. It differs from
other IMAP server implementations in that it is run on "sealed"
servers, where users are not normally permitted to log in and have no
system account on the server. The mailbox database is stored in parts
of the filesystem that are private to the Cyrus IMAP server. All user
access to mail is through software using the IMAP, POP3 or KPOP
protocols. It also includes support for virtual domains, NNTP,
mailbox annotations, and much more. The private mailbox database design
gives the server large advantages in efficiency, scalability and
administratability. Multiple concurrent read/write connections to the
same mailbox are permitted. The server supports access control lists on
mailboxes and storage quotas on mailbox hierarchies.

The Cyrus IMAP server supports the IMAP4rev1 protocol described
in RFC 3501. IMAP4rev1 has been approved as a proposed standard.
It supports any authentication mechanism available from the SASL
library, imaps/pop3s/nntps (IMAP/POP3/NNTP encrypted using SSL and
TLSv1) can be used for security. The server supports single instance
store where possible when an email message is addressed to multiple
recipients, SIEVE provides server side email filtering.

%package devel
Group: Development/Libraries
Summary: Cyrus IMAP server development files

%description devel
The %{name}-devel package contains header files and libraries
necessary for developing applications which use the imclient library.

%prep
%setup -q -n %{name}-%{tag_version}-%{revision}-%{git_hash}

%if 0%{?with_bdb} < 1
sed -i -e 's/,berkeley//g' cunit/aaa-db.testc
sed -r -i -e 's/"berkeley(|-[a-z-]+)", //g' lib/imapoptions
%endif

%if 0%{?kolab_enterprise} < 1
%patch0003 -p1
%endif

# only to update config.* files
autoreconf -vi || (libtoolize --force && autoreconf -vi)

# Modify docs master --> cyrus-master
%{__perl} -pi -e "s@master\(8\)@cyrus-master(8)@" man/*5 man/*8 lib/imapoptions
%{__sed} -i -e 's|\([^-]\)master|\1cyrus-master|g;s|^master|cyrus-master|g;s|Master|Cyrus-master|g;s|MASTER|CYRUS-MASTER|g' \
        man/master.8 doc/man.html

%if 0%{?with_dav}
# Modify docs httpd --> cyrus-httpd
%{__perl} -pi -e "s@httpd\(8\)@cyrus-httpd(8)@" man/*5 man/*8 lib/imapoptions
%{__sed} -i -e 's|\([^-]\)httpd|\1cyrus-httpd|g;s|^httpd|cyrus-httpd|g;s|Httpd|Cyrus-httpd|g;s|HTTPD|CYRUS-HTTPD|g' \
        man/httpd.8 doc/man.html
%endif

# Modify path in perl scripts
find . -type f -name "*.pl" | xargs %{__perl} -pi -e "s@/usr/local/bin/perl@%{__perl}@"

# modify lmtp socket path in .conf files
%{__perl} -pi -e "s@/var/imap/@%{_var}/lib/imap/@" master/conf/*.conf doc/cyrusv2.mc doc/m4/%{name}-sendmail-8.12.9-cyrusv2.m4

# enable idled in .conf files to prevent error messages
%{__perl} -pi -e "s/#  idled/  idled/" master/conf/*.conf

%build
CPPFLAGS="%{?optflags} -I%{_includedir}/et -I%{_includedir}/kerberosIV"; export CPPFLAGS
CFLAGS="%{?optflags} -fPIC"; export CFLAGS
CXXFLAGS="%{?optflags} -fPIC"; export CXXFLAGS
CCDLFLAGS="-rdynamic"; export CCDLFLAGS
%ifnarch ppc ppc64
LDFLAGS="$LDFLAGS -pie"; export LDFLAGS
%endif

%{configure} \
    --enable-event-notification \
    --enable-gssapi \
    --enable-idled \
    --enable-murder \
    --enable-netscapehack \
    --enable-nntp \
    --enable-replication \
    --enable-unit-tests \
%if 0
    --enable-xapian \
%endif
%if 0%{?with_bdb}
%if 0%{?fedora} >= 20 || 0%{?rhel} || 0%{?suse_version}
    --with-bdb-incdir=%{_includedir}/db4 \
%else
    --with-bdb-incdir=%{_includedir}/libdb4 \
%endif
%else
    --without-bdb \
%endif
    --with-cyrus-prefix=%{_cyrexecdir} \
    --with-extraident="Kolab-%{version}-%{release}" \
    --without-clamav \
%if 0%{?with_tcpwrap} < 1
    --without-wrap \
%endif
%if 0%{?with_zlib} < 1
    --without-zlib \
%endif
%if 0%{?with_dav}
    --with-http \
%endif
    --with-krbimpl=mit \
    --with-ldap=/usr \
%if 0%{?with_mysql}
    --with-mysql=%{_prefix} \
    --with-mysql-incdir=%{_includedir}/mysql/ \
    --with-mysql-libdir=%{_libdir}/mysql/ \
%endif
    --with-perl=%{__perl} \
%if 0%{?with_pgsql}
    --with-pgsql=%{_includedir} \
%endif
    --with-service-path=%{_cyrexecdir} \
    --with-syslogfacility=MAIL

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}

# Fix permissions on perl programs
find . -type f -name "*.pl" -exec %{__chmod} 755 {} \;

# Do what the regular make install does
%{__make} install DESTDIR=%{buildroot} PREFIX=%{_prefix} mandir=%{_mandir} INSTALLDIRS=vendor

# Install tools
for tool in tools/* ; do
  test -f ${tool} && %{__install} -m 755 ${tool} %{buildroot}%{_cyrexecdir}/
done
rm -rf %{buildroot}%{_cyrexecdir}/htmlstrip.c
rm -rf %{buildroot}%{_cyrexecdir}/config2rst
rm -rf %{buildroot}%{_cyrexecdir}/perl2rst

# Create directories
%{__install} -d \
  %{buildroot}%{_sysconfdir}/{logrotate.d,pam.d,cron.daily} \
  %{buildroot}%{_libdir}/sasl \
  %{buildroot}%{_var}/spool/imap \
  %{buildroot}%{_var}/lib/imap/{user,quota,proc,log,msg,socket,db,sieve,sync,md5,rpm,backup,meta} \
  %{buildroot}%{_var}/lib/imap/ptclient \
  %{buildroot}%{_sysconfdir}/pki/%{name} \
  doc/contrib

# Install additional files
%{__install} -p -m 644 master/conf/prefork.conf %{buildroot}%{_sysconfdir}/cyrus.conf
%{__install} -p -m 644 %{SOURCE1}    %{buildroot}%{_sysconfdir}/imapd.conf
%{__install} -p -m 755 %{SOURCE2}   %{buildroot}%{_cyrexecdir}/cvt_cyrusdb_all
%{__install} -p -m 644 %{SOURCE3}   %{buildroot}%{_var}/lib/imap/rpm/magic
%{__install} -p -m 644 %{SOURCE11}    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
%{__install} -p -m 644 %{SOURCE12}    %{buildroot}%{_sysconfdir}/pam.d/pop
%{__install} -p -m 644 %{SOURCE12}    %{buildroot}%{_sysconfdir}/pam.d/imap
%{__install} -p -m 644 %{SOURCE12}    %{buildroot}%{_sysconfdir}/pam.d/sieve
%{__install} -p -m 644 %{SOURCE12}    %{buildroot}%{_sysconfdir}/pam.d/mupdate
%{__install} -p -m 644 %{SOURCE12}    %{buildroot}%{_sysconfdir}/pam.d/lmtp
%{__install} -p -m 644 %{SOURCE12}    %{buildroot}%{_sysconfdir}/pam.d/nntp
%{__install} -p -m 644 %{SOURCE12}    %{buildroot}%{_sysconfdir}/pam.d/csync
%{__install} -p -m 755 %{SOURCE13}   %{buildroot}%{_sysconfdir}/cron.daily/%{name}
%if 0%{?suse_version}
%{__install} -d %{buildroot}%{_localstatedir}/adm/fillup-templates/
%{__install} -p -m 644 %{SOURCE22}   %{buildroot}%{_localstatedir}/adm/fillup-templates/sysconfig.%{name}
%else
%{__install} -d %{buildroot}%{_sysconfdir}/sysconfig/
%{__install} -p -m 644 %{SOURCE22}   %{buildroot}%{_sysconfdir}/sysconfig/%{name}
%endif

%if 0%{?with_systemd}
%{__install} -p -D -m 644 %{SOURCE31}   %{buildroot}%{_unitdir}/cyrus-imapd.service
%{__install} -p -D -m 755 %{SOURCE32}   %{buildroot}%{_cyrexecdir}/cyr_systemd_helper
%else
%{__install} -d %{buildroot}%{_sysconfdir}/rc.d/init.d
%{__install} -p -m 755 %{SOURCE21}   %{buildroot}%{_sysconfdir}/rc.d/init.d/%{name}
%endif

# Cleanup of doc dir
find doc perl -name CVS -type d | xargs -r %{__rm} -rf
find doc perl -name .cvsignore -type f | xargs -r %{__rm} -f
%{__rm} -f doc/Makefile.dist*
%{__rm} -f doc/text/htmlstrip.c
%{__rm} -f doc/text/Makefile
%{__rm} -rf doc/man

# fix permissions on perl .so files
find %{buildroot}%{perl_vendorarch} -type f -name "*.so" -exec %{__chmod} 755 {} \;

# fix conflicts with uw-imap
mv %{buildroot}%{_mandir}/man8/imapd.8 %{buildroot}%{_mandir}/man8/imapd.8cyrus
mv %{buildroot}%{_mandir}/man8/pop3d.8 %{buildroot}%{_mandir}/man8/pop3d.8cyrus

# Install templates
%{__install} -m 755 -d doc/conf
%{__install} -m 644 master/conf/*.conf doc/conf/

# Generate db config file
( grep '^{' lib/imapoptions | grep _db | grep -v _db_path | cut -d'"' -f 2,4 | \
  sed -e 's/^ *//' -e 's/-nosync//' -e 's/ *$//' -e 's/"/=/'
  echo sieve_version=2.2.3 ) | sort > %{buildroot}%{_var}/lib/imap/rpm/db.cfg

# create the ghost pem file
touch %{buildroot}%{ssl_pem_file}

# Rename 'master' binary and manpage to avoid clash with postfix
%{__mv} -f %{buildroot}%{_cyrexecdir}/master        %{buildroot}%{_cyrexecdir}/cyrus-master
%{__mv} -f %{buildroot}%{_mandir}/man8/master.8     %{buildroot}%{_mandir}/man8/cyrus-master.8

# Rename 'httpd' binary and manpage to avoid clash with apache httpd
%if 0%{?with_dav}
%{__mv} -f %{buildroot}%{_cyrexecdir}/httpd         %{buildroot}%{_cyrexecdir}/cyrus-httpd
%{__mv} -f %{buildroot}%{_mandir}/man8/httpd.8      %{buildroot}%{_mandir}/man8/cyrus-httpd.8
%endif

# Rename 'fetchnews' binary and manpage to avoid clash with leafnode
%{__mv} -f %{buildroot}%{_cyrexecdir}/fetchnews     %{buildroot}%{_cyrexecdir}/cyrfetchnews
%{__mv} -f %{buildroot}%{_mandir}/man8/fetchnews.8  %{buildroot}%{_mandir}/man8/cyrfetchnews.8
%{__perl} -pi -e 's|fetchnews|cyrfetchnews|g;s|Fetchnews|Cyrfetchnews|g;s/FETCHNEWS/CYRFETCHNEWS/g' \
        %{buildroot}%{_mandir}/man8/cyrfetchnews.8

# compress manpages
[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

# remove executable bit from docs
for ddir in doc perl/imap/examples
do
  find $ddir -type f -exec %{__chmod} -x {} \;
done

# Remove installed but not packaged files
%{__rm} -f %{buildroot}%{_cyrexecdir}/not-mkdep
%{__rm} -f %{buildroot}%{_cyrexecdir}/config2header*
%{__rm} -f %{buildroot}%{_cyrexecdir}/config2man
%{__rm} -f %{buildroot}%{_cyrexecdir}/pop3proxyd
find %{buildroot} -type f -name "perllocal.pod" -exec %{__rm} -vf {} \;
find %{buildroot} -type f -name ".packlist" -exec %{__rm} -vf {} \;
find %{buildroot} -type f -name ".gitignore" -exec %{__rm} -vf {} \;
%{__rm} -f %{buildroot}%{_mandir}/man8/syncnews.8*
find %{buildroot}%{perl_vendorarch} -type f -name "*.bs" -exec %{__rm} -vf {} \;

%check
make check || :

%clean
%{__rm} -rf %{buildroot}

%pre
if [ $1 == 1 ]; then
    # Create 'cyrus' user on target host
    /usr/sbin/groupadd -g %{gid} -r saslauth 2> /dev/null || :
    /usr/sbin/useradd -c "Cyrus IMAP Server" -d %{_var}/lib/imap -g %{_cyrusgroup} \
        -G saslauth -s /sbin/nologin -u %{uid} -r %{_cyrususer} 2> /dev/null || :
fi

%post
%if 0%{?suse_version}
/sbin/ldconfig
%endif

CHATTRSYNC=0

%if 0%{?suse_version}
%if 0%{?with_systemd}
    %fillup_only %{name}
%else
    %fillup_and_insserv %{name}
%endif
if [[ ! -e "%{_sysconfdir}/pam.d/runuser" ]]; then
    ln -s %{_sysconfdir}/pam.d/su %{_sysconfdir}/pam.d/runuser
fi
if [[ ! -e "%{_sysconfdir}/pam.d/runuser-l" ]]; then
    ln -s %{_sysconfdir}/pam.d/su-l %{_sysconfdir}/pam.d/runuser-l
fi
%endif

if [ -f "%{_sysconfdir}/sysconfig/cyrus-imapd" ]; then
    source %{_sysconfdir}/sysconfig/cyrus-imapd
fi

if [ $CHATTRSYNC -eq 1 ]; then
    # Force synchronous updates of files in the following directories
    chattr -R +S \
        $(grep ^configdirectory: /etc/imapd.conf | cut -d':' -f2) \
        $(grep ^partition- /etc/imapd.conf | cut -d':' -f2) \
        $(grep ^metapartition- /etc/imapd.conf | cut -d':' -f2) 2>/dev/null ||:
fi

# Create SSL certificates
exec > /dev/null 2> /dev/null

if [ ! -z "%{ssl_pem_file}" -a -z "$(cat %{ssl_pem_file})" ]; then
    %{__rm} -f "%{ssl_pem_file}" || :
fi

if [ ! -f %{ssl_pem_file} -a -d "%{_sysconfdir}/pki/tls/certs" ]; then
    pushd %{_sysconfdir}/pki/tls/certs
    umask 077
    %{__cat} << EOF | make %{name}.pem
--
SomeState
SomeCity
SomeOrganization
SomeOrganizationalUnit
localhost.localdomain
root@localhost.localdomain
EOF

    %{__chown} root.%{_cyrusgroup} %{name}.pem
    %{__chmod} 640 %{name}.pem
    mv %{name}.pem %{ssl_pem_file}
    popd
fi

# These commands may fail in a docker container, which may not
# have a /usr/bin/systemctl with a 'preset' command
%if 0%{?with_systemd}
%if 0%{?suse_version}
    %service_add_post cyrus-imapd.service || :
%else
    %systemd_post cyrus-imapd.service || :
%endif
%else
    /sbin/chkconfig --add %{name}
%endif

%preun
%if 0%{?with_systemd}
%if 0%{?suse_version}
    %service_del_preun cyrus-imapd.service
%else
    %systemd_preun cyrus-imapd.service >/dev/null 2>&1 || :
%endif
%else
    if [ $1 = 0 ]; then
        /sbin/service %{name} stop >/dev/null 2>&1 || :
        /sbin/chkconfig --del %{name}
    fi
%endif

%postun
%if 0%{?suse_version}
/sbin/ldconfig
%endif

%if 0%{?with_systemd}
%if 0%{?suse_version}
    %service_del_postun cyrus-imapd.service
%else
    %systemd_postun_with_restart cyrus-imapd.service
%endif
%else
    if [ $1 != 0 ]; then
        /sbin/service %{name} condrestart >/dev/null 2>&1 || :
    fi
%endif

%files
%defattr(-,root,root,-)
%doc COPYING README
%doc doc/*
%config(noreplace) %{_sysconfdir}/cyrus.conf
%config(noreplace) %{_sysconfdir}/imapd.conf
%if 0%{?with_systemd}
%{_unitdir}/cyrus-imapd.service
%{_cyrexecdir}/cyr_systemd_helper
%else
%{_sysconfdir}/rc.d/init.d/%{name}
%endif
%dir %{_sysconfdir}/pki
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if 0%{?suse_version}
%config(noreplace) %{_localstatedir}/adm/fillup-templates/sysconfig.%{name}
%else
%attr(0640,root,%{_cyrusgroup}) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%endif
%config(noreplace) %{_sysconfdir}/pam.d/pop
%config(noreplace) %{_sysconfdir}/pam.d/imap
%config(noreplace) %{_sysconfdir}/pam.d/sieve
%config(noreplace) %{_sysconfdir}/pam.d/lmtp
%config(noreplace) %{_sysconfdir}/pam.d/mupdate
%config(noreplace) %{_sysconfdir}/pam.d/csync
%config(noreplace) %{_sysconfdir}/pam.d/nntp
%attr(0755,root,root) %{_bindir}/cyradm
%{_bindir}/imtest
%{_bindir}/installsieve
%{_bindir}/lmtptest
%{_bindir}/mupdatetest
%{_bindir}/nntptest
%{_bindir}/pop3test
%{_bindir}/sieveshell
%{_bindir}/sivtest
%{_bindir}/smtptest
%{_bindir}/synctest
%{_sysconfdir}/cron.daily/%{name}
%dir %{_cyrexecdir}
%{_cyrexecdir}/arbitron
%{_cyrexecdir}/arbitronsort.pl
%{_cyrexecdir}/chk_cyrus
%{_cyrexecdir}/compile_st.pl
%{_cyrexecdir}/convert-sieve.pl
%{_cyrexecdir}/cyr_deny
%{_cyrexecdir}/cyr_df
%{_cyrexecdir}/cyr_info
#%%{_cyrexecdir}/ctl_conversationsdb
%{_cyrexecdir}/ctl_cyrusdb
%{_cyrexecdir}/ctl_deliver
%{_cyrexecdir}/ctl_mboxlist
%{_cyrexecdir}/cvt_cyrusdb
%{_cyrexecdir}/cyr_buildinfo
%{_cyrexecdir}/cyr_dbtool
%{_cyrexecdir}/cyr_expire
%{_cyrexecdir}/cyr_sequence
%{_cyrexecdir}/cyr_synclog
%{_cyrexecdir}/cyr_userseen
%{_cyrexecdir}/cyrdump
%if 0%{?with_dav}
%{_cyrexecdir}/cyrus-httpd
%endif
%{_cyrexecdir}/cyrus-master
%{_cyrexecdir}/deliver
%{_cyrexecdir}/dohash
%{_cyrexecdir}/fixsearchpath.pl
%{_cyrexecdir}/fud
%exclude %{_cyrexecdir}/git-version.sh
#%%{_cyrexecdir}/hammer_cyrusdb
%{_cyrexecdir}/imapd
%{_cyrexecdir}/ipurge
%exclude %{_cyrexecdir}/jenkins-build.sh
%{_cyrexecdir}/lmtpd
%{_cyrexecdir}/lmtpproxyd
%{_cyrexecdir}/masssievec
%{_cyrexecdir}/mbexamine
%{_cyrexecdir}/mbpath
%{_cyrexecdir}/mbtool
#%%{_cyrexecdir}/message_test
%{_cyrexecdir}/migrate-metadata
%{_cyrexecdir}/mkimap
%{_cyrexecdir}/mknewsgroups
%{_cyrexecdir}/notifyd
%{_cyrexecdir}/pop3d
%{_cyrexecdir}/quota
%{_cyrexecdir}/reconstruct
%{_cyrexecdir}/rehash
#%%{_cyrexecdir}/search_test
%{_cyrexecdir}/sievec
%{_cyrexecdir}/sieved
%{_cyrexecdir}/smmapd
#%%{_cyrexecdir}/squat_dump
%{_cyrexecdir}/squatter
%{_cyrexecdir}/timsieved
%{_cyrexecdir}/tls_prune
%{_cyrexecdir}/translatesieve
%{_cyrexecdir}/undohash
%{_cyrexecdir}/unexpunge
%{_cyrexecdir}/upgradesieve
%{_cyrexecdir}/cvt_cyrusdb_all
%{_cyrexecdir}/idled
%{_cyrexecdir}/mupdate
%{_cyrexecdir}/mupdate-loadgen.pl
%{_cyrexecdir}/proxyd
%{_cyrexecdir}/sync_client
%{_cyrexecdir}/sync_reset
%{_cyrexecdir}/sync_server
%{_cyrexecdir}/cyrfetchnews
%{_cyrexecdir}/nntpd
%{_cyrexecdir}/ptdump
%{_cyrexecdir}/ptexpire
%{_cyrexecdir}/ptloader
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/backup
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/db
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/log
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/meta
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/md5
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/msg
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %{_var}/lib/imap/proc
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %{_var}/lib/imap/ptclient
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/quota
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/rpm
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/sieve
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %{_var}/lib/imap/socket
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/sync
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/lib/imap/user
%attr(0750,%{_cyrususer},%{_cyrusgroup}) %dir %{_var}/spool/imap
%{_libdir}/*.so.*
%{_var}/lib/imap/rpm/*
%doc perl/imap/README
%doc perl/imap/Changes
%doc perl/imap/examples
%dir %{perl_vendorarch}/Cyrus
%dir %{perl_vendorarch}/Cyrus/IMAP
%{perl_vendorarch}/Cyrus/IMAP/Admin.pm
%{perl_vendorarch}/Cyrus/IMAP/Shell.pm
%{perl_vendorarch}/Cyrus/IMAP/IMSP.pm
%{perl_vendorarch}/Cyrus/IMAP.pm
%dir %{perl_vendorarch}/Cyrus/SIEVE
%{perl_vendorarch}/Cyrus/SIEVE/managesieve.pm
%dir %{perl_vendorlib}/Cyrus/
%dir %{perl_vendorlib}/Cyrus/Annotator
%{perl_vendorlib}/Cyrus/Annotator/Daemon.pm
%{perl_vendorlib}/Cyrus/Annotator/Message.pm
%dir %{perl_vendorarch}/auto
%dir %{perl_vendorarch}/auto/Cyrus
%dir %{perl_vendorarch}/auto/Cyrus/IMAP
%{perl_vendorarch}/auto/Cyrus/IMAP/IMAP.so
%dir %{perl_vendorarch}/auto/Cyrus/SIEVE
%dir %{perl_vendorarch}/auto/Cyrus/SIEVE/managesieve
%{perl_vendorarch}/auto/Cyrus/SIEVE/managesieve/managesieve.so
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%dir %{_sysconfdir}/pki/%{name}
%attr(0640,root,%{_cyrusgroup}) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{ssl_pem_file}

%files devel
%defattr(0644,root,root,0755)
%{_includedir}/cyrus
%{_libdir}/pkgconfig/*cyrus*.pc
%{_libdir}/*.so
%{_libdir}/*.la

%changelog
* Wed Jan 29 2020 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.15.28-1
- Fix MessageExpunge event notification when executed from system

* Tue Oct 29 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.5.13.40-1
- Include the user or group ID in failed login attempts

* Wed Oct 23 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.5.13.36-1
- Rebase on to upstream -2.5 series
- Fix ptloader group membership (Bifrost T250286)

* Mon Aug 19 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.5.12.30-1
- Rebase on to upstream 2.5.13

* Tue Mar 12 2019 Timotheus Pokorra <tp@tbits.net> - 2.5.12.25-2
- Backport patch from upstream for canonification for multiple domains

* Wed Jan  2 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.5.12.25-1
- Rebase on to upstream 2.5.12

* Tue Oct 17 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.11-4
- Fix potentially non-readable, non-writeable /dev/null

* Tue Dec 13 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.10-55-gb6dbffa
- Fix proxying extended list usage to backends with answers.

* Mon Nov 14 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.10-49-g2e214b4
- Decode the subject line before re-encoding it in automated responses.

* Sat Nov  5 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.10-43-g1148d47
- Preserve the folder uniqueid on rename.
- Transfer a folder between backends preserving the mailboxes.db uniqueid.
- Allow replicated backends to transfer mailboxes between pairs.
- Preserve the original partition as the target partition if not the default
  partition, when replicating or transferring a mailbox.

* Fri Sep 30 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.9.31-1
- Check in 31 revisions ahead of upstream 2.5.9 release

* Thu Sep 22 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.9.27-1
- Check in 27 revisions ahead of upstream 2.5.9 release

* Mon Aug 01 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.9.11-1
- Check in 11 revisions ahead of upstream 2.5.9 release

* Thu Jul  7 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.8.22-1
- Check in 22 revisions ahead of upstream 2.5.8 release

* Thu Jun 02 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.8.12-1
- Check in 12 revisions ahead of upstream 2.5.8 release

* Mon May 09 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.7.26-1
- Check in 26 revisions ahead of upstream 2.5.7 release

* Fri Apr 29 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.7.25-1
- Check in 25 revisions ahead of upstream 2.5.7 release

* Mon Mar 21 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.7.10-1
- Check in 10 revisions ahead of upstream 2.5.7 release

* Thu Mar 10 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.7.8-1
- Check in 8 revisions ahead of upstream 2.5.7 release

* Wed Dec 16 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.7-1
- Upstream release 2.5.7

* Fri Sep 25 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.6.7-1
- Check in 7 revisions ahead of upstream 2.5.6 release

* Sun Sep 20 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.6.3-1
- New upstream release 2.5.6, plus 3 additional revisions

* Fri Aug 14 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.5.5-1
- New upstream release 2.5.5, plus 5 additional revisions

* Wed May 13 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.2.3-1
- Check in 2 revisions ahead of new upstream release 2.5.2

* Tue May 12 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.2.1-1
- Check in 1 revision ahead of new upstream release 2.5.2

* Tue Apr 28 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.1-19.1
- Check in 19 revisions ahead of new upstream release 2.5.1

* Mon Apr 27 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.1-5.1
- Check in 5 revisions ahead of new upstream release 2.5.1

* Sat Apr 11 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.0-65.1
- Check in 65 revisions ahead of new upstream release 2.5.0

* Fri Mar 20 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.0-45.1
- Check in 45 revisions ahead of new upstream release 2.5.0

* Tue Mar 10 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5.0-30.1
- Check in 30 revisions ahead of new upstream release 2.5.0

* Fri Feb 13 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5-12.git
- New snapshot

* Tue Dec  9 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5-11.git
- Fix Murder topologies not handling null ACLs at all

* Thu Sep 25 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5-10.git
- Fix event notifications

* Fri Aug 29 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5-9.git
- Snapshot of (b2ef80be)
- Merge enhanced Sieve Date and Index extension

* Mon Mar  3 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.5-8.git
- Fix shared folder deleted namespace prefix

* Tue Mar 12 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.17-2
- Refresh patch for normalization of the UID - actually enable disabling it

* Sat Dec  1 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.17-1
- New upstream version

* Wed Nov 21 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.15-2
- Ship fix for APPEND BINARY GUID (#3754)

