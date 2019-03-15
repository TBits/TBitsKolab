<?php
    require_once('sdk.php');

    pm_Context::init('kolab');

    $fm = new \pm_ServerFileManager();

    $str = "";

    // Get the contents of premium.inc.php from the extension.
    if ($fm->fileExists(rtrim(pm_Context::getVarDir(), '/') . '/webmail/premium.inc.php')) {
        $str = $fm->getFileContents(
            rtrim(pm_Context::getVarDir(), '/') . '/webmail/premium.inc.php'
        );

    // Get the contents of premium.inc.php from the software package.
    } elseif ('/etc/roundcubemail/premium.inc.php') {
        $str = $fm->getFileContents('/etc/roundcubemail/premium.inc.php');
    } else {
        return FALSE;
    }

    foreach (pm_Domain::getAllDomains() as $domain) {
        if ($domain->hasPermission("manage_kolab") && $domain->hasHosting()) {
            $w_domain    = 'webmail.' . $domain_name;

            if ($domain->hasPermission('manage_kolab')) {
                if (!$fm->fileExists("/etc/roundcubemail/{$w_domain}/")) {
                    $fm->mkdir("/etc/roundcubemail/{$w_domain}/", '0755');
                }

                $fm->filePutContents("/etc/roundcubemail/{$w_domain}/premium.inc.php", $str);
            }
        }
    }
}
