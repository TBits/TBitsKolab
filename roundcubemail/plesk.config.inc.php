<?php
    include_once("/usr/share/psa-roundcube/config/config.inc.php");

    $components = explode('.', $_SERVER["HTTP_HOST"]);

    if (count($components) > 2) {
        array_shift($components);
    }

    $domain = implode('.', $components);

    $config['session_domain'] = $_SERVER["HTTP_HOST"];
    $config['username_domain'] = $domain;

    $config['support_url'] = "https://www.plesk.com/support/";

    $config['product_name'] = "Plesk Premium Mail, powered by Kolab";

    $config['default_host'] = "localhost";
    $config['default_port'] = 9143;

    $config['smtp_server'] = "localhost";
    $config['smtp_port'] = 25;
    $config['smtp_user'] = '%u';
    $config['smtp_pass'] = '%p';
    $config['smtp_helo_host'] = $_SERVER["HTTP_HOST"];

    $config['use_secure_urls'] = true;
    $config['force_https'] = true;

    $config['assets_path'] = "/assets/";

    $config['assets_dir'] = "/usr/share/roundcubemail/public_html/assets/";

    $config['imap_cache'] = "db";
    $config['imap_cache_ttl'] = "10d";

    $config['message_cache'] = null;

    $config['session_storage'] = "db";

    $config['skin'] = "plesk";

    $config['auto_create_user'] = true;

    $config['enable_installer'] = false;

    $config['plugins'] = Array(
            'acl',
            'archive',
            'calendar',
            'jqueryui',
            'kolab_activesync',
            'kolab_addressbook',
            'kolab_config',
            //'kolab_delegation',
            'kolab_files',
            'kolab_folders',
            'kolab_notes',
            'kolab_tags',
            'libkolab',
            'libcalendaring',
            'managesieve',
            'markasjunk',
            'newmail_notifier',
            'odfviewer',
            'password',
            'pdfviewer',
            'tasklist',
            'contextmenu',
        );

    $config['kolabdav_plugins'] = Array(
            'libcalendaring',
            'libkolab'
        );

    $config['skip_deleted'] = true;

    $config['read_when_deleted'] = true;
    $config['flag_for_deletion'] = true;
    $config['delete_always'] = true;

    $config['session_lifetime'] = 180;
    $config['password_charset'] = 'UTF-8';
    $config['useragent'] = 'Kolab 16/Roundcube ' . RCUBE_VERSION;
    $config['refresh_interval'] = 300;
    $config['check_all_folders'] = false;
    $config['dont_override'] = Array(
            'check_all_folders',
            'refresh_interval',
            'skin'
        );

    $config['message_sort_col'] = 'date';
    $config['default_list_mode'] = 'threads';
    $config['autoexpand_threads'] = 2;

    $config['message_sort_col'] = 'date';
    $config['default_list_mode'] = 'threads';
    $config['autoexpand_threads'] = 2;

    $config['spellcheck_engine'] = 'pspell';
    $config['spellcheck_dictionary'] = true;
    $config['spellcheck_ignore_caps'] = true;
    $config['spellcheck_ignore_nums'] = true;
    $config['spellcheck_ignore_syms'] = true;
    $config['spellcheck_languages'] = array(
            'da' => 'Dansk',
            'de' => 'Deutsch',
            'en' => 'English',
            'es' => 'Español',
            'fr' => 'Français',
            'it' => 'Italiano',
            'nl' => 'Nederlands',
            'pt' => 'Português',
            'ru' => 'Русский',
            'sv' => 'Svenska'
        );

    $config['undo_timeout'] = 10;
    $config['upload_progress'] = 2;
    $config['address_template'] = '{street}<br/>{locality} {zipcode}<br/>{country} {region}';
    $config['preview_pane'] = true;
    $config['preview_pane_mark_read'] = 0;

    // Bottom posting for reply mode
    $config['reply_mode'] = 0;
    $config['sig_above'] = false;
    $config['mdn_requests'] = 0;
    $config['mdn_default'] = false;
    $config['dsn_default'] = false;
    $config['reply_same_folder'] = false;

    $config['performance_stats'] = true;

    $config['archive_mbox'] = 'Archive';
    $config['drafts_mbox'] = 'Drafts';
    $config['junk_mbox'] = 'INBOX.Spam';
    $config['sent_mbox'] = 'Sent';
    $config['trash_mbox'] = 'Trash';

    $config['create_default_folders'] = true;
    $config['protect_default_folders'] = true;

    $config['default_folders'] = Array(
        'INBOX',
        'Archive',
        'Drafts',
        'Sent',
        'INBOX.Spam',
        'Trash'
    );

    $config['skin_include_php'] = false;
    $config['mime_magic'] = null;
    $config['im_identify_path'] = '/usr/bin/identify';
    $config['im_convert_path'] = '/usr/bin/convert';
    $config['log_dir'] = 'logs/';
    $config['temp_dir'] = '/tmp';

    $config['log_driver'] = 'file';
    $config['log_date_format'] = 'Y-M-d H:i:s O';
    $config['syslog_id'] = 'roundcube';
    $config['syslog_facility'] = LOG_USER;
    $config['smtp_log'] = true;
    $config['log_logins'] = true;
    $config['log_session'] = true;
    $config['debug_level'] = 1;
    $config['devel_mode'] = false;
    $config['sql_debug'] = false;
    $config['memcache_debug'] = false;
    $config['imap_debug'] = false;
    $config['ldap_debug'] = false;
    $config['smtp_debug'] = false;

    $config['fileapi_backend'] = "kolab";
    $config['fileapi_plugins'] = Array('kolab_folders');
    $config['fileapi_manticore'] = false;
    $config['fileapi_wopi_office'] = false;

    $config['imap_conn_options'] = Array(
        'ssl' => Array(
            'verify_peer' => FALSE,
            'verify_peer_name' => FALSE
        )
    );

    $config['smtp_conn_options'] = Array(
        'ssl' => Array(
            'verify_peer' => FALSE,
            'verify_peer_name' => FALSE
        )
    );

    @include('/etc/roundcubemail/kolab_syncroton.inc.php');

    if (file_exists(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/'. basename(__FILE__))) {
        @include_once(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/'. basename(__FILE__));
    }

    // Additional options for Plesk Premium Email - Free
    if (file_exists(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/freemium.inc.php')) {
        @include_once(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/freemium.inc.php');
    }

    // Integration between Plesk Premium Email and Collabora Online extensions
    if (file_exists(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/collabora.inc.php')) {
        @include_once(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/collabora.inc.php');
    }

    // Integration between Plesk Premium Email and Mattermost extensions
    if (file_exists(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/mattermost.inc.php')) {
        @include_once(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/mattermost.inc.php');
    }

    // Integration between Plesk Premium Email and Seafile extensions
    if (file_exists(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/seafile.inc.php')) {
        @include_once(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/seafile.inc.php');
    }

    @include('/etc/roundcubemail/licensing.inc.php');
