<?php
    if (file_exists(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/mattermost.inc.php')) {
        @include_once(RCUBE_CONFIG_DIR .'/'. $_SERVER['HTTP_HOST'] .'/mattermost.inc.php');
    }

