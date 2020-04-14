# Needed for opensuse build system
%if 0%{?opensuse_bs}
#!BuildIgnore:  boa
#!BuildIgnore:  cherokee
#!BuildIgnore:  nginx
#!BuildIgnore:  httpd-itk
#!BuildIgnore:  lighttpd
#!BuildIgnore:  thttpd

#!BuildIgnore:  fedora-logos-httpd

#!BuildIgnore:  php-mysql
%endif

%global bootstrap 0

%{!?php_inidir: %global php_inidir %{_sysconfdir}/php.d}

# Needed to reload the webserver if APC is installed/enabled.
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

%global _ap_sysconfdir %{_sysconfdir}/%{httpd_name}

# Paths. Do not include trailing slash
%global datadir %{_datadir}/roundcubemail
%global plugindir %{datadir}/plugins
%global confdir %{_sysconfdir}/roundcubemail
%global logdir /var/log/roundcubemail
%global tmpdir /var/lib/roundcubemail

%global rc_version 1.4.3.6
#%%global rc_rel_suffix rc2.12
%global dot_rel_suffix %{?rc_rel_suffix:.%{rc_rel_suffix}}
%global dash_rel_suffix %{?rc_rel_suffix:-%{rc_rel_suffix}}

Name:           roundcubemail
Version:        1.4.3.6

Release:        1.3%{?dist}.kolab_16

Summary:        Round Cube Webmail is a browser-based multilingual IMAP client

Group:          Applications/System
License:        GPLv2
URL:            http://www.roundcube.net

Source0:        roundcubemail-%{version}%{?dash_rel_suffix}.tar.gz
Source1:        comm.py

Source20:       roundcubemail.conf
Source21:       roundcubemail.logrotate

Source100:      plesk.config.inc.php
Source101:      plesk.managesieve.inc.php
Source102:      plesk.password.inc.php

Source200:      2017111400.sql

Patch201:       default-configuration.patch
Patch202:       roundcubemail-1.4-beta86-plugin-enigma-homedir.patch

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root%(%{__id_u} -n)

BuildRequires:  composer
%if 0%{?fedora}
# fix issue:
# have choice for php-composer(justinrainbow/json-schema) >= 2.0 needed by composer: php-justinrainbow-json-schema4 php-justinrainbow-json-schema
# have choice for php-composer(justinrainbow/json-schema) < 5 needed by composer: php-justinrainbow-json-schema4 php-justinrainbow-json-schema php-JsonSchema
BuildRequires:  php-justinrainbow-json-schema4
%endif

%if 0%{?plesk} < 1
BuildRequires:  php-gd
BuildRequires:  php-mbstring
BuildRequires:  php-pdo
BuildRequires:  php-pear >= 1.9.0
BuildRequires:  php-phpunit-PHPUnit
BuildRequires:  php-phpunit-PHPUnit-Selenium
BuildRequires:  php-xml

BuildRequires:  php-pear(Auth_SASL)
BuildRequires:  php-pear(DB)
BuildRequires:  php-pear(Mail_Mime)
BuildRequires:  php-pear(Mail_mimeDecode)
BuildRequires:  php-pear(MDB2) >= 2.5.0
BuildRequires:  php-pear(MDB2_Driver_mysqli)
BuildRequires:  php-pear(Net_IDNA2)
BuildRequires:  php-pear(Net_LDAP2)
BuildRequires:  php-kolab-net-ldap3
BuildRequires:  php-pear(Net_Sieve)
BuildRequires:  php-pear(Net_SMTP)
BuildRequires:  php-pear(Net_Socket)
%endif

%if "%{_arch}" != "ppc64" && "%{_arch}" != "ppc64le"
BuildRequires:  nodejs-less
%if 0%{?suse_version} < 1
BuildRequires:  uglify-js
%endif
%else
BuildRequires:  php-lessphp
%endif

%if 0%{?rhel} >= 8
%if "%{_arch}" != "ppc64" && "%{_arch}" != "ppc64le" && 0%{?suse_version} < 1
BuildRequires:  python%{?python3_pkgversion}-cssmin
%endif

# This can, regrettably, not be BuildRequires'ed, since the OSC
# command-line so epicly fails at downloading as large a chunk of data.
#BuildRequires:  firefox
BuildRequires:  python%{?python3_pkgversion}
BuildRequires:  python%{?python3_pkgversion}-nose
#BuildRequires:  python-selenium

%else

%if "%{_arch}" != "ppc64" && "%{_arch}" != "ppc64le" && 0%{?suse_version} < 1
BuildRequires:  python-cssmin
%endif

# This can, regrettably, not be BuildRequires'ed, since the OSC
# command-line so epicly fails at downloading as large a chunk of data.
#BuildRequires:  firefox
BuildRequires:  python
BuildRequires:  python-nose
#BuildRequires:  python-selenium

%endif # %if 0%{?rhel} >= 8

Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?plesk}
Requires:       %{name}-skin-plesk
Requires:       %{name}-skin-plesk-larry
%else
%if 0%{?kolab_enterprise}
Requires:       %{name}-skin-enterprise
%else
Requires:       %{name}-skin-chameleon
%endif
%endif

# Archive and Zipdownload plugins required through
# being listed in config.inc.php.sample.
Requires:       %{name}(plugin-acl) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-archive) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-password) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-managesieve) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-zipdownload) = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Roundcube is the world's most popular webmail software.

This is a meta-package that installs an appropriate bare minimum.

%package core
Summary:        The core of the Roundcube program
Group:          Applications/Internet
Provides:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}

%if 0%{?suse_version}
Requires:       http_daemon
Requires:       php >= 5.3
Recommends:     mod_php_any
%else
Requires:       webserver
Requires:       php-common >= 5.3
%endif

%if 0%{?fedora}
# to avoid on OBS, for packages depending on roundcubemail-core:
# have choice for webserver needed by roundcubemail-core: lighttpd httpd nginx cherokee
Requires:       httpd
%endif

Requires:       php-gd
Requires:       php-mbstring
Requires:       php-pear >= 1.9.0
Requires:       php-xml

Requires:       php-pear(Auth_SASL)
Requires:       php-pear(DB)
Requires:       php-pear(Mail_Mime)
Requires:       php-pear(Mail_mimeDecode)
Requires:       php-pear(MDB2) >= 2.5.0
Requires:       php-pear(MDB2_Driver_mysqli)
Requires:       php-pear(Net_IDNA2)
Requires:       php-pear(Net_Sieve)
Requires:       php-pear(Net_SMTP)
Requires:       php-pear(Net_Socket)

%if 0%{?plesk} < 1
Requires:       php-pear(Net_LDAP2)
Requires:       php-kolab-net-ldap3
%endif

%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-plesk)
Requires:       %{name}(skin-plesk-larry)
Requires:       %{name}(skin-plesk-larry-assets)
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise)
Requires:       %{name}(skin-kolab)
%endif
%else
Requires:       %{name}(skin-chameleon)
Requires:       %{name}(skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif

Requires:       %{name}(core-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

# The filesystem_attachments plugin is required.
Requires:       %{name}(plugin-filesystem_attachments) = %{?epoch:%{epoch}:}%{version}-%{release}
# The jqueryui plugin is required.
Requires:       %{name}(plugin-jqueryui) = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:      %{name}(plugin-legacy_browser)
Obsoletes:      %{name}-plugin-legacy_browser
Provides:       %{name}(plugin-legacy_browser) = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:      %{name}(plugin-threading_as_default}
Obsoletes:      %{name}-plugin-threading_as_default
Provides:       %{name}-plugin-threading_as_default = %{?epoch:%{epoch}:}%{version}-%{release}

%description core
The Roundcube program core functionality

%package core-assets
Summary:        Assets for Roundcube
Group:          Applications/Internet
Provides:       %{name}(core-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description core-assets
The assets sub-packages contains solely the static content
needed by Roundcube.

%package plugin-acl
Summary:        Plugin acl
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-acl-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Requires:       %{name}(plugin-acl-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-acl-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Requires:       %{name}-plugin-acl-skin-elastic = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-acl-skin-elastic-assets = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-acl-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-acl-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Requires:       %{name}(plugin-acl-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-acl-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-acl) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-acl
Plugin acl

%package plugin-additional_message_headers
Summary:        Plugin additional_message_headers
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-additional_message_headers-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-additional_message_headers-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-additional_message_headers-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-additional_message_headers-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-additional_message_headers-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-additional_message_headers) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-additional_message_headers
Plugin additional_message_headers

%package plugin-archive
Summary:        Plugin archive
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-archive-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-archive-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-archive-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-archive-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-archive-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-archive) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-archive
Plugin archive

%package plugin-attachment_reminder
Summary:        Plugin attachment_reminder
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-attachment_reminder-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-attachment_reminder-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-attachment_reminder-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-attachment_reminder-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-attachment_reminder-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-attachment_reminder) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-attachment_reminder
Plugin attachment_reminder

%package plugin-autologon
Summary:        Plugin autologon
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-autologon-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-autologon-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-autologon-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-autologon-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-autologon-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-autologon) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-autologon
Plugin autologon

%package plugin-database_attachments
Summary:        Plugin database_attachments
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-database_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-database_attachments-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-database_attachments-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-database_attachments-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-database_attachments-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-database_attachments) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-database_attachments
Plugin database_attachments

%package plugin-debug_logger
Summary:        Plugin debug_logger
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-debug_logger-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-debug_logger-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-debug_logger-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-debug_logger-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-debug_logger-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-debug_logger) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-debug_logger
Plugin debug_logger

%package plugin-emoticons
Summary:        Plugin emoticons
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-emoticons-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-emoticons-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-emoticons-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-emoticons-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-emoticons-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-emoticons) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-emoticons
Plugin emoticons

%package plugin-enigma
Summary:        Plugin enigma
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-enigma-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       php-pear-crypt-gpg
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Requires:       %{name}(plugin-enigma-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-enigma-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Requires:       %{name}-plugin-enigma-skin-elastic = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-enigma-skin-elastic-assets = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-enigma-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-enigma-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Requires:       %{name}(plugin-enigma-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-enigma-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-enigma) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-enigma
Plugin enigma

%package plugin-example_addressbook
Summary:        Plugin example_addressbook
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-example_addressbook-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-example_addressbook-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-example_addressbook-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-example_addressbook-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-example_addressbook-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-example_addressbook) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-example_addressbook
Plugin example_addressbook

%package plugin-filesystem_attachments
Summary:        Plugin filesystem_attachments
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-filesystem_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-filesystem_attachments-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-filesystem_attachments-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-filesystem_attachments-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-filesystem_attachments-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-filesystem_attachments) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-filesystem_attachments
Plugin filesystem_attachments

%package plugin-help
Summary:        Plugin help
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-help-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Requires:       %{name}(plugin-help-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-help-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Requires:       %{name}-plugin-help-skin-elastic = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-help-skin-elastic-assets = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-help-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-help-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Requires:       %{name}(plugin-help-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-help-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-help) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-help
Plugin help

%package plugin-hide_blockquote
Summary:        Plugin hide_blockquote
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-hide_blockquote-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Obsoletes:      %{name}-plugin-hide_blockquote-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-hide_blockquote-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-hide_blockquote-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Obsoletes:      %{name}-plugin-hide_blockquote-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-hide_blockquote-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-hide_blockquote-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-hide_blockquote-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Obsoletes:      %{name}(plugin-hide_blockquote-skin-elastic) < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-hide_blockquote-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-hide_blockquote) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-hide_blockquote
Plugin hide_blockquote

%package plugin-http_authentication
Summary:        Plugin http_authentication
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-http_authentication-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-http_authentication-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-http_authentication-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-http_authentication-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-http_authentication-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-http_authentication) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-http_authentication
Plugin http_authentication

%package plugin-identicon
Summary:        Plugin identicon
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-identicon-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-identicon-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-identicon-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-identicon-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-identicon-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-identicon) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-identicon
Plugin identicon

%package plugin-identity_select
Summary:        Plugin identity_select
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-identity_select-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-identity_select-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-identity_select-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-identity_select-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-identity_select-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-identity_select) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-identity_select
Plugin identity_select

%package plugin-jqueryui
Summary:        Plugin jqueryui
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-jqueryui-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Requires:       %{name}(plugin-jqueryui-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-jqueryui-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Requires:       %{name}-plugin-jqueryui-skin-elastic = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-jqueryui-skin-elastic-assets = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-jqueryui-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-jqueryui-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Requires:       %{name}(plugin-jqueryui-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-jqueryui-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-jqueryui) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-jqueryui
Plugin jqueryui

%package plugin-krb_authentication
Summary:        Plugin krb_authentication
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-krb_authentication-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-krb_authentication-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-krb_authentication-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-krb_authentication-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-krb_authentication-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-krb_authentication) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-krb_authentication
Plugin krb_authentication

%package plugin-managesieve
Summary:        Plugin managesieve
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-managesieve-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Requires:       %{name}(plugin-managesieve-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-managesieve-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Requires:       %{name}-plugin-managesieve-skin-elastic = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-managesieve-skin-elastic-assets = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-managesieve-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-managesieve-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Requires:       %{name}(plugin-managesieve-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-managesieve-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-managesieve) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-managesieve
Plugin managesieve

%package plugin-markasjunk
Summary:        Plugin markasjunk
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-markasjunk-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Obsoletes:      %{name}-plugin-markasjunk-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-markasjunk-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-markasjunk-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Obsoletes:      %{name}-plugin-markasjunk-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-markasjunk-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-markasjunk-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-markasjunk-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Obsoletes:      %{name}(plugin-markasjunk-skin-elastic) < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-markasjunk-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-markasjunk) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-markasjunk
Plugin markasjunk

%package plugin-new_user_dialog
Summary:        Plugin new_user_dialog
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-new_user_dialog-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-new_user_dialog-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-new_user_dialog-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-new_user_dialog-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-new_user_dialog-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-new_user_dialog) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-new_user_dialog
Plugin new_user_dialog

%package plugin-new_user_identity
Summary:        Plugin new_user_identity
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-new_user_identity-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-new_user_identity-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-new_user_identity-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-new_user_identity-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-new_user_identity-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-new_user_identity) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-new_user_identity
Plugin new_user_identity

%package plugin-newmail_notifier
Summary:        Plugin newmail_notifier
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-newmail_notifier-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-newmail_notifier-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-newmail_notifier-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-newmail_notifier-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-newmail_notifier-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-newmail_notifier) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-newmail_notifier
Plugin newmail_notifier

%package plugin-password
Summary:        Plugin password
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-password-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-password-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-password-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-password-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-password-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-password) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-password
Plugin password

%package plugin-redundant_attachments
Summary:        Plugin redundant_attachments
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-redundant_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-redundant_attachments-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-redundant_attachments-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-redundant_attachments-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-redundant_attachments-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-redundant_attachments) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-redundant_attachments
Plugin redundant_attachments

%package plugin-show_additional_headers
Summary:        Plugin show_additional_headers
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-show_additional_headers-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-show_additional_headers-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-show_additional_headers-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-show_additional_headers-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-show_additional_headers-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-show_additional_headers) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-show_additional_headers
Plugin show_additional_headers

%package plugin-squirrelmail_usercopy
Summary:        Plugin squirrelmail_usercopy
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-squirrelmail_usercopy-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-squirrelmail_usercopy-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-squirrelmail_usercopy-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-squirrelmail_usercopy-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-squirrelmail_usercopy-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-squirrelmail_usercopy) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-squirrelmail_usercopy
Plugin squirrelmail_usercopy

%package plugin-subscriptions_option
Summary:        Plugin subscriptions_option
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-subscriptions_option-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-subscriptions_option-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-subscriptions_option-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-subscriptions_option-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-subscriptions_option-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-subscriptions_option) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-subscriptions_option
Plugin subscriptions_option

%package plugin-userinfo
Summary:        Plugin userinfo
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-userinfo-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-userinfo-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-userinfo-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-userinfo-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-userinfo-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-userinfo) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-userinfo
Plugin userinfo

%package plugin-vcard_attachments
Summary:        Plugin vcard_attachments
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-vcard_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Obsoletes:      %{name}-plugin-vcard_attachments-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-vcard_attachments-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-vcard_attachments-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Obsoletes:      %{name}-plugin-vcard_attachments-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-vcard_attachments-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-vcard_attachments-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-vcard_attachments-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Obsoletes:      %{name}(plugin-vcard_attachments-skin-elastic) < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-vcard_attachments-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-vcard_attachments) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-vcard_attachments
Plugin vcard_attachments

%package plugin-virtuser_file
Summary:        Plugin virtuser_file
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-virtuser_file-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-virtuser_file-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-virtuser_file-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-virtuser_file-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-virtuser_file-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-virtuser_file) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-virtuser_file
Plugin virtuser_file

%package plugin-virtuser_query
Summary:        Plugin virtuser_query
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-virtuser_query-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-virtuser_query-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-virtuser_query-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-virtuser_query-skin-larry < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-virtuser_query-skin-larry-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-virtuser_query) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-virtuser_query
Plugin virtuser_query

%package plugin-zipdownload
Summary:        Plugin zipdownload
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-zipdownload-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
%if 0%{?plesk}
%if 0%{?bootstrap} < 1
Obsoletes:      %{name}-plugin-zipdownload-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-zipdownload-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-plesk) >= 0.4
Requires:       %{name}(skin-plesk-larry) >= 0.3
Requires:       %{name}(plugin-zipdownload-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%else
%if 0%{?kolab_enterprise}
%if 0%{?bootstrap} < 1
Requires:       %{name}(skin-enterprise) >= 0.3.7
Requires:       %{name}(skin-kolab) >= 0.4
%endif
Obsoletes:      %{name}-plugin-zipdownload-skin-elastic < %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      %{name}-plugin-zipdownload-skin-elastic-assets < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-zipdownload-skin-larry = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-plugin-zipdownload-skin-larry-assets = %{?epoch:%{epoch}:}%{version}-%{release}
%else
Requires:       %{name}(skin-chameleon) >= 0.3.9
Obsoletes:      %{name}(plugin-zipdownload-skin-elastic) < %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-zipdownload-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
%endif
%endif
Provides:       %{name}(plugin-zipdownload) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-zipdownload
Plugin zipdownload

%package plugin-acl-assets
Summary:        Plugin acl Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-acl-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-acl-assets
Plugin acl Assets

%package plugin-additional_message_headers-assets
Summary:        Plugin additional_message_headers Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-additional_message_headers-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-additional_message_headers-assets
Plugin additional_message_headers Assets

%package plugin-archive-assets
Summary:        Plugin archive Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-archive-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-archive-assets
Plugin archive Assets

%package plugin-attachment_reminder-assets
Summary:        Plugin attachment_reminder Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-attachment_reminder-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-attachment_reminder-assets
Plugin attachment_reminder Assets

%package plugin-autologon-assets
Summary:        Plugin autologon Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-autologon-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-autologon-assets
Plugin autologon Assets

%package plugin-database_attachments-assets
Summary:        Plugin database_attachments Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-database_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-database_attachments-assets
Plugin database_attachments Assets

%package plugin-debug_logger-assets
Summary:        Plugin debug_logger Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-debug_logger-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-debug_logger-assets
Plugin debug_logger Assets

%package plugin-emoticons-assets
Summary:        Plugin emoticons Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-emoticons-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-emoticons-assets
Plugin emoticons Assets

%package plugin-enigma-assets
Summary:        Plugin enigma Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-enigma-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-enigma-assets
Plugin enigma Assets

%package plugin-example_addressbook-assets
Summary:        Plugin example_addressbook Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-example_addressbook-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-example_addressbook-assets
Plugin example_addressbook Assets

%package plugin-filesystem_attachments-assets
Summary:        Plugin filesystem_attachments Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-filesystem_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-filesystem_attachments-assets
Plugin filesystem_attachments Assets

%package plugin-help-assets
Summary:        Plugin help Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-help-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-help-assets
Plugin help Assets

%package plugin-hide_blockquote-assets
Summary:        Plugin hide_blockquote Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-hide_blockquote-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-hide_blockquote-assets
Plugin hide_blockquote Assets

%package plugin-http_authentication-assets
Summary:        Plugin http_authentication Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-http_authentication-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-http_authentication-assets
Plugin http_authentication Assets

%package plugin-identicon-assets
Summary:        Plugin identicon Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-identicon-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-identicon-assets
Plugin identicon Assets

%package plugin-identity_select-assets
Summary:        Plugin identity_select Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-identity_select-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-identity_select-assets
Plugin identity_select Assets

%package plugin-jqueryui-assets
Summary:        Plugin jqueryui Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-jqueryui-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-jqueryui-assets
Plugin jqueryui Assets

%package plugin-krb_authentication-assets
Summary:        Plugin krb_authentication Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-krb_authentication-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-krb_authentication-assets
Plugin krb_authentication Assets

%package plugin-managesieve-assets
Summary:        Plugin managesieve Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-managesieve-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-managesieve-assets
Plugin managesieve Assets

%package plugin-markasjunk-assets
Summary:        Plugin markasjunk Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-markasjunk-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-markasjunk-assets
Plugin markasjunk Assets

%package plugin-new_user_dialog-assets
Summary:        Plugin new_user_dialog Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-new_user_dialog-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-new_user_dialog-assets
Plugin new_user_dialog Assets

%package plugin-new_user_identity-assets
Summary:        Plugin new_user_identity Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-new_user_identity-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-new_user_identity-assets
Plugin new_user_identity Assets

%package plugin-newmail_notifier-assets
Summary:        Plugin newmail_notifier Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-newmail_notifier-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-newmail_notifier-assets
Plugin newmail_notifier Assets

%package plugin-password-assets
Summary:        Plugin password Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-password-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-password-assets
Plugin password Assets

%package plugin-redundant_attachments-assets
Summary:        Plugin redundant_attachments Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-redundant_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-redundant_attachments-assets
Plugin redundant_attachments Assets

%package plugin-show_additional_headers-assets
Summary:        Plugin show_additional_headers Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-show_additional_headers-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-show_additional_headers-assets
Plugin show_additional_headers Assets

%package plugin-squirrelmail_usercopy-assets
Summary:        Plugin squirrelmail_usercopy Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-squirrelmail_usercopy-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-squirrelmail_usercopy-assets
Plugin squirrelmail_usercopy Assets

%package plugin-subscriptions_option-assets
Summary:        Plugin subscriptions_option Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-subscriptions_option-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-subscriptions_option-assets
Plugin subscriptions_option Assets

%package plugin-userinfo-assets
Summary:        Plugin userinfo Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-userinfo-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-userinfo-assets
Plugin userinfo Assets

%package plugin-vcard_attachments-assets
Summary:        Plugin vcard_attachments Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-vcard_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-vcard_attachments-assets
Plugin vcard_attachments Assets

%package plugin-virtuser_file-assets
Summary:        Plugin virtuser_file Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-virtuser_file-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-virtuser_file-assets
Plugin virtuser_file Assets

%package plugin-virtuser_query-assets
Summary:        Plugin virtuser_query Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-virtuser_query-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-virtuser_query-assets
Plugin virtuser_query Assets

%package plugin-zipdownload-assets
Summary:        Plugin zipdownload Assets
Group:          Applications/Internet
Provides:       %{name}(plugin-zipdownload-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-zipdownload-assets
Plugin zipdownload Assets

%package plugin-acl-skin-elastic
Summary:        Plugin acl / Skin elastic
Group:          Applications/Internet
Requires:       %{name}(plugin-acl) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-acl-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-acl-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-acl-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-acl-skin-elastic
Plugin acl / Skin elastic

%package plugin-acl-skin-larry
Summary:        Plugin acl / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-acl) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-acl-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-acl-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-acl-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-acl-skin-larry
Plugin acl / Skin larry

%package plugin-enigma-skin-elastic
Summary:        Plugin enigma / Skin elastic
Group:          Applications/Internet
Requires:       %{name}(plugin-enigma) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-enigma-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-enigma-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-enigma-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-enigma-skin-elastic
Plugin enigma / Skin elastic

%package plugin-enigma-skin-larry
Summary:        Plugin enigma / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-enigma) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-enigma-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-enigma-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-enigma-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-enigma-skin-larry
Plugin enigma / Skin larry

%package plugin-help-skin-elastic
Summary:        Plugin help / Skin elastic
Group:          Applications/Internet
Requires:       %{name}(plugin-help) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-help-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-help-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-help-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-help-skin-elastic
Plugin help / Skin elastic

%package plugin-help-skin-larry
Summary:        Plugin help / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-help) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-help-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-help-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-help-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-help-skin-larry
Plugin help / Skin larry

%package plugin-hide_blockquote-skin-larry
Summary:        Plugin hide_blockquote / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-hide_blockquote) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-hide_blockquote-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-hide_blockquote-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-hide_blockquote-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-hide_blockquote-skin-larry
Plugin hide_blockquote / Skin larry

%package plugin-jqueryui-skin-elastic
Summary:        Plugin jqueryui / Skin elastic
Group:          Applications/Internet
Requires:       %{name}(plugin-jqueryui) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-jqueryui-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-jqueryui-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-jqueryui-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-jqueryui-skin-elastic
Plugin jqueryui / Skin elastic

%package plugin-jqueryui-skin-larry
Summary:        Plugin jqueryui / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-jqueryui) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-jqueryui-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-jqueryui-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-jqueryui-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-jqueryui-skin-larry
Plugin jqueryui / Skin larry

%package plugin-managesieve-skin-elastic
Summary:        Plugin managesieve / Skin elastic
Group:          Applications/Internet
Requires:       %{name}(plugin-managesieve) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-managesieve-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-managesieve-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-managesieve-skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-managesieve-skin-elastic
Plugin managesieve / Skin elastic

%package plugin-managesieve-skin-larry
Summary:        Plugin managesieve / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-managesieve) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-managesieve-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-managesieve-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-managesieve-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-managesieve-skin-larry
Plugin managesieve / Skin larry

%package plugin-markasjunk-skin-larry
Summary:        Plugin markasjunk / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-markasjunk) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-markasjunk-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-markasjunk-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-markasjunk-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-markasjunk-skin-larry
Plugin markasjunk / Skin larry

%package plugin-vcard_attachments-skin-larry
Summary:        Plugin vcard_attachments / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-vcard_attachments) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-vcard_attachments-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-vcard_attachments-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-vcard_attachments-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-vcard_attachments-skin-larry
Plugin vcard_attachments / Skin larry

%package plugin-zipdownload-skin-larry
Summary:        Plugin zipdownload / Skin larry
Group:          Applications/Internet
Requires:       %{name}(plugin-zipdownload) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(plugin-zipdownload-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-zipdownload-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-zipdownload-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-zipdownload-skin-larry
Plugin zipdownload / Skin larry

%package plugin-acl-skin-elastic-assets
Summary:        Plugin acl / Skin elastic (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-acl-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-acl-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-acl-skin-elastic-assets
Plugin acl / Skin elastic (Assets Package)

%package plugin-acl-skin-larry-assets
Summary:        Plugin acl / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-acl-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-acl-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-acl-skin-larry-assets
Plugin acl / Skin larry (Assets Package)

%package plugin-enigma-skin-elastic-assets
Summary:        Plugin enigma / Skin elastic (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-enigma-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-enigma-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-enigma-skin-elastic-assets
Plugin enigma / Skin elastic (Assets Package)

%package plugin-enigma-skin-larry-assets
Summary:        Plugin enigma / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-enigma-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-enigma-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-enigma-skin-larry-assets
Plugin enigma / Skin larry (Assets Package)

%package plugin-help-skin-elastic-assets
Summary:        Plugin help / Skin elastic (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-help-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-help-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-help-skin-elastic-assets
Plugin help / Skin elastic (Assets Package)

%package plugin-help-skin-larry-assets
Summary:        Plugin help / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-help-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-help-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-help-skin-larry-assets
Plugin help / Skin larry (Assets Package)

%package plugin-hide_blockquote-skin-larry-assets
Summary:        Plugin hide_blockquote / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-hide_blockquote-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-hide_blockquote-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-hide_blockquote-skin-larry-assets
Plugin hide_blockquote / Skin larry (Assets Package)

%package plugin-jqueryui-skin-elastic-assets
Summary:        Plugin jqueryui / Skin elastic (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-jqueryui-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-jqueryui-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-jqueryui-skin-elastic-assets
Plugin jqueryui / Skin elastic (Assets Package)

%package plugin-jqueryui-skin-larry-assets
Summary:        Plugin jqueryui / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-jqueryui-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-jqueryui-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-jqueryui-skin-larry-assets
Plugin jqueryui / Skin larry (Assets Package)

%package plugin-managesieve-skin-elastic-assets
Summary:        Plugin managesieve / Skin elastic (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-managesieve-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-managesieve-skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-managesieve-skin-elastic-assets
Plugin managesieve / Skin elastic (Assets Package)

%package plugin-managesieve-skin-larry-assets
Summary:        Plugin managesieve / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-managesieve-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-managesieve-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-managesieve-skin-larry-assets
Plugin managesieve / Skin larry (Assets Package)

%package plugin-markasjunk-skin-larry-assets
Summary:        Plugin markasjunk / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-markasjunk-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-markasjunk-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-markasjunk-skin-larry-assets
Plugin markasjunk / Skin larry (Assets Package)

%package plugin-vcard_attachments-skin-larry-assets
Summary:        Plugin vcard_attachments / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-vcard_attachments-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-vcard_attachments-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-vcard_attachments-skin-larry-assets
Plugin vcard_attachments / Skin larry (Assets Package)

%package plugin-zipdownload-skin-larry-assets
Summary:        Plugin zipdownload / Skin larry (Assets)
Group:          Applications/Internet
Requires:       %{name}(plugin-zipdownload-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(plugin-zipdownload-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description plugin-zipdownload-skin-larry-assets
Plugin zipdownload / Skin larry (Assets Package)

%package skin-elastic
Summary:        Skin elastic
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(skin-elastic) = %{?epoch:%{epoch}:}%{version}-%{release}

%description skin-elastic
Skin elastic

%package skin-larry
Summary:        Skin larry
Group:          Applications/Internet
Requires:       %{name}(core) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description skin-larry
Skin larry

%package skin-elastic-assets
Summary:        Skin elastic (Assets)
Group:          Applications/Internet
Provides:       %{name}(skin-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(skin-elastic-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description skin-elastic-assets
Skin elastic (Assets Package)

%package skin-larry-assets
Summary:        Skin larry (Assets)
Group:          Applications/Internet
Provides:       %{name}(skin-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       %{name}(skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description skin-larry-assets
Skin larry (Assets Package)

%prep
%setup -q -c "%{name}-%{version}%{?dash_rel_suffix}"

pushd %{name}-%{version}%{?dash_rel_suffix}

cp -vf "%{SOURCE200}" SQL/mysql/
rm -rvf SQL/mysql/2016081200.sql

rm -rf temp/js_cache/

find . -type d -name "classic" | while read dir; do
    rm -rvf ${dir}
done

%if 0%{?plesk}
cp -vf %{SOURCE100} config/config.inc.php.sample
cp -vf %{SOURCE101} plugins/managesieve/config.inc.php.dist
cp -vf %{SOURCE102} plugins/password/config.inc.php.dist
%endif

%patch201 -p1
%if 0%{?plesk} < 1
%patch202 -p1
%endif

# Remove the results of patching when there's an incidental offset
find . -type f -name "*.orig" | while read file; do
    rm -rvf ${file}
done

# Remove hidden files and directories
find . -type f -name ".*" | while read file; do
    rm -rvf ${file}
done

find . -type d -name ".*" ! -name "." ! -name ".." | while read dir; do
    rm -rvf ${dir}
done

while [ ! -z "$(find . -type d -empty)" ]; do
    find . -type d -empty | while read dir; do
        rm -rvf ${dir}
    done
done

# Remove any reference to sqlite in config file so people don't
# mistakely assume it works
%{__sed} -i '/sqlite/d' config/defaults.inc.php
%{__sed} -i 's/\r//' SQL/mssql.initial.sql

# Remove password plugin helpers in Python
rm -rf plugins/password/helpers/chpass-wrapper.py
popd

cp -a %{name}-%{version}%{?dash_rel_suffix}/{CHANGELOG,LICENSE,README.md} .

rm -rf %{name}-%{version}%{?dash_rel_suffix}/plugins/jqueryui/themes/redmond

for skin in elastic larry; do
    # Template files and the like
    for sdir in $(find %{name}-%{version}%{?dash_rel_suffix}/ -type d -name "${skin}" | sort); do
        target_dir=$(echo ${sdir} | %{__sed} -e "s|%{name}-%{version}%{?dash_rel_suffix}|%{name}-skin-${skin}-%{version}%{?dash_rel_suffix}|g")
        %{__mkdir_p} $(dirname ${target_dir})
        # Copy all, including assets, for the -devel sub-package
        cp -av ${sdir} ${target_dir}
    done

    (
        echo "%package skin-${skin}"
        echo "Summary:        Skin ${skin}"
        echo "Group:          Applications/Internet"
        echo "Requires:       %%{name}(core) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo "Requires:       %%{name}(skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo "Provides:       %%{name}(skin) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo "Provides:       %%{name}(skin-${skin}) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo ""
        echo "%description skin-${skin}"
        echo "Skin ${skin}"
        echo ""
    ) >> skins.packages

    (
        echo "%files skin-${skin} -f skin-${skin}.files"
        echo "%defattr(-,root,root,-)"
        echo ""
    ) >> skins.files

    (
        echo "%package skin-${skin}-assets"
        echo "Summary:        Skin ${skin} (Assets)"
        echo "Group:          Applications/Internet"
        echo "Provides:       %%{name}(skin-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo "Provides:       %%{name}(skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo ""
        echo "%description skin-${skin}-assets"
        echo "Skin ${skin} (Assets Package)"
        echo ""
    ) >> skins-assets.packages

    (
        echo "%files skin-${skin}-assets -f skin-${skin}-assets.files"
        echo "%defattr(-,root,root,-)"
        echo ""
    ) >> skins-assets.files

    %{__rm} -rf %{name}-skin-${skin}-%{version}%{?dash_rel_suffix}/plugins
done

for plugin in $(find %{name}-%{version}%{?dash_rel_suffix}/plugins -mindepth 1 -maxdepth 1 -type d | sort); do
    target_dir=$(echo ${plugin} | %{__sed} -e "s|%{name}-%{version}%{?dash_rel_suffix}|%{name}-plugin-$(basename ${plugin})-%{version}%{?dash_rel_suffix}|g")
    %{__mkdir_p} $(dirname ${target_dir})
    cp -av ${plugin} ${target_dir}

    # Special treatment of the jquery plugin
    if [ "$(basename ${plugin})" == "jqueryui" ]; then
        %{__mv} ${target_dir}/themes ${target_dir}/skins
        %{__sed} -i -e 's/themes/skins/g' ${target_dir}/{config.inc.php.dist,jqueryui.php,README}
    fi

    (
        echo "%package plugin-$(basename ${plugin})"
        echo "Summary:        Plugin $(basename ${plugin})"
        echo "Group:          Applications/Internet"
        echo "Requires:       %%{name}(core) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo "Requires:       %%{name}(plugin-$(basename ${plugin})-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        if [ "$(basename ${plugin})" == "enigma" ]; then
            echo "Requires:       php-pear-crypt-gpg"
        fi
        if [ -d "${target_dir}/skins/" ]; then
            echo "%%if 0%%{?plesk}"
            echo "%%if 0%%{?bootstrap} < 1"
            if [ -d "${target_dir}/skins/elastic/" ]; then
                echo "Requires:       %%{name}(plugin-$(basename ${plugin})-skin-elastic) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            else
                echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-elastic < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-elastic-assets < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            fi
            echo "Requires:       %%{name}(skin-plesk) >= 0.4"
            echo "Requires:       %%{name}(skin-plesk-larry) >= 0.3"
            echo "Requires:       %%{name}(plugin-$(basename ${plugin})-skin-larry) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            echo "%%endif"
            echo "%%else"
            echo "%%if 0%%{?kolab_enterprise}"
            echo "%%if 0%%{?bootstrap} < 1"
            echo "Requires:       %%{name}(skin-enterprise) >= 0.3.7"
            echo "Requires:       %%{name}(skin-kolab) >= 0.4"
            echo "%%endif"
            if [ -d "${target_dir}/skins/elastic/" ]; then
                echo "Requires:       %%{name}-plugin-$(basename ${plugin})-skin-elastic = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Requires:       %%{name}-plugin-$(basename ${plugin})-skin-elastic-assets = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            else
                echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-elastic < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-elastic-assets < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            fi
            if [ -d "${target_dir}/skins/larry/" ]; then
                echo "Requires:       %%{name}-plugin-$(basename ${plugin})-skin-larry = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Requires:       %%{name}-plugin-$(basename ${plugin})-skin-larry-assets = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            else
                echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-larry < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-larry-assets < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            fi
            echo "%%else"
            echo "Requires:       %%{name}(skin-chameleon) >= 0.3.9"
            if [ -d "${target_dir}/skins/elastic/" ]; then
                echo "Requires:       %%{name}(plugin-$(basename ${plugin})-skin-elastic) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            else
                echo "Obsoletes:      %%{name}(plugin-$(basename ${plugin})-skin-elastic) < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            fi
            if [ -d "${target_dir}/skins/larry/" ]; then
                echo "Requires:       %%{name}(plugin-$(basename ${plugin})-skin-larry) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            else
                echo "Obsoletes:      %%{name}(plugin-$(basename ${plugin})-skin-larry) < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            fi
            echo "%%endif"
            echo "%%endif"
        else
            echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-elastic < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-elastic-assets < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-larry < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            echo "Obsoletes:      %%{name}-plugin-$(basename ${plugin})-skin-larry-assets < %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        fi
        echo "Provides:       %%{name}(plugin-$(basename ${plugin})) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo ""
        echo "%description plugin-$(basename ${plugin})"
        echo "Plugin $(basename ${plugin})"
        echo ""
    ) >> plugins.packages

    (
        echo "%files plugin-$(basename ${plugin}) -f plugin-$(basename ${plugin}).files"
        echo "%defattr(-,root,root,-)"
        if [ -d "${plugin}/config" -o -f "${plugin}/config.inc.php" -o -f "${plugin}/config.inc.php.dist" ]; then
            echo "%attr(0640,root,%%{httpd_group}) %config(noreplace) %%{_sysconfdir}/%%{name}/$(basename ${plugin}).inc.php"
        fi
        echo ""
    ) >> plugins.files

    (
        echo "%pre plugin-$(basename ${plugin})"
        echo "if [ -f \"%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted\" ]; then"
        echo "    %%{__rm} -f \"%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted\""
        echo "fi"
        echo ""
    ) >> plugins.pre

    (
        echo "%posttrans plugin-$(basename ${plugin})"
        echo "if [ ! -f "%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then"
        echo "    if [ -f \"%%{php_inidir}/apc.ini\" -o -f \"%%{php_inidir}/apcu.ini\" ]; then"
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
            echo "    if [ ! -z \"\$(echo \$dir | grep driver)\" ]; then"
            echo "        if [ -z \"\$(echo \$dir | grep kolab)\" ]; then"
            echo "            continue"
            echo "        fi"
            echo "    fi"
            echo ""
            echo "    %%{_datadir}/roundcubemail/bin/updatedb.sh \\"
            echo "        --dir \$dir \\"
            echo "        --package $(basename ${plugin}) \\"
            echo "        >/dev/null 2>&1 || :"
            echo ""
            echo "done"
            echo ""
        fi
    ) >> plugins.post

    (
        echo "%package plugin-$(basename ${plugin})-assets"
        echo "Summary:        Plugin $(basename ${plugin}) Assets"
        echo "Group:          Applications/Internet"
        echo "Provides:       %%{name}(plugin-$(basename ${plugin})-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo ""
        echo "%description plugin-$(basename ${plugin})-assets"
        echo "Plugin $(basename ${plugin}) Assets"
        echo ""
    ) >> plugins-assets.packages

    (
        echo "%files plugin-$(basename ${plugin})-assets -f plugin-$(basename ${plugin})-assets.files"
        echo "%defattr(-,root,root,-)"
        echo ""
    ) >> plugins-assets.files

    for skin in elastic larry; do
        for dir in $(find ${target_dir} -type d -name "${skin}" | sort); do
            starget_dir=$(echo ${dir} | %{__sed} -e "s|%{name}-plugin-$(basename ${plugin})-%{version}%{?dash_rel_suffix}|%{name}-plugin-$(basename ${plugin})-skin-${skin}-%{version}%{?dash_rel_suffix}|g")
            %{__mkdir_p} $(dirname ${starget_dir})
            %{__mv} ${dir} ${starget_dir}

            (
                echo "%package plugin-$(basename ${plugin})-skin-${skin}"
                echo "Summary:        Plugin $(basename ${plugin}) / Skin ${skin}"
                echo "Group:          Applications/Internet"
                echo "Requires:       %%{name}(plugin-$(basename ${plugin})) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Requires:       %%{name}(skin-${skin}) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Requires:       %%{name}(plugin-$(basename ${plugin})-skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Provides:       %%{name}(plugin-$(basename ${plugin})-skin) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Provides:       %%{name}(plugin-$(basename ${plugin})-skin-${skin}) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo ""
                echo "%description plugin-$(basename ${plugin})-skin-${skin}"
                echo "Plugin $(basename ${plugin}) / Skin ${skin}"
                echo ""
            ) >> plugins-skins.packages

            (
                echo "%files plugin-$(basename ${plugin})-skin-${skin} -f plugin-$(basename ${plugin})-skin-${skin}.files"
                echo "%defattr(-,root,root,-)"
                echo ""
            ) >> plugins-skins.files

            (
                echo "%package plugin-$(basename ${plugin})-skin-${skin}-assets"
                echo "Summary:        Plugin $(basename ${plugin}) / Skin ${skin} (Assets)"
                echo "Group:          Applications/Internet"
                echo "Requires:       %%{name}(plugin-$(basename ${plugin})-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Requires:       %%{name}(skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Provides:       %%{name}(plugin-$(basename ${plugin})-skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo ""
                echo "%description plugin-$(basename ${plugin})-skin-${skin}-assets"
                echo "Plugin $(basename ${plugin}) / Skin ${skin} (Assets Package)"
                echo ""
            ) >> plugins-skins-assets.packages

            (
                echo "%files plugin-$(basename ${plugin})-skin-${skin}-assets -f plugin-$(basename ${plugin})-skin-${skin}-assets.files"
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
    skins.packages \
    skins-assets.packages \
    > packages

cat \
    plugins.files \
    plugins-assets.files \
    plugins-skins.files \
    plugins-skins-assets.files \
    skins.files \
    skins-assets.files \
    > files

find | sort | tee files.find >/dev/null

%build
pushd %{name}-%{version}%{?dash_rel_suffix}
mkdir -p $HOME/.composer
echo '{}' > $HOME/.composer/composer.json
cat > composer.json << EOF
{
    "name": "kolab/roundcubemail",
    "description": "Roundcube Webmail for Kolab",
    "license": "GPL-3.0",
    "require": { "php": ">=5.3.3" },
    "autoload": {
        "psr-0": { "": "/usr/share/pear/" },
        "psr-4": { "": "/usr/share/php/" }
    }
}
EOF
composer -vvv dumpautoload --optimize
popd

%install
%{__install} -pm 755 %{SOURCE1} .

function new_files() {
    find %{buildroot}%{datadir} -type d -exec echo "%dir {}" \; > current-new.files
    find %{buildroot}%{datadir} -type f >> current-new.files
    find %{buildroot}%{datadir} -type l >> current-new.files

    if [ -f "current.files" ]; then
        python ./comm.py current.files current-new.files
    else
        cat current-new.files
    fi

    %{__mv} current-new.files current.files
}

%{__rm} -rf %{buildroot}

%{__install} -d \
%if 0%{?plesk} < 1
    %{buildroot}%{_ap_sysconfdir}/conf.d \
%endif
    %{buildroot}%{_sysconfdir}/logrotate.d \
    %{buildroot}%{confdir} \
    %{buildroot}%{datadir}/public_html \
    %{buildroot}%{logdir} \
    %{buildroot}%{tmpdir}/plugins

pushd %{name}-%{version}%{?dash_rel_suffix}

%if 0%{?plesk} < 1
%{__install} -pm 644 %SOURCE20 %{buildroot}%{_ap_sysconfdir}/conf.d
%endif

%{__install} -pm 644 %SOURCE21 %{buildroot}%{_sysconfdir}/logrotate.d/roundcubemail

sed -i -e 's/apache apache/%{httpd_user} %{httpd_group}/g' \
    %{buildroot}%{_sysconfdir}/logrotate.d/roundcubemail

# use dist files as config files
%{__install} -pm 644 config/config.inc.php.sample %{buildroot}%{confdir}/config.inc.php
%{__install} -pm 644 config/defaults.inc.php %{buildroot}%{confdir}/defaults.inc.php
%{__install} -pm 644 config/mimetypes.php %{buildroot}%{confdir}/mimetypes.php

pushd %{buildroot}%{datadir}
%{__ln_s} ../../..%{confdir} config
%{__ln_s} ../../..%{logdir} logs
%{__ln_s} ../../..%{tmpdir} temp
popd

# Utilities
%{__cp} -a bin/ %{buildroot}%{datadir}/bin/
%{__cp} -a vendor/ %{buildroot}%{datadir}/vendor/

# The core of the program
%{__install} -pm 644 index.php %{buildroot}%{datadir}/index.php
%{__install} -d %{buildroot}%{datadir}/program/
%{__cp} -a program/include/ %{buildroot}%{datadir}/program/include/
%{__cp} -a program/lib/ %{buildroot}%{datadir}/program/lib/
%{__cp} -a program/localization/ %{buildroot}%{datadir}/program/localization/
%{__cp} -a program/steps/ %{buildroot}%{datadir}/program/steps/
%{__install} -pm 644 public_html/index.php %{buildroot}%{datadir}/public_html/index.php
popd

#
# Exclude the following external libraries
#

# php-pear-Auth-SASL
%{__rm} -rf %{buildroot}/%{datadir}/program/lib/Auth/SASL/ \
    %{buildroot}/%{datadir}/program/lib/Auth/SASL.php

# php-pear-Net-LDAP3
%{__rm} -rf %{buildroot}/%{datadir}/program/lib/Net/LDAP3/ \
    %{buildroot}/%{datadir}/program/lib/Net/LDAP3.php

# php-pear-Net-IDNA2
%{__rm} -rf %{buildroot}/%{datadir}/program/lib/Net/IDNA2/ \
    %{buildroot}/%{datadir}/program/lib/Net/IDNA2.php

# php-pear-Net-SMTP
%{__rm} -rf %{buildroot}/%{datadir}/program/lib/Net/SMTP.php

# php-pear-Net-Socket
%{__rm} -rf %{buildroot}/%{datadir}/program/lib/Net/Socket.php

# php-pear-Mail
%{__rm} -rf %{buildroot}/%{datadir}/program/lib/Mail/

# php-pear-MDB2
%{__rm} -rf %{buildroot}/%{datadir}/program/lib/MDB2/ \
    %{buildroot}/%{datadir}/program/lib/MDB2.php

# php-pear
%{__rm} -rf %{buildroot}/%{datadir}/program/lib/PEAR.php \
    %{buildroot}/%{datadir}/program/lib/PEAR5.php

# Remove any empty directory we might be left with
find %{buildroot}/%{datadir} -type d -empty -delete

%{__install} -d \
    %{buildroot}%{plugindir} \
    %{buildroot}%{datadir}/skins

%if 0%{?rhel} > 5 || 0%{?fedora} > 13
# php-pear-Net-Sieve
%{__rm} -rf %{buildroot}/%{plugindir}/managesieve/lib/Net
%endif

if [ -d "%{buildroot}%{datadir}/public_html/" ]; then
    asset_path="%{buildroot}%{datadir}/public_html/assets"
else
    asset_path="%{buildroot}%{datadir}/assets"
fi

%{__mkdir_p} ${asset_path}

orig_dir="%{name}-%{version}%{?dash_rel_suffix}"
asset_dir="%{name}-assets-%{version}%{?dash_rel_suffix}$(echo ${asset_path} | %{__sed} -e 's|%{buildroot}%{datadir}||g')"

# Remove the skins and installer directories from ${orig_dir}
%{__rm} -rf ${orig_dir}/{installer,skins}

echo "Original directory for core: ${orig_dir}"
echo "Asset directory for core: ${asset_dir}"

# Compile and compress the CSS
for file in `find ${orig_dir} -type f -name "styles.less" -o -name "print.less" -o -name "embed.less" | grep -vE "${orig_dir}/(plugins|skins)/" `; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
    %{__mkdir_p} ${asset_loc}
    %{_bindir}/lessc -x ${file} > ${asset_loc}/$(basename ${file} .less).css
done
find ${asset_loc} -type f -name "*.css" -empty -delete
find ${asset_loc} -type d -empty -delete

# Compress the CSS
for file in `find ${orig_dir} -type f -name "*.css" ! -path "*tests/*" | grep -vE "${orig_dir}/(plugins|skins)/"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
    %{__mkdir_p} ${asset_loc}
    cat ${file} | python %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) || \
        %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
done

# Compress the JS, but not the already minified
for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js" | grep -vE "${orig_dir}/(plugins|skins)/"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
    %{__mkdir_p} ${asset_loc}
    uglifyjs ${file} > ${asset_loc}/$(basename ${file}) || \
        %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
done

# The already minified JS can just be copied over to the assets location
for file in `find ${orig_dir} -type f -name "*.min.js" | grep -vE "${orig_dir}/(plugins|skins)/"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
    %{__mkdir_p} ${asset_loc}
    %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
done

# Other assets
for file in $(find ${orig_dir} -type f \
        -name "*.eot" -o \
        -name "*.gif" -o \
        -name "*.ico" -o \
        -name "*.jpg" -o \
        -name "*.mp3" -o \
        -name "dummy.pdf" -o \
        -name "*.png" -o \
        -name "*.svg" -o \
        -name "*.swf" -o \
        -name "*.tif" -o \
        -name "*.tiff" -o \
        -name "*.ttf" -o \
        -name "*.wav" -o \
        -name "*.webp" -o \
        -name "*.woff" -o \
        -name "*.woff2" | \
        grep -vE "${orig_dir}/(plugins|skins)/"
    ); do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
    %{__mkdir_p} ${asset_loc}
    %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
done

new_files > core.files

#echo "== Files for core: =="
#cat core.files
#echo "==========================="

for file in `find %{name}-assets-%{version}%{?dash_rel_suffix}/ -type f`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|%{name}-assets-%{version}%{?dash_rel_suffix}|%{buildroot}%{datadir}|g"))
    %{__mkdir_p} ${asset_loc}
    %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
done

new_files > core-assets.files

#echo "== Files for core assets: =="
#cat core-assets.files
#echo "==========================="

echo "================================================================="
echo "Dividing Skin Assets and Non-Assets"
echo "================================================================="

for skin in elastic larry; do
    # Take the files from the original directory,
    # Find the ones that are assets,
    # Move those over to the assets-specific directory.

    orig_dir="%{name}-skin-${skin}-%{version}%{?dash_rel_suffix}"
    asset_dir="%{name}-skin-${skin}-assets-%{version}%{?dash_rel_suffix}$(echo ${asset_path} | %{__sed} -e 's|%{buildroot}%{datadir}||g')"

    echo "Original directory for the ${skin} skin: ${orig_dir}"
    echo "Asset directory for the ${skin} skin: ${asset_dir}"

    # Compile and compress the CSS
    for file in `find ${orig_dir} -type f -name "styles.less" -o -name "print.less" -o -name "embed.less"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{_bindir}/lessc -x ${file} > ${asset_loc}/$(basename ${file} .less).css
    done
    find ${asset_loc} -type f -name "*.css" -empty -delete
    find ${asset_log} -type d -empty -delete

    # Compress the CSS
    for file in `find ${orig_dir} -type f -name "*.css" ! -path "*tests/*"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        cat ${file} | python %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) || \
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    # Compress the JS, but not the already minified
    for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        uglifyjs ${file} > ${asset_loc}/$(basename ${file}) || \
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    # The already minified JS can just be copied over to the assets location
    for file in `find ${orig_dir} -type f -name "*.min.js"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    # Other assets
    for file in $(find ${orig_dir} -type f \
            -name "*.eot" -o \
            -name "*.gif" -o \
            -name "*.ico" -o \
            -name "*.jpg" -o \
            -name "*.mp3" -o \
            -name "dummy.pdf" -o \
            -name "*.png" -o \
            -name "*.svg" -o \
            -name "*.swf" -o \
            -name "*.tif" -o \
            -name "*.tiff" -o \
            -name "*.ttf" -o \
            -name "*.wav" -o \
            -name "*.webp" -o \
            -name "*.woff" -o \
            -name "*.woff2"
        ); do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    # The watermark.html is an asset, too
    if [ -f "${orig_dir}/skins/${skin}/watermark.html" ]; then
        %{__cp} -av ${orig_dir}/skins/${skin}/watermark.html \
            ${asset_dir}/skins/${skin}/watermark.html
    fi

    find %{name}-skin-${skin}-%{version}%{?dash_rel_suffix}/skins/ -type d -empty -delete

    cp -a %{name}-skin-${skin}-%{version}%{?dash_rel_suffix}/skins/* %{buildroot}%{datadir}/skins/.

    if [ "${skin}" == "elastic" ]; then
        pushd %{buildroot}%{datadir}/skins/elastic
        %{__rm} -rvf images
        ln -s ../../public_html/assets/skins/elastic/images images
        popd
    fi

    new_files > skin-${skin}.files

    #echo "== Files for skin ${skin}: =="
    #cat skin-${skin}.files
    #echo "==========================="

    %{__mkdir_p} %{buildroot}%{datadir}/public_html/assets/skins/
    cp -a %{name}-skin-${skin}-assets-%{version}%{?dash_rel_suffix}/public_html/assets/skins/* %{buildroot}%{datadir}/public_html/assets/skins/.

    new_files > skin-${skin}-assets.files

    #echo "== Files for skin assets ${skin}: =="
    #cat skin-${skin}-assets.files
    #echo "==========================="
done

echo "==================================================================================="
echo "Dividing Plugins, Plugin Assets, Plugin Skins and Plugin Skin Assets and Non-Assets"
echo "==================================================================================="

for plugin in $(find %{name}-%{version}%{?dash_rel_suffix}/plugins/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort); do
    for skin in elastic larry; do
        orig_dir="%{name}-plugin-${plugin}-skin-${skin}-%{version}%{?dash_rel_suffix}"

        # No skin, no assets
        if [ ! -d "${orig_dir}" ]; then
            continue
        fi

        asset_dir="%{name}-plugin-${plugin}-skin-${skin}-assets-%{version}%{?dash_rel_suffix}"

        # Compile and compress the CSS
        for file in `find ${orig_dir} -type f -name "styles.less" -o -name "print.less" -o -name "embed.less" `; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            %{_bindir}/lessc -x ${file} > ${asset_loc}/$(basename ${file} .less).css
        done
        find ${asset_loc} -type f ! -name "*.css" -empty -delete
        find ${asset_loc} -type d -empty -delete

        # Compress the CSS
        for file in `find ${orig_dir} -type f -name "*.css" ! -path "*tests/"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            cat ${file} | python %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) || \
                %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
        done

        # Compress the JS, but not the already minified
        for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            uglifyjs ${file} > ${asset_loc}/$(basename ${file}) || \
                %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
        done

        # The already minified JS can just be copied over to the assets location
        for file in `find ${orig_dir} -type f -name "*.min.js"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
        done

        # Other assets
        for file in $(find ${orig_dir} -type f \
                -name "*.eot" -o \
                -name "*.gif" -o \
                -name "*.ico" -o \
                -name "*.jpg" -o \
                -name "*.mp3" -o \
                -name "dummy.pdf" -o \
                -name "*.png" -o \
                -name "*.svg" -o \
                -name "*.swf" -o \
                -name "*.tif" -o \
                -name "*.tiff" -o \
                -name "*.ttf" -o \
                -name "*.wav" -o \
                -name "*.webp" -o \
                -name "*.woff" -o \
                -name "*.woff2"
            ); do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
        done

        # Purge empty directories
        find ${orig_dir} -type d -empty -delete
    done

    %{__mkdir_p} %{buildroot}%{plugindir}
    cp -a %{name}-plugin-${plugin}-%{version}%{?dash_rel_suffix}/plugins/${plugin} %{buildroot}%{plugindir}/.

    if [ -f "%{buildroot}%{plugindir}/${plugin}/config.inc.php.dist" ]; then
        pushd %{buildroot}%{plugindir}/${plugin}
        %{__mv} config.inc.php.dist %{buildroot}%{confdir}/${plugin}.inc.php
        ln -s ../../../../..%{confdir}/${plugin}.inc.php config.inc.php
        popd
    fi

    if [ "${plugin}" == "enigma" ]; then
        %{__mkdir_p} %{buildroot}%{tmpdir}/plugins/${plugin}/
        pushd %{buildroot}%{plugindir}/${plugin}
        %{__mv} -v home %{buildroot}%{tmpdir}/plugins/${plugin} || \
            mkdir -p %{buildroot}%{tmpdir}/plugins/${plugin}
        ln -sv ../../../../..%{tmpdir}/plugins/${plugin} home
        popd
    fi

    new_files > plugin-${plugin}.files

    #echo "== Files for plugin ${plugin}: =="
    #cat plugin-${plugin}.files
    #echo "==========================="

    # Skin-independent assets
    orig_dir="%{name}-plugin-${plugin}-%{version}%{?dash_rel_suffix}"
    asset_dir="%{name}-plugin-${plugin}-assets-%{version}%{?dash_rel_suffix}"

    # Compile and compress the CSS
    for file in `find ${orig_dir} -type f -name "styles.less" -o -name "print.less" -o -name "embed.less" `; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{_bindir}/lessc -x ${file} > ${asset_loc}/$(basename ${file} .less).css
    done
    find ${asset_loc} -type f -empty -delete
    find ${asset_loc} -type d -empty -delete

    # Compress the CSS
    for file in `find ${orig_dir} -type f -name "*.css" ! -path "*tests/"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        cat ${file} | python %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) || \
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    # Compress the JS, but not the already minified
    for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        uglifyjs ${file} > ${asset_loc}/$(basename ${file}) || \
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    # The already minified JS can just be copied over to the assets location
    for file in `find ${orig_dir} -type f -name "*.min.js"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    # Other assets
    for file in $(find ${orig_dir} -type f \
            -name "*.eot" -o \
            -name "*.gif" -o \
            -name "*.ico" -o \
            -name "*.jpg" -o \
            -name "*.mp3" -o \
            -name "dummy.pdf" -o \
            -name "*.png" -o \
            -name "*.svg" -o \
            -name "*.swf" -o \
            -name "*.tif" -o \
            -name "*.tiff" -o \
            -name "*.ttf" -o \
            -name "*.wav" -o \
            -name "*.webp" -o \
            -name "*.woff" -o \
            -name "*.woff2"
        ); do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    # Purge empty directories
    find ${orig_dir} -type d -empty -delete

%if 0%{?fedora}
    # Empty packages are not fun with Fedora
    if [ ! -d ${asset_loc} ]; then
        %{__mkdir_p} ${asset_loc}
        echo "/* Nothing here */" > ${asset_loc}/dummy.js
    fi
%endif

    # Install the assets
    for file in `find %{name}-plugin-${plugin}-assets-%{version}%{?dash_rel_suffix} -type f`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|%{name}-plugin-${plugin}-assets-%{version}%{?dash_rel_suffix}|$asset_path|g"))
        %{__mkdir_p} ${asset_loc}
        %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
    done

    new_files > plugin-${plugin}-assets.files
done

for plugin in $(find %{name}-%{version}%{?dash_rel_suffix}/plugins/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort); do
    for skin in elastic larry; do
        touch plugin-${plugin}-skin-${skin}.files
        touch plugin-${plugin}-skin-${skin}-assets.files

        if [ ! -d "%{name}-plugin-${plugin}-skin-${skin}-%{version}%{?dash_rel_suffix}/plugins/${plugin}/skins" ]; then
            rm -f plugin-${plugin}-skin-${skin}.files
            rm -f plugin-${plugin}-skin-${skin}-assets.files
            continue
        fi

        %{__install} -d %{buildroot}%{plugindir}/${plugin}/skins/
        cp -a %{name}-plugin-${plugin}-skin-${skin}-%{version}%{?dash_rel_suffix}/plugins/${plugin}/skins/${skin} %{buildroot}%{plugindir}/${plugin}/skins/.

        new_files > plugin-${plugin}-skin-${skin}.files
        if [ ! -s "plugin-${plugin}-skin-${skin}.files" ]; then
            rm -f plugin-${plugin}-skin-${skin}.files
        fi

        # Install the assets
        for file in `find %{name}-plugin-${plugin}-skin-${skin}-assets-%{version}%{?dash_rel_suffix} -type f`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|%{name}-plugin-${plugin}-skin-${skin}-assets-%{version}%{?dash_rel_suffix}|$asset_path|g"))
            %{__mkdir_p} ${asset_loc}
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
        done

        new_files > plugin-${plugin}-skin-${skin}-assets.files
        if [ ! -s "plugin-${plugin}-skin-${skin}-assets.files" ]; then
            rm -f plugin-${plugin}-skin-${skin}-assets.files
        fi
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

%pre
if [ -L %{plugindir}/enigma/home -a ! -d %{plugindir}/enigma/home ]; then
    %{__rm} -rf %{plugindir}/enigma/home >/dev/null 2>&1 || :
fi

%check
pushd %{name}-%{version}%{?dash_rel_suffix}/tests
phpunit --debug || :
popd

%clean
%{__rm} -rf %{buildroot}

%pre core
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-acl
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-additional_message_headers
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-archive
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-attachment_reminder
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-autologon
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-database_attachments
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-debug_logger
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-emoticons
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-enigma
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-example_addressbook
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-filesystem_attachments
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-help
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-hide_blockquote
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-http_authentication
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-identicon
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-identity_select
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-jqueryui
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-krb_authentication
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-managesieve
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-markasjunk
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-new_user_dialog
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-new_user_identity
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-newmail_notifier
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-password
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-redundant_attachments
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-show_additional_headers
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-squirrelmail_usercopy
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-subscriptions_option
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-userinfo
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-vcard_attachments
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-virtuser_file
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-virtuser_query
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%pre plugin-zipdownload
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%posttrans core
# replace default des string in config file for better security
function makedesstr () {
    chars=(0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z A
    B C D E F G H I J K L M N O P Q R S T U V W X Y Z)

    max=${#chars[*]}

    for i in `seq 1 24`; do
        let rand=${RANDOM}%%${max}
        str="${str}${chars[$rand]}"
    done
    echo $str
}

find %{logdir} -mindepth 1 -maxdepth 1 -type f -exec chown %{httpd_user}:%{httpd_group} {} \;

%{__sed} -i "s/rcmail-\!24ByteDESkey\*Str/`makedesstr`/" /etc/roundcubemail/defaults.inc.php || : &> /dev/null

%{__sed} -i -r -e "s/.*(\s*define\(\s*'RCMAIL_VERSION'\s*,\s*').*('\);)/\1%{version}-%{release}\2/g" \
    %{datadir}/program/include/iniset.php || :

if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%{_datadir}/roundcubemail/bin/updatedb.sh \
    --dir %{_datadir}/doc/roundcubemail-core-%{version}/SQL/ \
    --package roundcube || : \
    >/dev/null 2>&1

exit 0

%posttrans plugin-acl
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-additional_message_headers
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-archive
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-attachment_reminder
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-autologon
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-database_attachments
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-debug_logger
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-emoticons
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-enigma
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-example_addressbook
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-filesystem_attachments
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-help
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-hide_blockquote
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-http_authentication
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-identicon
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-identity_select
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-jqueryui
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-krb_authentication
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-managesieve
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-markasjunk
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-new_user_dialog
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-new_user_identity
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-newmail_notifier
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-password
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-redundant_attachments
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-show_additional_headers
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-squirrelmail_usercopy
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-subscriptions_option
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-userinfo
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-vcard_attachments
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-virtuser_file
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-virtuser_query
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%posttrans plugin-zipdownload
if [ ! -f %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted ]; then
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

%files
%defattr(-,root,root,-)
%doc %{name}-%{version}%{?dash_rel_suffix}/LICENSE
%doc %{name}-%{version}%{?dash_rel_suffix}/UPGRADING
%doc %{name}-%{version}%{?dash_rel_suffix}/SQL

%files core -f core.files
%defattr(-,root,root,-)
%doc %{name}-%{version}%{?dash_rel_suffix}/SQL
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if 0%{?suse_version}
%dir %{_ap_sysconfdir}/
%dir %{_ap_sysconfdir}/conf.d/
%attr(0755,root,%{httpd_group}) %dir %{confdir}
%endif
%if 0%{?plesk} < 1
%config(noreplace) %{_ap_sysconfdir}/conf.d/%{name}.conf
%endif
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/config.inc.php
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/defaults.inc.php
%attr(0640,root,%{httpd_group}) %{confdir}/mimetypes.php
%attr(0770,root,%{httpd_group}) %dir %{logdir}
%attr(0770,root,%{httpd_group}) %dir %{tmpdir}
%attr(0770,root,%{httpd_group}) %dir %{tmpdir}/plugins
%dir %{_localstatedir}/lib/rpm-state/
%dir %{_localstatedir}/lib/rpm-state/roundcubemail/

%files core-assets -f core-assets.files
%defattr(-,root,root,-)

%files plugin-acl -f plugin-acl.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/acl.inc.php

%files plugin-additional_message_headers -f plugin-additional_message_headers.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/additional_message_headers.inc.php

%files plugin-archive -f plugin-archive.files
%defattr(-,root,root,-)

%files plugin-attachment_reminder -f plugin-attachment_reminder.files
%defattr(-,root,root,-)

%files plugin-autologon -f plugin-autologon.files
%defattr(-,root,root,-)

%files plugin-database_attachments -f plugin-database_attachments.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/database_attachments.inc.php

%files plugin-debug_logger -f plugin-debug_logger.files
%defattr(-,root,root,-)

%files plugin-emoticons -f plugin-emoticons.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/emoticons.inc.php

%files plugin-enigma -f plugin-enigma.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/enigma.inc.php

%files plugin-example_addressbook -f plugin-example_addressbook.files
%defattr(-,root,root,-)

%files plugin-filesystem_attachments -f plugin-filesystem_attachments.files
%defattr(-,root,root,-)

%files plugin-help -f plugin-help.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/help.inc.php

%files plugin-hide_blockquote -f plugin-hide_blockquote.files
%defattr(-,root,root,-)

%files plugin-http_authentication -f plugin-http_authentication.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/http_authentication.inc.php

%files plugin-identicon -f plugin-identicon.files
%defattr(-,root,root,-)

%files plugin-identity_select -f plugin-identity_select.files
%defattr(-,root,root,-)

%files plugin-jqueryui -f plugin-jqueryui.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/jqueryui.inc.php

%files plugin-krb_authentication -f plugin-krb_authentication.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/krb_authentication.inc.php

%files plugin-managesieve -f plugin-managesieve.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/managesieve.inc.php

%files plugin-markasjunk -f plugin-markasjunk.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/markasjunk.inc.php

%files plugin-new_user_dialog -f plugin-new_user_dialog.files
%defattr(-,root,root,-)

%files plugin-new_user_identity -f plugin-new_user_identity.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/new_user_identity.inc.php

%files plugin-newmail_notifier -f plugin-newmail_notifier.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/newmail_notifier.inc.php

%files plugin-password -f plugin-password.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/password.inc.php

%files plugin-redundant_attachments -f plugin-redundant_attachments.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/redundant_attachments.inc.php

%files plugin-show_additional_headers -f plugin-show_additional_headers.files
%defattr(-,root,root,-)

%files plugin-squirrelmail_usercopy -f plugin-squirrelmail_usercopy.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/squirrelmail_usercopy.inc.php

%files plugin-subscriptions_option -f plugin-subscriptions_option.files
%defattr(-,root,root,-)

%files plugin-userinfo -f plugin-userinfo.files
%defattr(-,root,root,-)

%files plugin-vcard_attachments -f plugin-vcard_attachments.files
%defattr(-,root,root,-)

%files plugin-virtuser_file -f plugin-virtuser_file.files
%defattr(-,root,root,-)

%files plugin-virtuser_query -f plugin-virtuser_query.files
%defattr(-,root,root,-)

%files plugin-zipdownload -f plugin-zipdownload.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{_sysconfdir}/%{name}/zipdownload.inc.php

%files plugin-acl-assets -f plugin-acl-assets.files
%defattr(-,root,root,-)

%files plugin-additional_message_headers-assets -f plugin-additional_message_headers-assets.files
%defattr(-,root,root,-)

%files plugin-archive-assets -f plugin-archive-assets.files
%defattr(-,root,root,-)

%files plugin-attachment_reminder-assets -f plugin-attachment_reminder-assets.files
%defattr(-,root,root,-)

%files plugin-autologon-assets -f plugin-autologon-assets.files
%defattr(-,root,root,-)

%files plugin-database_attachments-assets -f plugin-database_attachments-assets.files
%defattr(-,root,root,-)

%files plugin-debug_logger-assets -f plugin-debug_logger-assets.files
%defattr(-,root,root,-)

%files plugin-emoticons-assets -f plugin-emoticons-assets.files
%defattr(-,root,root,-)

%files plugin-enigma-assets -f plugin-enigma-assets.files
%defattr(-,root,root,-)

%files plugin-example_addressbook-assets -f plugin-example_addressbook-assets.files
%defattr(-,root,root,-)

%files plugin-filesystem_attachments-assets -f plugin-filesystem_attachments-assets.files
%defattr(-,root,root,-)

%files plugin-help-assets -f plugin-help-assets.files
%defattr(-,root,root,-)

%files plugin-hide_blockquote-assets -f plugin-hide_blockquote-assets.files
%defattr(-,root,root,-)

%files plugin-http_authentication-assets -f plugin-http_authentication-assets.files
%defattr(-,root,root,-)

%files plugin-identicon-assets -f plugin-identicon-assets.files
%defattr(-,root,root,-)

%files plugin-identity_select-assets -f plugin-identity_select-assets.files
%defattr(-,root,root,-)

%files plugin-jqueryui-assets -f plugin-jqueryui-assets.files
%defattr(-,root,root,-)

%files plugin-krb_authentication-assets -f plugin-krb_authentication-assets.files
%defattr(-,root,root,-)

%files plugin-managesieve-assets -f plugin-managesieve-assets.files
%defattr(-,root,root,-)

%files plugin-markasjunk-assets -f plugin-markasjunk-assets.files
%defattr(-,root,root,-)

%files plugin-new_user_dialog-assets -f plugin-new_user_dialog-assets.files
%defattr(-,root,root,-)

%files plugin-new_user_identity-assets -f plugin-new_user_identity-assets.files
%defattr(-,root,root,-)

%files plugin-newmail_notifier-assets -f plugin-newmail_notifier-assets.files
%defattr(-,root,root,-)

%files plugin-password-assets -f plugin-password-assets.files
%defattr(-,root,root,-)

%files plugin-redundant_attachments-assets -f plugin-redundant_attachments-assets.files
%defattr(-,root,root,-)

%files plugin-show_additional_headers-assets -f plugin-show_additional_headers-assets.files
%defattr(-,root,root,-)

%files plugin-squirrelmail_usercopy-assets -f plugin-squirrelmail_usercopy-assets.files
%defattr(-,root,root,-)

%files plugin-subscriptions_option-assets -f plugin-subscriptions_option-assets.files
%defattr(-,root,root,-)

%files plugin-userinfo-assets -f plugin-userinfo-assets.files
%defattr(-,root,root,-)

%files plugin-vcard_attachments-assets -f plugin-vcard_attachments-assets.files
%defattr(-,root,root,-)

%files plugin-virtuser_file-assets -f plugin-virtuser_file-assets.files
%defattr(-,root,root,-)

%files plugin-virtuser_query-assets -f plugin-virtuser_query-assets.files
%defattr(-,root,root,-)

%files plugin-zipdownload-assets -f plugin-zipdownload-assets.files
%defattr(-,root,root,-)

%files plugin-acl-skin-elastic -f plugin-acl-skin-elastic.files
%defattr(-,root,root,-)

%files plugin-acl-skin-larry -f plugin-acl-skin-larry.files
%defattr(-,root,root,-)

%files plugin-enigma-skin-elastic -f plugin-enigma-skin-elastic.files
%defattr(-,root,root,-)

%files plugin-enigma-skin-larry -f plugin-enigma-skin-larry.files
%defattr(-,root,root,-)

%files plugin-help-skin-elastic -f plugin-help-skin-elastic.files
%defattr(-,root,root,-)

%files plugin-help-skin-larry -f plugin-help-skin-larry.files
%defattr(-,root,root,-)

%files plugin-hide_blockquote-skin-larry -f plugin-hide_blockquote-skin-larry.files
%defattr(-,root,root,-)

%files plugin-jqueryui-skin-elastic -f plugin-jqueryui-skin-elastic.files
%defattr(-,root,root,-)

%files plugin-jqueryui-skin-larry -f plugin-jqueryui-skin-larry.files
%defattr(-,root,root,-)

%files plugin-managesieve-skin-elastic -f plugin-managesieve-skin-elastic.files
%defattr(-,root,root,-)

%files plugin-managesieve-skin-larry -f plugin-managesieve-skin-larry.files
%defattr(-,root,root,-)

%files plugin-markasjunk-skin-larry -f plugin-markasjunk-skin-larry.files
%defattr(-,root,root,-)

%files plugin-vcard_attachments-skin-larry -f plugin-vcard_attachments-skin-larry.files
%defattr(-,root,root,-)

%files plugin-zipdownload-skin-larry -f plugin-zipdownload-skin-larry.files
%defattr(-,root,root,-)

%files plugin-acl-skin-elastic-assets -f plugin-acl-skin-elastic-assets.files
%defattr(-,root,root,-)

%files plugin-acl-skin-larry-assets -f plugin-acl-skin-larry-assets.files
%defattr(-,root,root,-)

%files plugin-enigma-skin-elastic-assets -f plugin-enigma-skin-elastic-assets.files
%defattr(-,root,root,-)

%files plugin-enigma-skin-larry-assets -f plugin-enigma-skin-larry-assets.files
%defattr(-,root,root,-)

%files plugin-help-skin-elastic-assets -f plugin-help-skin-elastic-assets.files
%defattr(-,root,root,-)

%files plugin-help-skin-larry-assets -f plugin-help-skin-larry-assets.files
%defattr(-,root,root,-)

%files plugin-hide_blockquote-skin-larry-assets -f plugin-hide_blockquote-skin-larry-assets.files
%defattr(-,root,root,-)

%files plugin-jqueryui-skin-elastic-assets -f plugin-jqueryui-skin-elastic-assets.files
%defattr(-,root,root,-)

%files plugin-jqueryui-skin-larry-assets -f plugin-jqueryui-skin-larry-assets.files
%defattr(-,root,root,-)

%files plugin-managesieve-skin-elastic-assets -f plugin-managesieve-skin-elastic-assets.files
%defattr(-,root,root,-)

%files plugin-managesieve-skin-larry-assets -f plugin-managesieve-skin-larry-assets.files
%defattr(-,root,root,-)

%files plugin-markasjunk-skin-larry-assets -f plugin-markasjunk-skin-larry-assets.files
%defattr(-,root,root,-)

%files plugin-vcard_attachments-skin-larry-assets -f plugin-vcard_attachments-skin-larry-assets.files
%defattr(-,root,root,-)

%files plugin-zipdownload-skin-larry-assets -f plugin-zipdownload-skin-larry-assets.files
%defattr(-,root,root,-)

%files skin-elastic -f skin-elastic.files
%defattr(-,root,root,-)

%files skin-larry -f skin-larry.files
%defattr(-,root,root,-)

%files skin-elastic-assets -f skin-elastic-assets.files
%defattr(-,root,root,-)

%files skin-larry-assets -f skin-larry-assets.files
%defattr(-,root,root,-)

%changelog
* Mon Mar  2 2020 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.4.3.6-1
- Check in 6 revisions ahead of upstream 1.4.3 release

* Wed Dec  4 2019 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.4.1.27-1
- Check in 27 revisions ahead of upstream 1.4.1 release

* Mon Oct  7 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-312.rc2.12
- Check in 12 revisions ahead of upstream 1.4-rc2 release

* Mon Jul  1 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-248.rc1.221
- Check in 221 revisions ahead of the upstream 1.4-rc1 release

* Mon Jun  3 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-246.rc1.167
- Check in 167 revisions ahead of the upstream 1.4-rc1 release

* Mon May 20 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-242.rc1.133
- Fix for context menu

* Wed May 15 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-240.rc1.133
- Check in 133 revisions ahead of the upstream 1.4-rc1 release

* Mon Apr 15 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-236.rc1.65
- Check in 65 revisions ahead of the upstream rc1 release

* Sat Jan 19 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-206.beta206
- Check in 206 revisions ahead of the beta release

* Thu Dec  6 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-151.beta151
- Check in 151 revisions ahead of the beta release

* Thu Nov 22 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-66.beta136
- Check in 136 revisions ahead of the beta release

* Mon Oct 29 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-50.beta95
- Check in 95 revisions ahead of the beta release

* Tue Sep 18 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-49.beta36
- Check in 36 revisions ahead of beta release
- Conditionally include collabora.inc.php per vhost on Plesk

* Mon Aug 27 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-47.beta3
- Promote to beta (3 fixes ahead of upstream)

* Sat Aug 18 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-39.alpha8
- New snapshot
- Set create_default_folders to true on Plesk

* Thu Jul 12 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-38.alpha7
- Fix unread icon
- Use bold font for folders with unread messages
- New skin thumbnail image
- Fix search scope selection

* Tue Jun  5 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-36.alpha6
- Fix toolbars in Safari desktop browser (T110373)

* Thu May 31 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-34.alpha6
- Check in pre-alpha 1.4 release with Elastic skin

* Tue May 22 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-32.alpha5
- Check in pre-alpha 1.4 release with Elastic skin

* Tue May 15 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-31.alpha4
- Check in pre-alpha 1.4 release with Elastic skin

* Mon May 14 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-16.alpha4
- Check in pre-alpha 1.4 release with Elastic skin

* Fri May  4 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-13.alpha3
- Check in pre-alpha 1.4 release with Elastic skin

* Mon Apr 30 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-12.alpha2
- Check in pre-alpha 1.4 release with Elastic skin

* Wed Apr 25 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-9.alpha1
- Check in pre-alpha 1.4 release with Elastic skin

* Tue Apr 10 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.4-8.alpha0
- Check in pre-alpha 1.4 release with Elastic skin

* Thu Apr  5 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.3.5-1
- Check in 4 revisions ahead of 1.3.5 release

* Thu Mar  8 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.3.4-3
- Check in 14 revisions ahead of 1.3.4 release

* Wed Feb 28 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.3.4-2
- Check in 12 revisions ahead of 1.3.4 release

* Sun Feb 11 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.3.4-1
- Check in upstream 1.3.4 release

* Tue Nov 14 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.3.3-2
- Stop dropping columns

* Thu Nov  9 2017 Timotheus Pokorra <tp@tbits.net> - 1.3.3-1
- Check in upstream 1.3.3 release

* Wed Oct  4 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.3.1.12-1
- Check in 12 revisions ahead of upstream 1.3.1 release

* Sun Aug 27 2017 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 1.3.0.41-1
- Check in 41 revisions ahead of upstream 1.3.0 release

* Mon Jun 19 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.2.5-6
- Fix saving preferences (timezone)
- Fix syntax error against MariaDB 10.2
- Fix assets for enigma plugin

* Thu May 25 2017 Timotheus Pokorra <tp@tbits.net> - 1.2.5-5
- avoid problems on Fedora, roundcubemail-core requires webserver but there are several available

* Wed May 10 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.2.5-2
- Fix log rotation in Plesk

* Fri Apr 28 2017 Timotheus Pokorra <tp@tbits.net> - 1.2.5-1
- Check in upstream 1.2.5 release

* Tue Apr 25 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.2.4-4
- Correct config.inc.php

* Mon Apr 24 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.2.4-2
- Include licensing.inc.php for Plesk installations

* Wed Mar 15 2017 Timotheus Pokorra <tp@tbits.net> - 1.2.4-1
- Check in upstream 1.2.4 release

* Wed Nov 30 2016 Timotheus Pokorra <tp@tbits.net> - 1.2.3-1
- Check in upstream 1.2.3 release

* Thu Sep 29 2016 Timotheus Pokorra <tp@tbits.net> - 1.2.2-1
- Check in maintenance upstream 1.2.2 release

* Wed Jul  6 2016 Jeroen van Meeuwen <vanmeeuwen@Kolabsys.com> - 1.2.0-1
- Check in the latest stable release

* Thu Jan 14 2016 Timotheus Pokorra <tp@tbits.net>
- /var/log/roundcubemail and /var/lib/roundcubemail should be owned by the webserver (#3678)
- using now the globals for those directories

* Tue Dec 22 2015 Timotheus Pokorra <tp@tbits.net>
- fix problems with upgrading, with the removed subpackages for skins

* Fri Dec 18 2015 Timotheus Pokorra <tp@tbits.net>
- fix problems with empty subpackages that occur with rpm 4.13 (#5303)
- drop some skin subpackages of plugins that are empty
- add dummy files to asset subpackages of plugins that are empty

* Fri Mar 27 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1.1.3-1
- Check in 3 revisions ahead of 1.1.1 release

* Wed Feb 25 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1.0-4
- Repack of 1.1 release branch at bbbd02bd

* Tue Feb 24 2015 Daniel Hoffend <dh@dotlan.net> - 1.1.0-3
- Fixed rewrite rules again

* Mon Feb 23 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1.0-2
- Repack of 1.1 release branch at 366ffd7a

* Sun Feb 15 2015 Daniel Hoffend <dh@dotlan.net> - - 1.1.0-2
- Remove odfviewer configuration in roundcubemail.conf

* Sat Feb 14 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1.0-1
- Final release of 1.1.0

* Wed Feb  4 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.10-git
- Ship a new GIT snapshot (09d52dbb)

* Thu Jan 29 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.10-git
- Ship a new GIT snapshot to resolve #3436 / #4431

* Wed Jan 28 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.9.git
- Require php-mysqlnd

* Fri Jan 23 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.8.git
- New snapshot release

* Wed Jan 14 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.7.git
- New snapshot release

* Fri Jan  9 2015 Timotheus Pokorra <tp@tbits.net>
- jqueryui.tagedit: backport a commit for #3912 and #4188

* Thu Jan  1 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.6.git
- New snapshot release for #4085 and various other tickets.

* Thu Aug 21 2014 Daniel Hoffend <dh@dotlan.net> - 1.1-0.5.git
- updated database upgrade process (roundcube != core)
- removed non-needed files

* Sun Aug  3 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.4.git
- New git master head snapshot
- Merge using Net_LDAP3
- Increase CSRF protection

* Tue Jun 24 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.3.git
- New git master head snapshot

* Fri Apr  4 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.2.git
- New git master head snapshot

* Fri Feb 14 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.1-0.1.git
- Current git master head snapshot

* Mon Nov 25 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.22.git
- New snapshot

* Mon Nov 11 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.21.git
- Fix the archive button

* Fri Nov  1 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.20.git
- Revert unstable list.js enhancements

* Thu Oct 31 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.19.git
- New snapshot

* Tue Oct 29 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.18.git
- Do not require httpd nor php directly

* Fri Oct 18 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.17.git
- New snapshot with many fixes and enhancements

* Sat Sep 14 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.9.git
- Fix CVE-2013-5646

* Fri Aug  9 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.7.git
- New snapshot

* Wed Jul 31 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.6.git
- New snapshot

* Tue Jun 18 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.0-0.5.git
- Now with advanced LDAP features
- Snapshot

* Thu Apr 11 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.9-0.20.rc2
- New upstream version

* Tue Jan  8 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.9-0.18.beta
- Package beta release for Roundcube 0.9

* Sun Dec 16 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.9-0.17
- Require php-gd for contact photos (0.16)
- Fix our logrotate (0.15)
- Ship latest contextmenu version (1.9)
- New snapshot (0.8 - 0.13, 0.15)
- Ship new skin as default (0.6)
- Check in latest from github/master (0.3, 0.4, 0.5)
- Use github/master instead (0.1)
- Snapshot from github/release-0.8 HEAD (0.1)

* Tue May 15 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.8-0.3.svn6135
- Package bleeding edge upstream
- Order Allow,Deny, Allow from All (#762)
- AllowOverride All (#776)

* Thu May  3 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.8-0.2.svn6135
- Correct symbolic links
- Package bleeding edge upstream

* Thu Apr 19 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7.2-1
- New upstream release
- Do not include kolab plugins - these are now a separate package

* Mon Jan 09 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7.1-1
- New upstream releases

* Fri Dec  2 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-6beta2
- Ship the latest fixes for testing purposes, in new pre-0.7 stable snapshot tarballs

* Thu Dec  1 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-2beta2
- Include Piwik Analytics plugin

* Mon Nov 28 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-1beta2
- Apply fix for #453 (terms plugin does not take into account skin_logo)

* Tue Nov 15 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-0.11beta2
- Resolve the following bugs: https://bugzilla.kolabsys.com/buglist.cgi?
  query_format=advanced&bug_status=RESOLVED&bug_status=CLOSED&product=Roundcube
  &target_milestone=0.7-beta2&target_milestone=0.7-next&target_milestone=future
- Ship upstream solution for #479 adding 'autocomplete_single' setting

* Thu Nov 10 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-0.10beta2
- Ship revision 0.10 of 0.7-beta2

* Sat Nov  5 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-0.9beta2
- Ship new snapshot version working towards 0.7-beta2, with patch for #323,
  and proposed patch for #466, #472, #473 and #479

* Tue Nov  1 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-0.8beta2
- Apply patch for parsing vlv response controls

* Sun Oct 30 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> 0.7-0.7beta2
- New beta release
- Include kolab_config plugin for configuration storage in IMAP folders and
  objects.
- Include creating default folders for Kolab Groupware related information
  in kolab_folders plugin.
- Include kolab_zpush configuration screen.
- Ship functional kolab_auth "helpdesk login" feature.

* Wed Oct 26 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-0.5beta1
- Ship zpush configuration plugin

* Thu Oct 20 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.7-0.4beta1
- 0.7 beta1 release
- Enhance use of LDAP Virtual List View controls
- Correct function use of VLV by numSubordinates, and with scope one
- Added search_only parameter for address book configuration
- ship additional plugins contextmenu, compose_addressbook, recipient_to_contact,
  and listcommands

* Thu Sep 15 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-8.rc1
- Fix permissions on enigma working directory
- Add thread_as_default plugin, enabling configuration to use 'threading'
  as the default view for mail folders, as opposed to the standard 'list'
  view.
- Correct symbolic link to enigma working directory.

* Fri Sep  9 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-6.rc1
- Ship the terms and conditions plugin

* Tue Sep  6 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-4.rc1
- Upstream roudncube.net release of release candidate 1 in the 0.6 series,
  see http://trac.roundcube.net/wiki/Changelog for changes.

* Fri Aug 26 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-3.beta3
- #369 Group of participants is displayed as one participant in the GUI (IE7)
- #368 Upload PDF as an image to a contact
- #365 event.end is null
- #357 Upload image in IE and enter
- #354 Duplicate use of tags in tagged commands, or logs entries not
  traceable per user/session
- Increase logging for memcached (part of #361)
- Increase flexibility for http_authenticate logoff event (part of #366)

* Thu Aug 18 2011 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.6-2.beta2
- New release
- Ship .htaccess file, but without some of the system settings
- Asynchronous triggering of Free/Busy
- New address book functionality
- Correct fix for illegal operand
- Rebuild with requirement for MDB2-Driver-mysqli
- Improved LDAP VLV Search/Index compatibility
- Include development on Calendar backend
- Literally remove all the external libraries
- Fix #108 configuration for Horde
- Fix ID
- Fix permission typo
- Remove Net/IDNA2 plugin
- Fix manage sieve configuration
- Split out kolab plugins

* Thu Feb 10 2011 Jon Ciesla <limb@jcomserv.net> - 0.5.1-1
- New upstream.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct 18 2010 Jon Ciesla <limb@jcomserv.net> = 0.4.2-1
- New upstream.

* Mon Oct 04 2010 Jon Ciesla <limb@jcomserv.net> = 0.4.1-1
- New upstream.

* Mon Feb 01 2010 Jon Ciesla <limb@jcomserv.net> = 0.3.1-2
- Patch to fix CVE-2010-0464, BZ 560143.

* Mon Nov 30 2009 Jon Ciesla <limb@jcomserv.net> = 0.3.1-1
- New upstream.

* Thu Oct 22 2009 Jon Ciesla <limb@jcomserv.net> = 0.3-2
- Macro fix, BZ530037.

* Wed Sep 23 2009 Jon Ciesla <limb@jcomserv.net> = 0.3-1
- New upstream.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Jon Ciesla <limb@jcomserv.net> = 0.2.2-2
- Incorporated Chris Eveleigh's config changes to fix mimetype bug, BZ 511857.

* Wed Jul 01 2009 Jon Ciesla <limb@jcomserv.net> = 0.2.2-1
- New upstream.

* Fri Apr 10 2009 Jon Ciesla <limb@jcomserv.net> = 0.2.1-1
- New upstream.

* Mon Mar 30 2009 Jon Ciesla <limb@jcomserv.net> = 0.2-9.stable
- Patch for PG until php-pear-MDB2 hits 1.5.0 stable. BZ 489505.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8.stable
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Jon Ciesla <limb@jcomserv.net> = 0.2-7.stable
- Patch for CVE-2009-0413, BZ 484052.

* Mon Jan 05 2009 Jon Ciesla <limb@jcomserv.net> = 0.2-6.stable
- New upstream.
- Dropped two most recent patches, applied upstream.

* Wed Dec 17 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-5.beta
- Security fix, BZ 476830.

* Fri Dec 12 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-4.beta
- Security fix, BZ 476223.

* Thu Oct 09 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-3.beta
- New upstream.

* Mon Jun 16 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-2.alpha
- osx files removed upstream.

* Mon Jun 16 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-1.alpha
- Fixed php-xml, php-mbstring Requires.  BZ 451652.
- Removing osx files, will be pulled from next upstream release.

* Fri Jun 13 2008 Jon Ciesla <limb@jcomserv.net> = 0.2-0.alpha
- Update to 0.2-alpha, security fixes for BZ 423271.
- mysql update and pear patches applied upstream.
- Patched config paths.

* Fri Apr 18 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-5
- Added php-pecl-Fileinfo Reqires. BZ 442728.

* Wed Apr 16 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-4
- Added mcrypt, MDB2 Requires.  BZ 442728.

* Thu Apr 10 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-3
- Patch to fix PEAR path issue, drop symlinks.

* Thu Apr 10 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-2
- Drop %%pre script that was breaking pear packages.

* Wed Apr 09 2008 Jon Ciesla <limb@jcomserv.net> = 0.1.1-1
- New upstream release.
- Added patch to fix mysql update.

* Tue Mar 18 2008 Jon Ciesla <limb@jcomserv.net> = 0.1-1
- Updgrade to 0.1 final, -dep.
- Added new mimeDecode dep.

* Mon Feb 04 2008 Jon Ciesla <limb@jcomserv.net> = 0.1-0.10rc2.1
- Changed to upstream -dep tarball, GPL-compliant.

* Fri Feb 01 2008 Jon Ciesla <limb@jcomserv.net> = 0.1-0.9rc2.1
- re-removed PEAR components that slipped back in after rc1.

* Fri Oct 26 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.8rc2
- Upgrade to 0.1-rc2

* Thu Aug 16 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.7rc1.1
- License tag correction.

* Tue Jul 03 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.6rc1.1
- New upstream release, all GPL, all current languages included.

* Mon May 14 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.5.beta2.2
- Fixed source timestamps, added Russian langpack.
- Added logpath fix to main.inc.php
- Fixed logrotate filename.

* Fri May 11 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.4.beta2.2
- Cleanup/elegantization of spec, .conf.

* Thu May 10 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.3.beta2.2
- Fixed bad chars in script.

* Thu May 10 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.2.beta2.2
- Added all langpacks.

* Thu May 10 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-0.1.beta2.2
- Versioning fix.

* Wed May 09 2007 Jon Ciesla <limb@jcomserv.net> = 0.1-beta2.3
- Fixed generation of DES.
- Cleanup re patch.

* Mon May 07 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-beta2.2.3
- Removed duplicate docs.
- Moved SQL to doc.
- Fixed perms on log dir, sysconfdir.
- Fixed Requires.
- Fixed config.
- Fixed changelog spacing.

* Fri May 04 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-beta2.2.2
- Created new source tarball with PEAR code removed. Added script for creation.

* Tue Feb 13 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-beta2.2.1
- Excluded Portions from PEAR, included as dependancies
- Fixed log/temp issues, including logrotate

* Tue Jan 30 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-beta2.2
- Initial packaging.
