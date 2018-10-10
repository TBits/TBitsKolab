<?php
    $config['calendar_driver'] = "kolab";
    $config['calendar_default_view'] = "agendaWeek";
    $config['calendar_timeslots'] = 2;
    $config['calendar_first_day'] = 1;
    $config['calendar_first_hour'] = 6;
    $config['calendar_work_start'] = 6;
    $config['calendar_work_end'] = 18;
    $config['calendar_event_coloring'] = 0;

    $config['calendar_caldav_url'] = (
        (
            array_key_exists('HTTPS', $_SERVER) &&
            !empty($_SERVER['HTTPS']) &&
            $_SERVER['HTTPS'] !== 'off'
        ) ? "https://" : "http://") .
            $_SERVER["HTTP_HOST"] . "/iRony/calendars/%u/%i/";

    $config['calendar_contact_birthdays'] = true;

    $config['kolab_invitation_calendars'] = true;

    $config['calendar_resources_driver'] = null;

    $config['calendar_resources_directory'] = array();

    if (file_exists(RCUBE_CONFIG_DIR . '/' . $_SERVER["HTTP_HOST"] . '/' . basename(__FILE__))) {
        include_once(RCUBE_CONFIG_DIR . '/' . $_SERVER["HTTP_HOST"] . '/' . basename(__FILE__));
    }
?>
