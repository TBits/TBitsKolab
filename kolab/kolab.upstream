%if 0%{?opensuse_bs}
#!BuildIgnore   httpd
%endif

%if 0%{?suse_version} < 1 && 0%{?fedora} < 1 && 0%{?rhel} < 7
%global with_systemd 0
%else
%global with_systemd 1
%endif

%global debug_package %{nil}

Name:           kolab
Version:        16.0.1
Release:        6%{?dist}
Summary:        The Kolab Groupware Solution

Group:          Applications/System
License:        GPL
URL:            http://www.kolab.org
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Other meta-packages
Requires:       kolab-conf
Requires:       kolab-imap
Requires:       kolab-ldap
Requires:       kolab-mta
Requires:       kolab-webadmin
Requires:       kolab-webclient

Requires:       kolab-cli
Requires:       kolab-saslauthd
Requires:       kolab-server
%if 0%{?suse_version}
Requires:       mysql
%else
%if 0%{?rhel} > 6
Requires:       mariadb-server
%else
Requires:       mysql-server
%endif
%endif

%description
The Kolab Groupware solution is a fully-featured Free Software groupware solution,
and this is the meta-package you can use to install it with.

%package conf
Summary:        Kolab Groupware IMAP Component
Group:          Applications/System
Requires:       kolab-cli
Requires:       pykolab

%description conf
This is the Kolab Groupware Configuration component meta-package

%package imap
Summary:        Kolab Groupware IMAP Component
Group:          Applications/System
Requires:       cyrus-imapd
%if %{?_arch} == "ppc64le" && 0%{?fedora}
# Do not require Guam on fedora/ppc64le
%else
Requires:       guam
%endif
Requires:       kolab-saslauthd
Requires:       pykolab

%description imap
This is the Kolab Groupware IMAP component meta-package

%package ldap
Summary:        Kolab Groupware LDAP component meta-package
Group:          Applications/System
%if 0%{?rhel} > 6
Requires:       389-ds-base
%else
Requires:       389-ds
%endif
Requires:       kolab-schema
# Install or setup-kolab will fail
Requires:       python-sqlalchemy

%description ldap
This is the meta-package for the default Kolab Groupware LDAP
component

%if 0%{?plesk}
%package plesk
Summary:        Kolab Groupware for Plesk %{plesk}
Group:          Applications/System
Requires:       chwala
Requires:       guam
Requires:       iRony
Requires:       kolab-syncroton
Requires:       php-kolabformat >= 1.0
Requires:       php-kolab >= 0.5
Requires:       php-pear(Auth_SASL)
Requires:       php-pear(HTTP_Request2)
Requires:       php-pear(Mail_Mime) >= 1.8.5
Requires:       roundcubemail-core
Requires:       roundcubemail-plugin-acl
Requires:       roundcubemail-plugin-archive
Requires:       roundcubemail-plugin-calendar
Requires:       roundcubemail-plugin-contextmenu
Requires:       roundcubemail-plugin-jqueryui
Requires:       roundcubemail-plugin-kolab_activesync
Requires:       roundcubemail-plugin-kolab_addressbook
Requires:       roundcubemail-plugin-kolab_config
Requires:       roundcubemail-plugin-kolab_files
Requires:       roundcubemail-plugin-kolab_folders
Requires:       roundcubemail-plugin-kolab_notes
Requires:       roundcubemail-plugin-kolab_tags
Requires:       roundcubemail-plugin-managesieve
Requires:       roundcubemail-plugin-markasjunk
Requires:       roundcubemail-plugin-newmail_notifier
Requires:       roundcubemail-plugin-odfviewer
Requires:       roundcubemail-plugin-password
Requires:       roundcubemail-plugin-pdfviewer
Requires:       roundcubemail-plugin-tasklist
Requires:       roundcubemail-plugin-zipdownload
Requires:       roundcubemail-skin-plesk

%description plesk
This is the meta-package to install Kolab Groupware on Plesk %{plesk}
%endif

%package mta
Summary:        The Kolab Groupware Mail Transfer Agent (MTA) meta-package
Group:          Applications/System
Requires:       amavisd-new

%if 0%{?rhel} > 6 || 0%{?fedora} > 0
Requires:       clamav-update
%endif

%if 0%{?with_systemd}
Requires:       clamav-server-systemd
%else
Requires:       clamav-server-sysvinit
%endif
Requires:       clamav-update

Requires:       postfix
Requires:       postfix-kolab
%if 0%{?fedora} >= 23
Requires:       postfix-ldap
%endif
Requires:       spamassassin
Requires:       wallace
Obsoletes:      sendmail
Obsoletes:      sendmail-cf

%description mta
This is the Kolab Groupware Mail Transfer Agent (MTA) meta-package

%package webclient
Summary:        Kolab Groupware Server Web Mail Interface
Group:          Productivity/Office/Organizers
Requires:       chwala
Requires:       iRony
Requires:       kolab-autoconf
Requires:       kolab-freebusy
Requires:       kolab-syncroton
# Install or /usr/bin/mysql isn't available
Requires:       mysql

%if 0%{?rhel} > 6
# Require httpd or lighttpd gets installed
Requires:       httpd
# Require php or the installation is incomplete
Requires:       php
%endif

Requires:       roundcubemail
Requires:       roundcubemail(plugin-archive)
Requires:       roundcubemail(plugin-markasjunk)
Requires:       roundcubemail(plugin-newmail_notifier)
Requires:       roundcubemail(plugin-redundant_attachments)

Requires:       roundcubemail-plugin-contextmenu
Requires:       roundcubemail-plugins-kolab

%description webclient
This is the Kolab Groupware web client meta-package

%prep
%setup -q

%build

%install

%clean

%files
%defattr(-,root,root,-)
%doc README

%files conf
%defattr(-,root,root,-)
%doc README

%files imap
%defattr(-,root,root,-)
%doc README

%files ldap
%defattr(-,root,root,-)
%doc README

%files mta
%defattr(-,root,root,-)
%doc README

%if 0%{?plesk}
%files plesk
%defattr(-,root,root,-)
%doc README
%endif

%files webclient
%defattr(-,root,root,-)
%doc README

%changelog
* Mon May 07 2018 Christoph Erhardt <kolab@sicherha.de> - 16.0.1-6
- Fix logical expression

* Tue Sep 05 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 16.0.1-5
- Exclude requiring guam on fedora/ppc64le

* Wed Jan 11 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 16.0.1-4
- Initial changes for Plesk 17 installation

* Thu Mar 10 2016 Timotheus Pokorra <tp@tbits.net> - 16.0.1-2
- Fedora 23 requires postfix-ldap to be installed

* Sun Jan 31 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 16.0.1-1
- Set the build architecture back to not noarch

* Fri Jan 15 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 16.0.0-1
- Release Kolab 16

* Sun Jul 13 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.8-1
- Fix logo location and introduce the use of asset paths

* Fri May 02 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.4-1
- Refresh configuration for kolab-mta on UCS
- Add default plugin dependencies for kolab-webclient

* Sun Sep  8 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.0-1
- Also depend on chwala and iRony

* Fri Aug  3 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.0-1
- Add dependency on kolab-utils for Kolab 3.0 alpha

* Tue May  1 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0-2
- Add requirement for mysql-server
- Check in version 3.0

* Thu Apr 12 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4-3
- Add dependencies on kolab-cli, kolab-saslauthd and kolab-server

* Tue Jul 12 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4-2
- Fix version in changelog
- BuildArch is noarch
- Introduce the kolab meta-package
