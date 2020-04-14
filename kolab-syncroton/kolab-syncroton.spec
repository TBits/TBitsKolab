# Needed for opensuse build system
%if 0%{?opensuse_bs}
#!BuildIgnore:  boa
#!BuildIgnore:  cherokee
#!BuildIgnore:  nginx
#!BuildIgnore:  httpd-itk
#!BuildIgnore:  lighttpd
#!BuildIgnore:  thttpd

#!BuildIgnore:  fedora-logos-httpd

#!BuildIgnore:  php-mysqlnd

#!BuildIgnore:  roundcubemail-skin-classic
#!BuildIgnore:  roundcubemail-plugin-jqueryui-skin-classic
%endif

%{!?php_inidir: %global php_inidir %{_sysconfdir}/php.d}

%if 0%{?suse_version}
%global httpd_group www
%global httpd_name apache2
%global httpd_user wwwrun
%else
%if 0%{?plesk}
%global httpd_group roundcube_sysgroup
%global httpd_name httpd
%global httpd_user roundcube_sysuser
%else
%global httpd_group apache
%global httpd_name httpd
%global httpd_user apache
%endif
%endif

%global _ap_sysconfdir %{_sysconfdir}/%{httpd_name}

Name:           kolab-syncroton
Version:        2.3.16
Release:        3.12%{?dist}.kolab_16
Summary:        ActiveSync for Kolab Groupware

Group:          Applications/Internet
License:        LGPLv2
URL:            http://www.syncroton.org

Source0:        https://mirror.kolabenterprise.com/pub/releases/%{name}-%{version}.tar.gz
Source1:        kolab-syncroton.logrotate
Source2:        plesk.kolab_syncroton.inc.php

BuildArch:      noarch

# Use this build requirement to make sure we are using
# up to date vendorized copies of the plugins.
%if 0%{?plesk} < 1
BuildRequires:  roundcubemail-plugin-kolab_auth >= 3.2
%endif
BuildRequires:  roundcubemail-plugin-kolab_folders >= 3.2
BuildRequires:  roundcubemail-plugin-libcalendaring >= 3.2
BuildRequires:  roundcubemail-plugin-libkolab >= 3.2

%if 0%{?suse_version}
BuildRequires:  roundcubemail
Requires:       php
Requires:       php-pear-Auth_SASL
Requires:       php-pear-MDB2_Driver_mysqli
Requires:       php-pear-Net_IDNA2
Requires:       php-pear-Net_SMTP
Requires:       php-pear-Net_Socket
%else
Requires:       php-common >= 5.3
Requires:       php-pear-Auth-SASL
Requires:       php-pear-MDB2-Driver-mysqli
Requires:       php-pear-Net-IDNA2
Requires:       php-pear-Net-SMTP
Requires:       php-pear-Net-Socket
%endif

Requires:       logrotate
Requires:       roundcubemail(core)
%if 0%{?plesk} < 1
Requires:       roundcubemail-plugin-kolab_auth >= 3.2
%endif
Requires:       roundcubemail-plugin-kolab_folders >= 3.2
Requires:       roundcubemail-plugin-libcalendaring >= 3.2
Requires:       roundcubemail-plugin-libkolab >= 3.2
Requires:       php-kolabformat
Requires:       php-pear-MDB2
Requires:       php-ZendFramework

%description
Kolab Groupware provides ActiveSync for Calendars, Address Books
and Tasks though this package - based on Syncroton technology.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p \
    %{buildroot}/%{_datadir}/%{name} \
%if 0%{?plesk} < 1
    %{buildroot}/%{_ap_sysconfdir}/conf.d/ \
%endif
    %{buildroot}/%{_sysconfdir}/roundcubemail/ \
    %{buildroot}/%{_var}/log/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
cp -pr %SOURCE1 %{buildroot}%{_sysconfdir}/logrotate.d/kolab-syncroton

sed -i \
    -e 's/apache apache/%{httpd_user} %{httpd_group}/g' \
    %{buildroot}%{_sysconfdir}/logrotate.d/kolab-syncroton

cp -a lib %{buildroot}/%{_datadir}/%{name}/.
cp -a index.php %{buildroot}/%{_datadir}/%{name}/.

%if 0%{?plesk}
cp -a %SOURCE2 %{buildroot}/%{_sysconfdir}/roundcubemail/kolab_syncroton.inc.php
%else
cp -a config/config.inc.php.dist %{buildroot}/%{_sysconfdir}/roundcubemail/kolab_syncroton.inc.php
%endif

pushd %{buildroot}/%{_datadir}/%{name}
ln -s ../../..%{_sysconfdir}/roundcubemail config
ln -s ../../..%{_var}/log/%{name} logs
pushd lib/ext
ln -s ../../../roundcubemail/program/lib/Roundcube
popd
pushd lib
ln -s ../../roundcubemail/plugins plugins
popd
ln -s ../roundcubemail/vendor vendor
popd

%if 0%{?plesk} < 1
cp -a docs/kolab-syncroton.conf %{buildroot}/%{_ap_sysconfdir}/conf.d/
%endif

find %{buildroot}/%{_datadir}/%{name}/ -type f -name "*.orig" -delete

# Fix anything executable that does not have a shebang
for file in `find %{buildroot}/%{_datadir}/%{name}/ -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done

# Find files with a shebang that do not have executable permissions
for file in `find %{buildroot}/%{_datadir}/%{name}/ -type f ! -perm /a+x`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done

# Find files that have non-standard-executable-perm
find %{buildroot}/%{_datadir}/%{name}/ -type f -perm /g+wx -exec chmod -v g-w {} \;

# Find files that are not readable
find %{buildroot}/%{_datadir}/%{name}/ -type f ! -perm /go+r -exec chmod -v go+r {} \;

%pre
if [ -d "/usr/share/kolab-syncroton/lib/ext/Roundcube" -a ! -L "/usr/share/kolab-syncroton/lib/ext/Roundcube" ]; then
    rm -rf "/usr/share/kolab-syncroton/lib/ext/Roundcube"
fi

%pretrans
if [ -d "/usr/share/kolab-syncroton/lib/plugins" -a ! -L "/usr/share/kolab-syncroton/lib/plugins" ]; then
    find /usr/share/kolab-syncroton/lib/plugins/ \
        -type l -exec rm -f {} \;
    rm -rf /usr/share/kolab-syncroton/lib/plugins/
    pushd /usr/share/kolab-syncroton/lib/
    ln -s ../../roundcubemail/plugins
fi

%post
if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
    if [ ! -z "`grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null`" ]; then
%if 0%{?fedora} > 15
        /bin/systemctl condrestart %{httpd_name}.service
%else
        /sbin/service %{httpd_name} condrestart
%endif
    fi
fi

/usr/share/roundcubemail/bin/updatedb.sh \
    --dir /usr/share/doc/kolab-syncroton-%{version}/SQL/ \
    --package syncroton \
    >/dev/null 2>&1 || :

exit 0

%files
%doc docs/*
%if 0%{?suse_version}
%dir %{_ap_sysconfdir}/
%dir %{_ap_sysconfdir}/conf.d/
%endif
%if 0%{?plesk} < 1
%config(noreplace) %{_ap_sysconfdir}/conf.d/kolab-syncroton.conf
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/roundcubemail/kolab_syncroton.inc.php
%{_datadir}/%{name}
%attr(0770,%{httpd_user},%{httpd_group}) %{_var}/log/%{name}

%changelog
* Wed Dec  4 2019 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.3.16-1
- Release version 2.3.16

* Mon Jul 29 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.15-3
- Fix MeetingResponse for Calendar events

* Thu Apr 11 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.15-2
- Update defaults

* Fri Feb  1 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.15-1
- Release 2.3.15

* Thu Dec 27 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.14-1
- Release 2.3.14

* Fri Aug 17 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.13-1
- Release 2.3.13

* Wed Jun 13 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.12-1
- Release 2.3.12

* Thu Mar  8 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.10-1
- Release 2.3.10

* Fri Mar  2 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.9-1
- Release 2.3.9

* Fri Feb  2 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.8-3
- Fix redundant GETMETADATA requests for mail folders

* Wed Jan 24 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.8-2
- Fix logging
- Fix version number

* Wed Dec 20 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.8-1
- Release 2.3.8

* Sun Aug 27 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.7-1
- Release 2.3.7

* Fri Aug 18 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.6-2
- Patch setAttendeeStatus for increased Outlook compatibility

* Wed Jul 19 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.6-1
- Release 2.3.6

* Sun Jun 18 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.5-2
- Implement a GAL virtual folder with LDAP backend for Outlook over Activesync
- Fix organizer / ownership for events

* Thu Jun  8 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.5-1
- Release 2.3.5

* Wed May 10 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.4-3
- Fix log rotation on Plesk

* Fri Feb 24 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.4-2
- Only call kolab_auth::ldap_close() if the method actually exists

* Wed Jan 25 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.4-1
- Release of version 2.3.4

* Tue Nov 15 2016 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.3-1
- Release of version 2.3.3

* Fri Mar 27 2015 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.2-1
- Release of version 2.3.2, see;

  https://issues.kolab.org/buglist.cgi?target_milestone=2.3.2&product=Syncroton

* Thu Feb  5 2015 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.1-1
- Release of version 2.3.1, see;

  https://issues.kolab.org/buglist.cgi?target_milestone=2.3.1&product=Syncroton

* Tue Jan 27 2015 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.3.0-1
- Release of version 2.3.0, see;

  https://issues.kolab.org/buglist.cgi?target_milestone=2.3.0&product=Syncroton

* Mon Sep 15 2014 Daniel Hoffend <dh@dotlan.net> - 2.3-0.2.git
- New upstream version

* Tue Apr  8 2014 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.2.5-2
- Include fix for From: header off iOS devices

* Sun Apr  6 2014 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.2.5-1
- New upstream version
- #2664 - Fix for devices that do not support empty Sync responses
- Fix synchronization of task importance
- #2845 - Fix invalid email message identifier in Move response
- Fix issues in recode_message() - wrong boundaries handling

* Tue Feb 11 2014 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.2.4-5
- Rebuild against up-to-date roundcubemail-plugins-kolab
- Fix memory consumption issues on very large result sets (#2828)

* Thu Feb  6 2014 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.2.4-4
- Fix recode_message() boundary handling
- Refresh Junk folder patch

* Wed Jan 29 2014 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.2.4-2
- Fix From: header on iPad/iPhone activesync clients not having a
  displayName. Set 'activesync_fix_from'
- Fix Junk folders being omitted for synchronization

* Tue Jan 28 2014 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 2.2.4-1
- New upstream release

* Tue Nov 12 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.2.3-2
- Fix a trailing slash issue
- New upstream release
- Fixes:
  2385 - Do not depend on kolab_cache behavior
  2386 - Improve performance by skipping IMAP SEARCH when checking
         mail folder for changes
  ???? - Skip SELECT/DELETE ... WHERE id = NULL queries
  2383 - Enable alarms synchronization by default
  2431 - Fix event attendees synchronization from server to the device

* Mon Nov 11 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.2.2-3
- Make sure we use the readily available plugins and libraries

* Fri Oct 18 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.2.2-1
- New upstream version in sync with cache refactoring

* Mon Oct 14 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.2.1-1
- New upstream version 2.2.1

* Sun Sep  8 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.2.0-1
- Release version 2.2.0

* Tue Mar 12 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.1-0.2.rc2
- New upstream release

* Tue Feb 12 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.1-0.1.rc1
- Check in new release 2.1-rc1

* Sun Dec  9 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.0.0-0.2
- Pull in the required configuration

* Tue Nov 27 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.0.0-0.1
- New snapshot that fixes SMTP Auth (#1380)

* Thu Sep 27 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.1-2
- Apply fix for authentication failing

* Fri Sep 21 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0.1-1
- New upstream release

* Wed Sep 19 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.1
- On the road to version 1.0, distribute a snapshot

* Wed Aug  1 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-0.2
- New git master snapshot

* Wed Jul 25 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-0.1
- This is a package, too
