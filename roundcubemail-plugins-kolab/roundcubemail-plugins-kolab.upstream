%{!?php_inidir: %global php_inidir %{_sysconfdir}/php.d}

%if 0%{?suse_version} < 1 && 0%{?fedora} < 1 && 0%{?rhel} < 7
%global with_systemd 0
%else
%global with_systemd 1
%endif

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

%global roundcube_version 1.2
%global datadir %{_datadir}/roundcubemail
%global plugindir %{datadir}/plugins
%global confdir %{_sysconfdir}/roundcubemail
%global tmpdir %{_var}/lib/roundcubemail

Name:           roundcubemail-plugins-kolab
Version:        3.3.6
Release:        1%{?dist}
Summary:        Kolab Groupware plugins for Roundcube Webmail

Group:          Applications/Internet
License:        AGPLv3+ and GPLv3+
URL:            http://www.kolab.org

# From 562ed98bd2e265c0d8a12bd2092b72d85d3e3543
Source0:        https://mirror.kolabenterprise.com/pub/releases/roundcubemail-plugins-kolab-%{version}.tar.gz
Source1:        comm.py

Source100:      plesk.calendar.inc.php
Source101:      plesk.kolab_addressbook.inc.php
Source102:      plesk.kolab_folders.inc.php
Source103:      plesk.libkolab.inc.php

Patch0001:      0001-Fix-missing-first-occurrence-of-an-event-when-moved-.patch

Patch1001:      roundcubemail-plugins-kolab-3.3-kolab-files-manticore-api.patch

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

BuildRequires:  composer
%if 0%{?fedora}
# fix issue:
# have choice for php-composer(justinrainbow/json-schema) >= 2.0 needed by composer: php-justinrainbow-json-schema4 php-justinrainbow-json-schema
# have choice for php-composer(justinrainbow/json-schema) < 5 needed by composer: php-justinrainbow-json-schema4 php-justinrainbow-json-schema php-JsonSchema
BuildRequires:  php-justinrainbow-json-schema4
%endif

%if "%{_arch}" != "ppc64" && "%{_arch}" != "ppc64le" && 0%{?suse_version} < 1
BuildRequires:  python-cssmin
BuildRequires:  uglify-js
%else
BuildRequires:  roundcubemail(core)
%endif

BuildRequires:  python

Requires:       php-kolabformat >= 1.0
Requires:       php-kolab >= 0.5
Requires:       php-pear(HTTP_Request2)
%if 0%{?plesk} < 1
Requires:       php-pear(Net_LDAP3)
%endif
Requires:       php-pear(Mail_Mime) >= 1.8.5
Requires:       roundcubemail >= %{roundcube_version}
Requires:       roundcubemail(plugin-calendar) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_activesync) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_addressbook) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_auth) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_config) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_delegation) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_files) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_folders) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_notes) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_tags) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-odfviewer) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-pdfviewer) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-tasklist) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      roundcubemail-kolab < %{version}-%{release}
Provides:       roundcubemail-kolab = %{version}-%{release}

%description
A collection of Kolab Groupware plugins for Roundcube Webmail

%package -n roundcubemail-plugin-calendar
Summary:        Plugin calendar
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-calendar-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?fedora} >= 25
# avoid that plugin-calendar-skin-classic is installed, which is not what we want. that would return an error when loading the calendar
Requires:       roundcubemail(plugin-calendar-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       roundcubemail(plugin-calendar-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
Requires:       roundcubemail(plugin-libcalendaring) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-calendar) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-calendar
Plugin calendar

%package -n roundcubemail-plugin-html_converter
Summary:        Plugin html_converter
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-html_converter-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-html_converter-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       lynx
Provides:       roundcubemail(plugin-html_converter) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-html_converter
Plugin html_converter

%package -n roundcubemail-plugin-kolab_2fa
Summary:        Plugin kolab_2fa
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_2fa-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_2fa-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       php-endroid-qrcode
Requires:       php-enygma-yubikey
Requires:       php-spomky-labs-otphp
Provides:       roundcubemail(plugin-kolab_2fa) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_2fa
Plugin kolab_2fa

%package -n roundcubemail-plugin-kolab_activesync
Summary:        Plugin kolab_activesync
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_activesync-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_activesync-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-jqueryui) >= %{roundcube_version}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_activesync) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_activesync
Plugin kolab_activesync

%package -n roundcubemail-plugin-kolab_addressbook
Summary:        Plugin kolab_addressbook
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_addressbook-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_addressbook-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_addressbook) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_addressbook
Plugin kolab_addressbook

%package -n roundcubemail-plugin-kolab_auth
Summary:        Plugin kolab_auth
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_auth-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_auth) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_auth
Plugin kolab_auth

%package -n roundcubemail-plugin-kolab_config
Summary:        Plugin kolab_config
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_config-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_config) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_config
Plugin kolab_config

%package -n roundcubemail-plugin-kolab_delegation
Summary:        Plugin kolab_delegation
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_delegation-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_delegation-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_auth) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_delegation) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_delegation
Plugin kolab_delegation

%package -n roundcubemail-plugin-kolab_files
Summary:        Plugin kolab_files
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_files-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_files-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       php-curl
Provides:       roundcubemail(plugin-kolab_files) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_files
Plugin kolab_files

%package -n roundcubemail-plugin-kolab_folders
Summary:        Plugin kolab_folders
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_folders-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_folders) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_folders
Plugin kolab_folders

%package -n roundcubemail-plugin-kolab_notes
Summary:        Plugin kolab_notes
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_notes-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_notes-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-acl) >= %{roundcube_version}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_notes) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_notes
Plugin kolab_notes

%package -n roundcubemail-plugin-kolab_shortcuts
Summary:        Plugin kolab_shortcuts
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_shortcuts-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_shortcuts) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_shortcuts
Plugin kolab_shortcuts

%package -n roundcubemail-plugin-kolab_tags
Summary:        Plugin kolab_tags
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_tags-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-kolab_tags-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_tags) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_tags
Plugin kolab_tags

%package -n roundcubemail-plugin-ldap_authentication
Summary:        Plugin ldap_authentication
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-ldap_authentication-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-ldap_authentication) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-ldap_authentication
Plugin ldap_authentication

%package -n roundcubemail-plugin-libcalendaring
Summary:        Plugin libcalendaring
Group:          Applications/Internet
Requires:       php-sabre-vobject
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-libcalendaring-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libcalendaring-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-libcalendaring) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-libcalendaring
Plugin libcalendaring

%package -n roundcubemail-plugin-libkolab
Summary:        Plugin libkolab
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-libkolab-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-libkolab
Plugin libkolab

%package -n roundcubemail-plugin-loginfail
Summary:        Plugin loginfail
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-loginfail-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-loginfail) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-loginfail
Plugin loginfail

%package -n roundcubemail-plugin-logon_page
Summary:        Plugin logon_page
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-logon_page-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-logon_page) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-logon_page
Plugin logon_page

%package -n roundcubemail-plugin-odfviewer
Summary:        Plugin odfviewer
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-odfviewer-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-odfviewer) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-odfviewer
Plugin odfviewer

%package -n roundcubemail-plugin-pdfviewer
Summary:        Plugin pdfviewer
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-pdfviewer-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-pdfviewer) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-pdfviewer
Plugin pdfviewer

%package -n roundcubemail-plugin-piwik_analytics
Summary:        Plugin piwik_analytics
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-piwik_analytics-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-piwik_analytics) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-piwik_analytics
Plugin piwik_analytics

%package -n roundcubemail-plugin-tasklist
Summary:        Plugin tasklist
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-tasklist-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-tasklist-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-acl) >= %{roundcube_version}
Requires:       roundcubemail(plugin-jqueryui) >= %{roundcube_version}
Requires:       roundcubemail(plugin-libcalendaring) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-tasklist) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-tasklist
Plugin tasklist

%package -n roundcubemail-plugin-tinymce_config
Summary:        Plugin tinymce_config
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-tinymce_config-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-tinymce_config) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-tinymce_config
Plugin tinymce_config

%package -n roundcubemail-plugin-wap_client
Summary:        Plugin wap_client
Group:          Applications/Internet
Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-wap_client-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-wap_client) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-wap_client
Plugin wap_client

%package -n roundcubemail-plugin-calendar-assets
Summary:        Plugin calendar Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-calendar-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-calendar-assets
Plugin calendar Assets

%package -n roundcubemail-plugin-kolab_2fa-assets
Summary:        Plugin kolab_2fa Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_2fa-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_2fa-assets
Plugin kolab_2fa Assets

%package -n roundcubemail-plugin-kolab_activesync-assets
Summary:        Plugin kolab_activesync Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_activesync-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_activesync-assets
Plugin kolab_activesync Assets

%package -n roundcubemail-plugin-kolab_addressbook-assets
Summary:        Plugin kolab_addressbook Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_addressbook-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_addressbook-assets
Plugin kolab_addressbook Assets

%package -n roundcubemail-plugin-kolab_auth-assets
Summary:        Plugin kolab_auth Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_auth-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_auth-assets
Plugin kolab_auth Assets

%package -n roundcubemail-plugin-kolab_config-assets
Summary:        Plugin kolab_config Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_config-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_config-assets
Plugin kolab_config Assets

%package -n roundcubemail-plugin-kolab_delegation-assets
Summary:        Plugin kolab_delegation Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_delegation-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_delegation-assets
Plugin kolab_delegation Assets

%package -n roundcubemail-plugin-kolab_files-assets
Summary:        Plugin kolab_files Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_files-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_files-assets
Plugin kolab_files Assets

%package -n roundcubemail-plugin-kolab_folders-assets
Summary:        Plugin kolab_folders Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_folders-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_folders-assets
Plugin kolab_folders Assets

%package -n roundcubemail-plugin-kolab_notes-assets
Summary:        Plugin kolab_notes Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_notes-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_notes-assets
Plugin kolab_notes Assets

%package -n roundcubemail-plugin-kolab_shortcuts-assets
Summary:        Plugin kolab_shortcuts Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_shortcuts-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_shortcuts-assets
Plugin kolab_shortcuts Assets

%package -n roundcubemail-plugin-kolab_tags-assets
Summary:        Plugin kolab_tags Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_tags-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_tags-assets
Plugin kolab_tags Assets

%package -n roundcubemail-plugin-ldap_authentication-assets
Summary:        Plugin ldap_authentication Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-ldap_authentication-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-ldap_authentication-assets
Plugin ldap_authentication Assets

%package -n roundcubemail-plugin-libcalendaring-assets
Summary:        Plugin libcalendaring Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-libcalendaring-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-libcalendaring-assets
Plugin libcalendaring Assets

%package -n roundcubemail-plugin-libkolab-assets
Summary:        Plugin libkolab Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-libkolab-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-libkolab-assets
Plugin libkolab Assets

%package -n roundcubemail-plugin-loginfail-assets
Summary:        Plugin loginfail Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-loginfail-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-loginfail-assets
Plugin loginfail Assets

%package -n roundcubemail-plugin-logon_page-assets
Summary:        Plugin logon_page Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-logon_page-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-logon_page-assets
Plugin logon_page Assets

%package -n roundcubemail-plugin-odfviewer-assets
Summary:        Plugin odfviewer Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-odfviewer-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-odfviewer-assets
Plugin odfviewer Assets

%package -n roundcubemail-plugin-pdfviewer-assets
Summary:        Plugin pdfviewer Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-pdfviewer-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-pdfviewer-assets
Plugin pdfviewer Assets

%package -n roundcubemail-plugin-piwik_analytics-assets
Summary:        Plugin piwik_analytics Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-piwik_analytics-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-piwik_analytics-assets
Plugin piwik_analytics Assets

%package -n roundcubemail-plugin-tasklist-assets
Summary:        Plugin tasklist Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-tasklist-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-tasklist-assets
Plugin tasklist Assets

%package -n roundcubemail-plugin-tinymce_config-assets
Summary:        Plugin tinymce_config Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-tinymce_config-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-tinymce_config-assets
Plugin tinymce_config Assets

%package -n roundcubemail-plugin-wap_client-assets
Summary:        Plugin wap_client Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-wap_client-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-wap_client-assets
Plugin wap_client Assets

%package -n roundcubemail-plugin-calendar-skin-larry
Summary:        Plugin calendar / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-calendar) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-calendar-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-calendar-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-calendar-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-calendar-skin-larry
Plugin calendar / Skin larry

%package -n roundcubemail-plugin-calendar-skin-classic
Summary:        Plugin calendar / Skin classic
Group:          Applications/Internet
Requires:       roundcubemail(plugin-calendar) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-classic) >= %{roundcube_version}
Requires:       roundcubemail(plugin-calendar-skin-classic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-calendar-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-calendar-skin-classic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-calendar-skin-classic
Plugin calendar / Skin classic

%package -n roundcubemail-plugin-kolab_2fa-skin-larry
Summary:        Plugin kolab_2fa / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_2fa) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_2fa-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_2fa-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_2fa-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_2fa-skin-larry
Plugin kolab_2fa / Skin larry

%package -n roundcubemail-plugin-kolab_activesync-skin-larry
Summary:        Plugin kolab_activesync / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_activesync) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_activesync-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_activesync-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_activesync-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_activesync-skin-larry
Plugin kolab_activesync / Skin larry

%package -n roundcubemail-plugin-kolab_activesync-skin-classic
Summary:        Plugin kolab_activesync / Skin classic
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_activesync) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-classic) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_activesync-skin-classic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_activesync-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_activesync-skin-classic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_activesync-skin-classic
Plugin kolab_activesync / Skin classic

%package -n roundcubemail-plugin-kolab_addressbook-skin-larry
Summary:        Plugin kolab_addressbook / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_addressbook) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_addressbook-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_addressbook-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_addressbook-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_addressbook-skin-larry
Plugin kolab_addressbook / Skin larry

%package -n roundcubemail-plugin-kolab_addressbook-skin-classic
Summary:        Plugin kolab_addressbook / Skin classic
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_addressbook) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-classic) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_addressbook-skin-classic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_addressbook-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_addressbook-skin-classic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_addressbook-skin-classic
Plugin kolab_addressbook / Skin classic

%package -n roundcubemail-plugin-kolab_delegation-skin-larry
Summary:        Plugin kolab_delegation / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_delegation) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_delegation-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_delegation-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_delegation-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_delegation-skin-larry
Plugin kolab_delegation / Skin larry

%package -n roundcubemail-plugin-kolab_delegation-skin-classic
Summary:        Plugin kolab_delegation / Skin classic
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_delegation) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-classic) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_delegation-skin-classic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_delegation-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_delegation-skin-classic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_delegation-skin-classic
Plugin kolab_delegation / Skin classic

%package -n roundcubemail-plugin-kolab_files-skin-larry
Summary:        Plugin kolab_files / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_files) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_files-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_files-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_files-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_files-skin-larry
Plugin kolab_files / Skin larry

%package -n roundcubemail-plugin-kolab_notes-skin-larry
Summary:        Plugin kolab_notes / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_notes) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_notes-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_notes-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_notes-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_notes-skin-larry
Plugin kolab_notes / Skin larry

%package -n roundcubemail-plugin-kolab_tags-skin-larry
Summary:        Plugin kolab_tags / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-kolab_tags) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-kolab_tags-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_tags-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-kolab_tags-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_tags-skin-larry
Plugin kolab_tags / Skin larry

%package -n roundcubemail-plugin-tasklist-skin-larry
Summary:        Plugin tasklist / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-tasklist) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-tasklist-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-tasklist-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-tasklist-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-tasklist-skin-larry
Plugin tasklist / Skin larry

%package -n roundcubemail-plugin-calendar-skin-larry-assets
Summary:        Plugin calendar / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-calendar-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-calendar-skin-larry-assets
Plugin calendar / Skin larry (Assets Package)

%package -n roundcubemail-plugin-calendar-skin-classic-assets
Summary:        Plugin calendar / Skin classic (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-calendar-skin-classic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-calendar-skin-classic-assets
Plugin calendar / Skin classic (Assets Package)

%package -n roundcubemail-plugin-kolab_2fa-skin-larry-assets
Summary:        Plugin kolab_2fa / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_2fa-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_2fa-skin-larry-assets
Plugin kolab_2fa / Skin larry (Assets Package)

%package -n roundcubemail-plugin-kolab_activesync-skin-larry-assets
Summary:        Plugin kolab_activesync / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_activesync-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_activesync-skin-larry-assets
Plugin kolab_activesync / Skin larry (Assets Package)

%package -n roundcubemail-plugin-kolab_activesync-skin-classic-assets
Summary:        Plugin kolab_activesync / Skin classic (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_activesync-skin-classic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_activesync-skin-classic-assets
Plugin kolab_activesync / Skin classic (Assets Package)

%package -n roundcubemail-plugin-kolab_addressbook-skin-larry-assets
Summary:        Plugin kolab_addressbook / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_addressbook-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_addressbook-skin-larry-assets
Plugin kolab_addressbook / Skin larry (Assets Package)

%package -n roundcubemail-plugin-kolab_addressbook-skin-classic-assets
Summary:        Plugin kolab_addressbook / Skin classic (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_addressbook-skin-classic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_addressbook-skin-classic-assets
Plugin kolab_addressbook / Skin classic (Assets Package)

%package -n roundcubemail-plugin-kolab_delegation-skin-larry-assets
Summary:        Plugin kolab_delegation / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_delegation-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_delegation-skin-larry-assets
Plugin kolab_delegation / Skin larry (Assets Package)

%package -n roundcubemail-plugin-kolab_delegation-skin-classic-assets
Summary:        Plugin kolab_delegation / Skin classic (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_delegation-skin-classic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_delegation-skin-classic-assets
Plugin kolab_delegation / Skin classic (Assets Package)

%package -n roundcubemail-plugin-kolab_files-skin-larry-assets
Summary:        Plugin kolab_files / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_files-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_files-skin-larry-assets
Plugin kolab_files / Skin larry (Assets Package)

%package -n roundcubemail-plugin-kolab_notes-skin-larry-assets
Summary:        Plugin kolab_notes / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_notes-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_notes-skin-larry-assets
Plugin kolab_notes / Skin larry (Assets Package)

%package -n roundcubemail-plugin-kolab_tags-skin-larry-assets
Summary:        Plugin kolab_tags / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-kolab_tags-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-kolab_tags-skin-larry-assets
Plugin kolab_tags / Skin larry (Assets Package)

%package -n roundcubemail-plugin-libcalendaring-skin-larry-assets
Summary:        Plugin libcalendaring / Skin larry (Assets)
Group:          Applications/Internet
Requires:       roundcubemail(plugin-libcalendaring) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Obsoletes:      roundcubemail-plugin-libcalendaring-skin-larry
Provides:       roundcubemail(plugin-libcalendaring-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-libcalendaring-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-libcalendaring-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-libcalendaring-skin-larry-assets
Plugin libcalendaring / Skin larry (Assets Package)

%package -n roundcubemail-plugin-libkolab-skin-larry-assets
Summary:        Plugin libkolab / Skin larry (Assets)
Group:          Applications/Internet
Requires:       roundcubemail(plugin-libkolab) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Obsoletes:      roundcubemail-plugin-libkolab-skin-larry
Provides:       roundcubemail(plugin-libkolab-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-libkolab-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-libkolab-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-libkolab-skin-larry-assets
Plugin libkolab / Skin larry (Assets Package)

%package -n roundcubemail-plugin-tasklist-skin-larry-assets
Summary:        Plugin tasklist / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-tasklist-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-tasklist-skin-larry-assets
Plugin tasklist / Skin larry (Assets Package)

%prep
%setup -q  -c "%{name}-%{version}"

pushd %{name}-%{version}

%if 0%{?plesk}
# Provide defaults for Plesk
cp -af %{SOURCE100} plugins/calendar/config.inc.php.dist
cp -af %{SOURCE101} plugins/kolab_addressbook/config.inc.php.dist
cp -af %{SOURCE102} plugins/kolab_folders/config.inc.php.dist
cp -af %{SOURCE103} plugins/libkolab/config.inc.php.dist
%endif

%patch0001 -p1
%patch1001 -p1

find -type d -name "helpdocs" -exec rm -rvf {} \; 2>/dev/null || :

rm -rf plugins/kolab_zpush
rm -rf plugins/owncloud

# Remove the results of patching when there's an incidental offset
find . -type f -name "*.orig" -delete

# Remove hidden files
find . -type f -name ".*" -delete

# Eliminate links
for link in `find . -type l`; do
    source=$(readlink -f ${link})
    rm -rf ${link}
    cp -av ${source} ${link}
done

popd

for plugin in $(find %{name}-%{version}/plugins -mindepth 1 -maxdepth 1 -type d | sort); do
    target_dir=$(echo ${plugin} | %{__sed} -e "s|%{name}-%{version}|%{name}-plugin-$(basename ${plugin})-%{version}|g")
    %{__mkdir_p} $(dirname ${target_dir})
    cp -av ${plugin} ${target_dir}

    (
        echo "%package -n roundcubemail-plugin-$(basename ${plugin})"
        echo "Summary:        Plugin $(basename ${plugin})"
        echo "Group:          Applications/Internet"
        echo "Requires:       roundcubemail(core) >= %%{roundcube_version}"
        echo "Requires:       roundcubemail(plugin-$(basename ${plugin})-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        if [ -d "${plugin}/skins/" ]; then
            echo "Requires:       roundcubemail(plugin-$(basename ${plugin})-skin) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        fi

        for rplugin in $(grep -rn "require_plugin" ${plugin}/ | cut -d"'" -f2 | sort); do
            if [ -d "%{name}-%{version}/plugins/${rplugin}" ]; then
                echo "Requires:       roundcubemail(plugin-${rplugin}) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            else
                echo "Requires:       roundcubemail(plugin-${rplugin}) >= %%{roundcube_version}"
            fi
        done

        if [ "$(basename ${plugin})" == "kolab_files" ]; then
            echo "Requires:       php-curl"
        elif [ "$(basename ${plugin})" == "kolab_2fa" ]; then
            echo "Requires:       php-endroid-qrcode"
            echo "Requires:       php-enygma-yubikey"
            echo "Requires:       php-spomky-labs-otphp"
        elif [ "$(basename ${plugin})" == "html_converter" ]; then
            echo "Requires:       lynx"
        fi

        echo "Provides:       roundcubemail(plugin-$(basename ${plugin})) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo ""
        echo "%description -n roundcubemail-plugin-$(basename ${plugin})"
        echo "Plugin $(basename ${plugin})"
        echo ""
    ) >> plugins.packages

    (
        echo "%files -n roundcubemail-plugin-$(basename ${plugin}) -f plugin-$(basename ${plugin}).files"
        echo "%defattr(-,root,root,-)"
        if [ -d "${plugin}/config" -o -f "${plugin}/config.inc.php" -o -f "${plugin}/config.inc.php.dist" ]; then
            echo "%attr(0640,root,%%{httpd_group}) %config(noreplace) %%{_sysconfdir}/roundcubemail/$(basename ${plugin}).inc.php"
        fi
        echo ""
    ) >> plugins.files

    (
        echo "%pre -n roundcubemail-plugin-$(basename ${plugin})"
        echo "if [ -f \"%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted\" ]; then"
        echo "    %%{__rm} -f \"%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted\""
        echo "fi"
        echo ""
    ) >> plugins.pre

    (
        echo "%posttrans -n roundcubemail-plugin-$(basename ${plugin})"
        echo "if [ ! -f \"%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted\" ]; then"
        echo "    if [ -f \"%%{php_inidir}/apc.ini\"  -o -f \"%%{php_inidir}/apcu.ini\" ]; then"
        echo "        if [ ! -z \"\$(grep ^apc.enabled=1 %%{php_inidir}/apc{,u}.ini 2>/dev/null)\" ]; then"
        echo "%if 0%%{?with_systemd}"
        echo "            /bin/systemctl condrestart %%{httpd_name}.service"
        echo "%else"
        echo "            /sbin/service %%{httpd_name} condrestart"
        echo "%endif"
        echo "        fi"
        echo "    fi"
        echo "    %%{__mkdir_p} %%{_localstatedir}/lib/rpm-state/roundcubemail/"
        echo "    touch %%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
        echo "fi"
        echo ""
        if [ ! -z "$(find ${plugin} -type d -name SQL)" ]; then
            echo "for dir in \$(find /usr/share/roundcubemail/plugins/$(basename ${plugin})/ -type d -name SQL); do"
            echo "    # Skip plugins with multiple drivers and no kolab driver"
            echo "    if [ ! -z \"\$(echo \${dir} | grep driver)\" ]; then"
            echo "        if [ -z \"\$(echo \${dir} | grep kolab)\" ]; then"
            echo "            continue"
            echo "        fi"
            echo "    fi"
            echo ""
            echo "    /usr/share/roundcubemail/bin/updatedb.sh \\"
            echo "        --dir \${dir} \\"
            echo "        --package $(basename ${plugin}) \\"
            echo "        >/dev/null 2>&1 || :"
            echo ""
            echo "done"
            echo ""
        fi
    ) >> plugins.post

    (
        echo "%package -n roundcubemail-plugin-$(basename ${plugin})-assets"
        echo "Summary:        Plugin $(basename ${plugin}) Assets"
        echo "Group:          Applications/Internet"
        echo "Provides:       roundcubemail(plugin-$(basename ${plugin})-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo ""
        echo "%description -n roundcubemail-plugin-$(basename ${plugin})-assets"
        echo "Plugin $(basename ${plugin}) Assets"
        echo ""
    ) >> plugins-assets.packages

    (
        echo "%files -n roundcubemail-plugin-$(basename ${plugin})-assets -f plugin-$(basename ${plugin})-assets.files"
        echo "%defattr(-,root,root,-)"
        echo ""
    ) >> plugins-assets.files

    for skin in larry classic; do
        for dir in $(find ${target_dir} -type d -name "${skin}" | grep -v "helpdocs" | sort); do
            starget_dir=$(echo ${dir} | %{__sed} -e "s|%{name}-plugin-$(basename ${plugin})-%{version}|%{name}-plugin-$(basename ${plugin})-skin-${skin}-%{version}|g")
            %{__mkdir_p} $(dirname ${starget_dir})
            %{__mv} ${dir} ${starget_dir}

            (
                echo "%package -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}"
                echo "Summary:        Plugin $(basename ${plugin}) / Skin ${skin}"
                echo "Group:          Applications/Internet"
                echo "Requires:       roundcubemail(plugin-$(basename ${plugin})) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Requires:       roundcubemail(skin-${skin}) >= %%{roundcube_version}"
                echo "Requires:       roundcubemail(plugin-$(basename ${plugin})-skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Provides:       roundcubemail(plugin-$(basename ${plugin})-skin) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Provides:       roundcubemail(plugin-$(basename ${plugin})-skin-${skin}) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo ""
                echo "%description -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}"
                echo "Plugin $(basename ${plugin}) / Skin ${skin}"
                echo ""
            ) >> plugins-skins.packages

            (
                echo "%files -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin} -f plugin-$(basename ${plugin})-skin-${skin}.files"
                echo "%defattr(-,root,root,-)"
                echo ""
            ) >> plugins-skins.files

            (
                echo "%package -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}-assets"
                echo "Summary:        Plugin $(basename ${plugin}) / Skin ${skin} (Assets)"
                echo "Group:          Applications/Internet"
                echo "Provides:       roundcubemail(plugin-$(basename ${plugin})-skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo ""
                echo "%description -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}-assets"
                echo "Plugin $(basename ${plugin}) / Skin ${skin} (Assets Package)"
                echo ""
            ) >> plugins-skins-assets.packages

            (
                echo "%files -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}-assets -f plugin-$(basename ${plugin})-skin-${skin}-assets.files"
                echo "%defattr(-,root,root,-)"
                echo ""
            ) >> plugins-skins-assets.files
        done
    done
done

cat \
    plugins.packages \
    plugins-assets.packages \
    plugins-skins.packages \
    plugins-skins-assets.packages \
    > packages

cat \
    plugins.files \
    plugins-assets.files \
    plugins-skins.files \
    plugins-skins-assets.files \
    > files

find | sort | tee files.find >/dev/null

%build

%install
%{__install} -pm 755 %{SOURCE1} .

function new_files() {
    find %{buildroot}%{datadir} -type d -exec echo "%dir {}" \; > current-new.files
    find %{buildroot}%{datadir} -type f >> current-new.files
    find %{buildroot}%{datadir} -type l >> current-new.files

    if [ -f "current.files" ]; then
        %{_bindir}/python ./comm.py current.files current-new.files
    else
        cat current-new.files
    fi

    %{__mv} current-new.files current.files
}

%{__rm} -rf %{buildroot}

%{__install} -d \
    %{buildroot}%{confdir} \
    %{buildroot}%{datadir}/public_html \
    %{buildroot}%{plugindir}

if [ -d "%{buildroot}%{datadir}/public_html/" ]; then
    asset_path="%{buildroot}%{datadir}/public_html/assets"
else
    asset_path="%{buildroot}%{datadir}/assets"
fi

%{__mkdir_p} ${asset_path}

echo "================================================================="
echo "Dividing Plugins, Plugin Assets, Plugin Skins and Plugin Skin Assets and Non-Assets"
echo "================================================================="

for plugin in $(find %{name}-%{version}/plugins/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort); do
    for skin in larry classic; do
        orig_dir="%{name}-plugin-${plugin}-skin-${skin}-%{version}"
        asset_dir="%{name}-plugin-${plugin}-skin-${skin}-assets-%{version}"

        # Compress the CSS
        for file in `find ${orig_dir} -type f -name "*.css"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            cat ${file} | %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) && \
                %{__rm} -rf ${file} || \
                %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
        done || :

        # Compress the JS, but not the already minified
        for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            uglifyjs ${file} > ${asset_loc}/$(basename ${file}) && \
                %{__rm} -rf ${file} || \
                %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
        done || :

        # The already minified JS can just be copied over to the assets location
        for file in `find ${orig_dir} -type f -name "*.min.js"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
        done || :

        # Other assets
        for file in $(find ${orig_dir} -type f \
                -name "*.eot" -o \
                -name "*.gif" -o \
                -name "*.ico" -o \
                -name "*.jpg" -o \
                -name "*.mp3" -o \
                -name "*.png" -o \
                -name "*.svg" -o \
                -name "*.swf" -o \
                -name "*.tif" -o \
                -name "*.ttf" -o \
                -name "*.woff"
            ); do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            %{__mv} -vf ${file} ${asset_loc}/$(basename $file)
        done || :

        # Purge empty directories
        find ${orig_dir} -type d -empty -delete || :
    done

    # Skin-independent assets
    orig_dir="%{name}-plugin-${plugin}-%{version}"
    asset_dir="%{name}-plugin-${plugin}-assets-%{version}"

    # Compress the CSS
    for file in `find ${orig_dir} -type f -name "*.css"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        cat ${file} | %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) && \
            %{__rm} -rf ${file} || \
            %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
    done

    # Compress the JS, but not the already minified
    for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        uglifyjs ${file} > ${asset_loc}/$(basename ${file}) && \
            %{__rm} -rf ${file} || \
            %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
    done

    # The already minified JS can just be copied over to the assets location
    for file in `find ${orig_dir} -type f -name "*.min.js"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
    done

    # Other assets
    for file in $(find ${orig_dir} -type f \
            -name "*.eot" -o \
            -name "*.gif" -o \
            -name "*.ico" -o \
            -name "*.jpg" -o \
            -name "*.mp3" -o \
            -name "*.png" -o \
            -name "*.svg" -o \
            -name "*.swf" -o \
            -name "*.tif" -o \
            -name "*.ttf" -o \
            -name "*.woff"
        ); do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__mv} -vf ${file} ${asset_loc}/$(basename $file)
    done

    if [ "${plugin}" == "pdfviewer" ]; then
        %{__mv} -vf ${orig_dir}/plugins/pdfviewer/viewer/locale ${asset_dir}/plugins/pdfviewer/viewer/.
        %{__mv} -vf ${orig_dir}/plugins/pdfviewer/viewer/viewer.html ${asset_dir}/plugins/pdfviewer/viewer/.
    fi

    # Purge empty directories
    find ${orig_dir} -type d -empty -delete || :

    # Install the assets
    for file in `find %{name}-plugin-${plugin}-assets-%{version} -type f`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|%{name}-plugin-${plugin}-assets-%{version}|${asset_path}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
    done || :

    new_files > plugin-${plugin}-assets.files

    echo "== Files for plugin ${plugin}: =="
    cat plugin-${plugin}-assets.files
    echo "==========================="

    %{__mkdir_p} %{buildroot}%{plugindir}
    cp -a %{name}-plugin-${plugin}-%{version}/plugins/${plugin} %{buildroot}%{plugindir}/.

    if [ -f "%{buildroot}%{plugindir}/${plugin}/config.inc.php.dist" ]; then
        pushd %{buildroot}%{plugindir}/${plugin}
        %{__mv} config.inc.php.dist %{buildroot}%{confdir}/${plugin}.inc.php
        ln -s ../../../../..%{confdir}/${plugin}.inc.php config.inc.php
        popd
    fi

    if [ -f "%{buildroot}%{plugindir}/${plugin}/logon_page.html" ]; then
        %{__mkdir_p} %{buildroot}%{confdir}
        %{__mv} -vf %{buildroot}%{plugindir}/${plugin}/logon_page.html %{buildroot}%{confdir}
        pushd %{buildroot}%{plugindir}/${plugin}/
        ln -s ../../../../..%{confdir}/logon_page.html logon_page.html
        popd
    fi

    new_files > plugin-${plugin}.files

    echo "== Files for plugin ${plugin}: =="
    cat plugin-${plugin}.files
    echo "==========================="
done

for plugin in $(find %{name}-%{version}/plugins/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort); do
    for skin in larry classic; do
        touch plugin-${plugin}-skin-${skin}.files
        touch plugin-${plugin}-skin-${skin}-assets.files

        if [ -d "%{name}-plugin-${plugin}-skin-${skin}-%{version}/plugins/${plugin}/skins/${skin}" ]; then
            %{__install} -d %{buildroot}%{plugindir}/${plugin}/skins/
            cp -a %{name}-plugin-${plugin}-skin-${skin}-%{version}/plugins/${plugin}/skins/${skin} %{buildroot}%{plugindir}/${plugin}/skins/.

            new_files > plugin-${plugin}-skin-${skin}.files

            echo "== Files for skin ${plugin}-${skin}: =="
            cat plugin-${plugin}-skin-${skin}.files
            echo "==========================="
        fi

        # Install the assets
        for file in `find %{name}-plugin-${plugin}-skin-${skin}-assets-%{version} -type f`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|%{name}-plugin-${plugin}-skin-${skin}-assets-%{version}|${asset_path}|g"))
            %{__mkdir_p} ${asset_loc}
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
        done || :

        new_files > plugin-${plugin}-skin-${skin}-assets.files

        echo "== Files for skin ${plugin}-${skin}: =="
        cat plugin-${plugin}-skin-${skin}-assets.files
        echo "==========================="

    done
done

# Provide the rpm state directory
%{__mkdir_p} %{buildroot}/%{_localstatedir}/lib/rpm-state/roundcubemail/

%{__sed} -r -i \
    -e 's|%{buildroot}||g' \
    -e '/^%dir\s*$/d' \
    -e '/^(%dir )*\/etc\/roundcubemail\//d' \
    -e '/^(%dir )*\/var\//d' \
    *.files

%pre -n roundcubemail-plugin-calendar
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-html_converter
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_2fa
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_activesync
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_addressbook
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_auth
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_config
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_delegation
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_files
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_folders
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_notes
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_shortcuts
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-kolab_tags
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-ldap_authentication
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-libcalendaring
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-libkolab
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-logon_page
if [ -f "%{plugindir}/logon_page/logon_page.html" ]; then
    mv -vf %{plugindir}/logon_page/logon_page.html %{confdir}/logon_page.html
fi

if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-odfviewer
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-pdfviewer
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-piwik_analytics
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-tasklist
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-tinymce_config
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre -n roundcubemail-plugin-wap_client
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%posttrans -n roundcubemail-plugin-calendar
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini"  -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

for dir in $(find /usr/share/roundcubemail/plugins/calendar/ -type d -name SQL); do
    # Skip plugins with multiple drivers and no kolab driver
    if [ ! -z "$(echo ${dir} | grep driver)" ]; then
        if [ -z "$(echo ${dir} | grep kolab)" ]; then
            continue
        fi
    fi

    /usr/share/roundcubemail/bin/updatedb.sh \
        --dir ${dir} \
        --package calendar \
        >/dev/null 2>&1 || :

done

%posttrans -n roundcubemail-plugin-kolab_2fa
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_activesync
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_addressbook
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_auth
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_config
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_delegation
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_files
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_folders
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_notes
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_shortcuts
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-kolab_tags
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-ldap_authentication
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-libcalendaring
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-libkolab
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

for dir in $(find /usr/share/roundcubemail/plugins/libkolab/ -type d -name SQL); do
    # Skip plugins with multiple drivers and no kolab driver
    if [ ! -z "$(echo ${dir} | grep driver)" ]; then
        if [ -z "$(echo ${dir} | grep kolab)" ]; then
            continue
        fi
    fi

    /usr/share/roundcubemail/bin/updatedb.sh \
        --dir ${dir} \
        --package libkolab \
        >/dev/null 2>&1 || :

done

%posttrans -n roundcubemail-plugin-logon_page
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-odfviewer
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-pdfviewer
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-piwik_analytics
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-tasklist
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

for dir in $(find /usr/share/roundcubemail/plugins/tasklist/ -type d -name SQL); do
    # Skip plugins with multiple drivers and no kolab driver
    if [ ! -z "$(echo ${dir} | grep driver)" ]; then
        if [ -z "$(echo ${dir} | grep kolab)" ]; then
            continue
        fi
    fi

    /usr/share/roundcubemail/bin/updatedb.sh \
        --dir ${dir} \
        --package tasklist \
        >/dev/null 2>&1 || :

done

%posttrans -n roundcubemail-plugin-tinymce_config
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%posttrans -n roundcubemail-plugin-wap_client
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini 2>/dev/null)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_localstatedir}/lib/rpm-state/
%dir %{_localstatedir}/lib/rpm-state/roundcubemail/

%files -n roundcubemail-plugin-calendar -f plugin-calendar.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/calendar.inc.php

%files -n roundcubemail-plugin-html_converter -f plugin-html_converter.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_2fa -f plugin-kolab_2fa.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/kolab_2fa.inc.php

%files -n roundcubemail-plugin-kolab_activesync -f plugin-kolab_activesync.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/kolab_activesync.inc.php

%files -n roundcubemail-plugin-kolab_addressbook -f plugin-kolab_addressbook.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/kolab_addressbook.inc.php

%files -n roundcubemail-plugin-kolab_auth -f plugin-kolab_auth.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/kolab_auth.inc.php

%files -n roundcubemail-plugin-kolab_config -f plugin-kolab_config.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_delegation -f plugin-kolab_delegation.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/kolab_delegation.inc.php

%files -n roundcubemail-plugin-kolab_files -f plugin-kolab_files.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/kolab_files.inc.php

%files -n roundcubemail-plugin-kolab_folders -f plugin-kolab_folders.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/kolab_folders.inc.php

%files -n roundcubemail-plugin-kolab_notes -f plugin-kolab_notes.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_shortcuts -f plugin-kolab_shortcuts.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_tags -f plugin-kolab_tags.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-ldap_authentication -f plugin-ldap_authentication.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/ldap_authentication.inc.php

%files -n roundcubemail-plugin-libcalendaring -f plugin-libcalendaring.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-libkolab -f plugin-libkolab.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/libkolab.inc.php

%files -n roundcubemail-plugin-loginfail -f plugin-loginfail.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-logon_page -f plugin-logon_page.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/logon_page.html

%files -n roundcubemail-plugin-odfviewer -f plugin-odfviewer.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-pdfviewer -f plugin-pdfviewer.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-piwik_analytics -f plugin-piwik_analytics.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/piwik_analytics.inc.php

%files -n roundcubemail-plugin-tasklist -f plugin-tasklist.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/tasklist.inc.php

%files -n roundcubemail-plugin-tinymce_config -f plugin-tinymce_config.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-wap_client -f plugin-wap_client.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/wap_client.inc.php

%files -n roundcubemail-plugin-calendar-assets -f plugin-calendar-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_2fa-assets -f plugin-kolab_2fa-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_activesync-assets -f plugin-kolab_activesync-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_addressbook-assets -f plugin-kolab_addressbook-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_auth-assets -f plugin-kolab_auth-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_config-assets -f plugin-kolab_config-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_delegation-assets -f plugin-kolab_delegation-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_files-assets -f plugin-kolab_files-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_folders-assets -f plugin-kolab_folders-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_notes-assets -f plugin-kolab_notes-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_shortcuts-assets -f plugin-kolab_shortcuts-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_tags-assets -f plugin-kolab_tags-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-ldap_authentication-assets -f plugin-ldap_authentication-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-libcalendaring-assets -f plugin-libcalendaring-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-libkolab-assets -f plugin-libkolab-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-loginfail-assets -f plugin-loginfail-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-logon_page-assets -f plugin-logon_page-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-odfviewer-assets -f plugin-odfviewer-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-pdfviewer-assets -f plugin-pdfviewer-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-piwik_analytics-assets -f plugin-piwik_analytics-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-tasklist-assets -f plugin-tasklist-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-tinymce_config-assets -f plugin-tinymce_config-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-calendar-skin-larry -f plugin-calendar-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-calendar-skin-classic -f plugin-calendar-skin-classic.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_2fa-skin-larry -f plugin-kolab_2fa-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_activesync-skin-larry -f plugin-kolab_activesync-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_activesync-skin-classic -f plugin-kolab_activesync-skin-classic.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_addressbook-skin-larry -f plugin-kolab_addressbook-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_addressbook-skin-classic -f plugin-kolab_addressbook-skin-classic.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_delegation-skin-larry -f plugin-kolab_delegation-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_delegation-skin-classic -f plugin-kolab_delegation-skin-classic.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_files-skin-larry -f plugin-kolab_files-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_notes-skin-larry -f plugin-kolab_notes-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_tags-skin-larry -f plugin-kolab_tags-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-tasklist-skin-larry -f plugin-tasklist-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-calendar-skin-larry-assets -f plugin-calendar-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-calendar-skin-classic-assets -f plugin-calendar-skin-classic-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_2fa-skin-larry-assets -f plugin-kolab_2fa-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_activesync-skin-larry-assets -f plugin-kolab_activesync-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_activesync-skin-classic-assets -f plugin-kolab_activesync-skin-classic-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_addressbook-skin-larry-assets -f plugin-kolab_addressbook-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_addressbook-skin-classic-assets -f plugin-kolab_addressbook-skin-classic-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_delegation-skin-larry-assets -f plugin-kolab_delegation-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_delegation-skin-classic-assets -f plugin-kolab_delegation-skin-classic-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_files-skin-larry-assets -f plugin-kolab_files-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_notes-skin-larry-assets -f plugin-kolab_notes-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-kolab_tags-skin-larry-assets -f plugin-kolab_tags-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-libcalendaring-skin-larry-assets -f plugin-libcalendaring-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-libkolab-skin-larry-assets -f plugin-libkolab-skin-larry-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-tasklist-skin-larry-assets -f plugin-tasklist-skin-larry-assets.files
%defattr(-,root,root,-)

%changelog
* Thu May 17 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 3.3.6-2
- Fix removal of first occurence of event when moving (T103344)

* Tue Apr 17 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 3.3.6-1
- Release of 3.3.6

* Fri Jan  5 2018 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.5-2
- Repack of 3.3.5

* Tue Nov 28 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.5-1
- Release of version 3.3.5

* Fri Oct  6 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.4-2
- Fix Etc/UTC timezone

* Mon Oct  2 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.4-1
- Release of version 3.3.4

* Wed Jul 19 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.3-1
- Release of version 3.3.3

* Wed Jun 28 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.2-1
- Release of version 3.3.2

* Thu May 25 2017 Timotheus Pokorra <tp@tbits.net> - 3.3.1-3
- Fix build error on Fedora 25, composer needs php-justinrainbow-json-schema4

* Wed May 24 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.1-2
- Fix reqression in handling delegated events

* Mon May 22 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.1-1
- Release of version 3.3.1

* Tue Apr  4 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3.0-1
- Release of version 3.3.0

* Fri Nov 11 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.3-0.20161115.git
- Check in 3.3 snapshot

* Fri Dec 18 2015 Timotheus Pokorra <tp@tbits.net> - 3.3-0.20151218.git
- dropping roundcubemail-plugin-libcalendaring-skin-larry because it is empty (#5303)
- rpm 4.13 rejects empty sub packages

* Tue Apr 21 2015 Timotheus Pokorra <tp@tbits.net> - 3.2.8-2
- adding libkolab-skin-larry

* Fri Mar 27 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.8-1
- Release of version 3.2.8

* Wed Feb 25 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.7-1
- Release of version 3.2.7

* Sun Feb 15 2015 Daniel Hoffend <dh@dotlan.net> - 3.2.5-2
- Removed tmpdir+symlink for odfviewer

* Sat Feb 14 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.5-1
- Release of version 3.2.5

* Wed Feb  4 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.4-1
- Release of version 3.2.4

* Sat Jan 24 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.3-5
- Fix symbolic link to go up far enough (#4307, comment #4).

* Thu Jan 22 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.3-2
- Fix #4095 (tags not being updated)

* Wed Jan 21 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.3-1
- Release of version 3.2.3

* Thu Jan  1 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.2-1
- Release of 3.2.2
- Fix reference to blank.gif (#4115)
- Fix folder navigation when splitting assets (#4114)
- Clarify configuring login as functionality to limit impersonation to settings only (#4113)
- Fix using a group for authorization of the login as functionality (#4111)
- Clarify the license verbiage (#4035)
- Add creating a folder dialog to save to cloud dialog (#4034)

* Wed Dec 10 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.1-1
- New upstream release

* Thu Dec 04 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.0-1
- Release 3.2.0

* Fri Aug 29 2014 Daniel Hoffend <dh@dotlan.net> - 3.2-0.8.git
- Update translations

* Tue Aug 12 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2-0.5.git
- New git master head snapshot

* Tue Jun 24 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2-0.4.git
- New git master head snapshot

* Fri Apr  4 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2-0.3.git
- New git master head snapshot

* Tue Feb 25 2014 Daniel Hoffend <dh@dotlan.net> - 3.2-0.2.git
-  Apply patch for #2867 oudated mysql initial
-  Apply patch for #2863 kolab_storage_cache::save()

* Fri Feb 14 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2-0.1.git
- Upstream snapshot with birthday calendar for Kolab 3.2

* Tue Feb 11 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.12-1
- New upstream version
- Fix memory issues with very large result sets (#2828)

* Tue Jan 28 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.11-1
- New upstream version

* Thu Jan  9 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.10-1
- New upstream version

* Thu Dec 26 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.9-1
- New upstream version

* Mon Nov 25 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.8-1
- New upstream version

* Mon Nov 11 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.7-1
- Extend xml column for photo and crypt keys
- Fix SQL syntax when purging a folder
- Set _mailbox property when saving (#2474)
- Fix memory leaks for recurring event (exceptions)

* Fri Nov  1 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.6-4
- Fix replacement of alarm values
- Also apply patch for #2463 - all day events displayed on wrong date
- Also apply patch for #2353 - ICS import efficiency
- Also apply patch for task enhancements
- New upstream version

* Fri Oct 18 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.5-1
- New upstream release, with major caching improvements

* Thu Sep 19 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.3-1
- New upstream release, resolves:

    2191    Restrict email addresses for identity creation/editing to
            what is registered in LDAP
    2197    Invitation Mail aren't send
    2209    not all location is displayed
    2214    PHP Fatal error in libvcalendar
    2241    Remove LDAP connection in
            load_user_role_plugins_and_settings() for better performance

* Wed Sep 11 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.2-1
- Release 3.1.2 with bugfixes

* Sun Aug 25 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.1-1
- Release 3.1.1 with bugfixes

* Thu Aug  8 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.0-1
- Release 3.1.0 after initial round of bug fixing

* Fri Jul 12 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1-0.6
- A new snapshot with enhanced domain discoery for kolab_auth

* Wed May  8 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1-0.5
- Correct kolab_files configuration
- Ship new snapshot
- Fix apc.ini grep problem

* Wed Oct 17 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0-0.24.git20121017.7a8916c2
- New snapshot (0.24)
- New snapshot (0.23)
- New snapshot (0.22)
- Ship activesync plugin (0.19)
- Require php-pear(HTTP_Request2) (0.19)
- Ship Kolab logo (0.17)
- Latest snapshot from git master HEAD (0.17)
- Add odfviewer files/ directory (0.17)
- Ship correct snapshot sources and indicate where the sources come from (0.14)
- Fix some packaging issues (#835617) (0.14)
- Actually require Roundcube core to be of version 0.9 or later as well (0.8)
- Require php-pear(HTTP_Request) (0.8)
- Another snapshot release (0.8)
- Add requirement for libkolabxml and php-kolabformat (0.2)
- Pre-release of Kolab 3.0 (0.1)

* Thu Apr 19 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7.1-2
- Rebuild

* Sat Apr 14 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7.1-1
- First package
