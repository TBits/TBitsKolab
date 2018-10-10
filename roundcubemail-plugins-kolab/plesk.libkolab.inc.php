<?php

    /*
        Managed by Puppet
     */

    $config['kolab_freebusy_server'] = 'https://freebusy.kolabsys.com/';

    if (file_exists(RCUBE_CONFIG_DIR . '/' . $_SERVER["HTTP_HOST"] . '/' . basename(__FILE__))) {
        include_once(RCUBE_CONFIG_DIR . '/' . $_SERVER["HTTP_HOST"] . '/' . basename(__FILE__));
    }

    $config['kolab_cache'] = true;

    $config['kolab_ssl_verify_host'] = false;
    $config['kolab_ssl_verify_peer'] = false;

    $config['kolab_use_subscriptions'] = true;

    $config['kolab_skip_namespace'] = Array();

    $config['kolab_messages_cache_bypass'] = 2;

?>
