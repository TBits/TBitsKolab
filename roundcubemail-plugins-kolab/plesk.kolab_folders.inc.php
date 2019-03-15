<?php

// Default kolab-specific folders. Set values to non-empty
// strings to create default folders of apropriate type.
// If there is no default folder with specified type in user mailbox,
// it will be created.
// Note: Mail folders will be also subscribed.

// Default Configuration folder
$config['kolab_folders_configuration_default'] = 'Configuration';
// Default Calendar folder
$config['kolab_folders_event_default'] = 'Calendar';
// Default Contacts (Addressbook) folder
$config['kolab_folders_contact_default'] = 'Contacts';
// Default Tasks folder
$config['kolab_folders_task_default'] = 'Tasks';
// Default Notes folder
$config['kolab_folders_note_default'] = 'Notes';
// Default Journal folder
$config['kolab_folders_journal_default'] = 'Journal';
// Default Files folder
$config['kolab_folders_file_default'] = 'Files';
// Default FreeBusy folder
$config['kolab_folders_freebusy_default'] = 'Freebusy';

// INBOX folder
$config['kolab_folders_mail_inbox'] = 'INBOX';
// Drafts folder
$config['kolab_folders_mail_drafts'] = 'Drafts';
// Sent folder
$config['kolab_folders_mail_sentitems'] = 'Sent';
// Trash folder
$config['kolab_folders_mail_wastebasket'] = 'Trash';
// Others folders
$config['kolab_folders_mail_outbox'] = '';
$config['kolab_folders_mail_junkemail'] = 'INBOX.Spam';
