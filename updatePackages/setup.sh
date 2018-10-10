#!/bin/bash

# create new package instructions

CURRENTPATH=`pwd`
PATCHESPATH=~/tmp/KolabScripts/kolab/patches
TBITSPATCHESPATH=~/tmp/lbs-TBitsKolab/updatePackages
TBITSSCRIPTSPATH=~/tmp/KolabUpgradeScripts
OBSPATH=~/tmp/lbs-kolab
RELEASE=103

obsbranch="Kolab_16"
patchesbranch="Kolab16"
branch="TBitsKolab16Test"

if [[ "`whoami`" == "root" ]]
then
  yum -y install git || exit -1
fi

mkdir -p ~/tmp

# get the TBits patches
#  eg https://github.com/TBits/KolabScripts/tree/Kolab16/kolab/patches
if [ -d ~/tmp/KolabScripts ]
then
  cd ~/tmp/KolabScripts
  git pull || exit -1
else
  cd ~/tmp
  git clone --depth 1 -b $patchesbranch https://github.com/TBits/KolabScripts.git || exit -1
fi

if [ -d ~/tmp/lbs-TBitsKolab ]
then
  cd ~/tmp/lbs-TBitsKolab
  git pull || exit -1
else
  cd ~/tmp
  git clone --depth 1 -b $branch https://github.com/TBits/lbs-TBitsKolab.git || exit -1
fi

mkdir -p ~/tmp/lbs-TBitsKolab/updatePackages
cp -R $CURRENTPATH/* ~/tmp/lbs-TBitsKolab/updatePackages

if [ -d ~/tmp/ude_login ]
then
  cd ~/tmp/ude_login
  git pull || exit -1
else
  cd ~/tmp
  git clone --depth 1 https://github.com/TBits/ude_login.git || exit -1
fi

# get the latest src package from Kolab OBS. they get synched to Github every night
if [ -d ~/tmp/lbs-kolab ]
then
  cd ~/tmp/lbs-kolab
  git reset --hard
  git clean -f -d
  git checkout $obsbranch
  git pull || exit -1
else
  cd ~/tmp
  git clone --depth 15 -b $obsbranch https://github.com/TBits/lbs-kolab.git || exit -1
fi
# wir wollen im Moment auf einer Version von Oktober 2018 bleiben
#cd ~/tmp/lbs-kolab
#git checkout 2b424088cd8cf6b3b00f5e1219cde8cc4f8b8a05 || exit -1
#cd -
# wir wollen im Moment auf der Version von März 2018 bleiben
cd ~/tmp/lbs-kolab
git checkout a4531e980e276e7721f71c1620333d8fd7956e77 || exit -1
cd -

unmodified_pkgnames=( libcalendaring libkolabxml libkolab kolab-utils python-sievelib python-icalendar php-kolab-net-ldap3 mozldap roundcubemail-skin-chameleon roundcubemail-plugin-contextmenu php-sabre-vobject php-sabre-http php-sabre-dav php-sabre-event kolab-freebusy php-endroid-qrcode php-enygma-yubikey php-spomky-labs-otphp php-christianriesen-base32 kolab-syncroton chwala iRony kolab-schema kolab-autoconf )

for pkgname in "${unmodified_pkgnames[@]}"
do
    rm -Rf ~/tmp/lbs-TBitsKolab/$pkgname/*
    mkdir -p ~/tmp/lbs-TBitsKolab/$pkgname
    cp -R $OBSPATH/$pkgname ~/tmp/lbs-TBitsKolab/
    rm -Rf ~/tmp/lbs-TBitsKolab/$pkgname/debian
    rm -f ~/tmp/lbs-TBitsKolab/$pkgname/*.dsc
done

modified_pkgnames=( pykolab kolab-webadmin roundcubemail-plugins-kolab roundcubemail kolab cyrus-imapd )

for pkgname in "${modified_pkgnames[@]}"
do
    cd $OBSPATH/$pkgname

    # sometimes new files are added in master, which we have to add in the spec file, eg. roundcubemail-plugins-kolab
    if [ -f $TBITSPATCHESPATH/$pkgname.patch ]
    then
      patch -p1 < $TBITSPATCHESPATH/$pkgname.patch || exit -1
    fi

    if [[ "$pkgname" == "kolab-webadmin" ]]
    then
      # from initMultiDomain.sh
      cp $PATCHESPATH/validateAliasDomainPostfixVirtualFileBug2658.patch .
      cp $PATCHESPATH/canonification_via_uid_wap.patch .
      
      # from initTBitsISP.sh
      cp $PATCHESPATH/patchMultiDomainAdminsBug2018.patch .
      cp $PATCHESPATH/domainquotaBug2046.patch .
      cp $PATCHESPATH/domainAdminDefaultQuota.patch .
      cp $PATCHESPATH/domainAdminMaxAccounts.patch .
      cp $PATCHESPATH/lastLoginTBitsAttribute-wap.patch .
      cp $PATCHESPATH/quotaused_wap.patch .
      cp $PATCHESPATH/listUsersLastLoginQuotaUsage.patch .
      cp $PATCHESPATH/wap_api_listuserswithhash.patch .
      cp $PATCHESPATH/intranetToken-wap.patch .

      cp $PATCHESPATH/wap_disallow_users.patch .
      cp $PATCHESPATH/dont_generate_attribs_when_editing.patch .

      cp $PATCHESPATH/../initTBitsUserTypes.php .
      cp $PATCHESPATH/99tbits.ldif .
    fi

    if [[ "$pkgname" == "pykolab" ]]
    then
      # from initSetupKolabPatches.sh
      cp $PATCHESPATH/fixPykolabIMAPKeepAlive.patch .
      cp $PATCHESPATH/pykolab_do_not_rename_existing_mailbox_T3315.patch .
      cp $PATCHESPATH/pykolab_wap_client_unverified_context_localhost.patch .
      cp $PATCHESPATH/kolab_lam_invalid_mailbox_name.patch .
 
      # from initMultiDomain.sh
      cp $PATCHESPATH/canonification_via_uid_pykolab.patch .

      # from disableSpamFilter.sh
      cp $PATCHESPATH/disableSpamFilter.patch .
      cp $PATCHESPATH/disableSpamFilter2.patch .

      # from initTBitsISP.sh
      cp $PATCHESPATH/lastLoginTBitsAttribute-pykolab.patch .
      cp $PATCHESPATH/allowPrimaryEmailAddressFromDomain.patch .
      cp $PATCHESPATH/logLoginData.patch .

      # from initTBitsCustomizationsDE.sh
      cp $PATCHESPATH/onlyAllowKolabUsersToAuthViaSasl.patch .
    fi

    if [[ "$pkgname" == "roundcubemail-plugins-kolab" ]]
    then
      # from initSetupKolabPatches.sh
      cp $PATCHESPATH/roundcubeStorageMariadbBug4883.patch .
      cp $PATCHESPATH/roundcube_calendar_etc_timezone_T2666.patch .

      # from initMultiDomain.sh
      cp $PATCHESPATH/canonification_via_uid_roundcube.patch .

      # add the ude_login plugin
      cp ~/tmp/ude_login/ude_login.php .
      cp ~/tmp/ude_login/ude_login.inc.php .
    fi

    if [[ "$pkgname" == "roundcubemail" ]]
    then
      # from initTBitsISP.sh
      cp $PATCHESPATH/optional_disable_addressbook_export.patch .

      cp $TBITSPATCHESPATH/backport_managesieve_forwards.patch .
    fi

    if [[ "$pkgname" == "cyrus-imapd" ]]
    then
      cp $PATCHESPATH/cyrus_canonification_multiple_domains.patch .
      cp $PATCHESPATH/cyrus_filter_kolab_mailboxes.patch .
    fi

    if [[ "$pkgname" == "tbits-kolab-scripts" ]]
    then
      cp $TBITSSCRIPTSPATH/refresh_quota_sieve/kolab_refresh_quota_and_sieve.config.php .
      cp $TBITSSCRIPTSPATH/refresh_quota_sieve/kolab_refresh_quota_and_sieve.php .
      cp $TBITSSCRIPTSPATH/import/importKolabWeiterleitungen.php .
      cp $TBITSSCRIPTSPATH/backup/backup.sh .
    fi

    # Adjust spec file for customized builds
    sed -i "s#Release:.*#Release:        $RELEASE.tbits%(date +%%Y%%m%%d)%{?dist}#g" $pkgname.spec

    # for logging the differences
    # git status
    # git diff | cat

    rm -Rf ~/tmp/lbs-TBitsKolab/$pkgname/*
    mkdir -p ~/tmp/lbs-TBitsKolab/$pkgname
    cp -R $OBSPATH/$pkgname ~/tmp/lbs-TBitsKolab/
    rm -Rf ~/tmp/lbs-TBitsKolab/$pkgname/debian
    rm -f ~/tmp/lbs-TBitsKolab/$pkgname/*.dsc
done

cd ~/tmp/lbs-TBitsKolab
find . -type f -name "*.orig" -delete
git add  --all .
git config --global user.name "LBS BuildBot"
git config --global user.email tp@tbits.net

# only commit if there is actually something new
git diff-index --quiet HEAD || git commit -a -m "latest build for TBits" || exit -1

#git push || exit -1
