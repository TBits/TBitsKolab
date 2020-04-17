#!/bin/bash

# create new package instructions

RELEASE=108
obsbranch="Kolab_16"
patchesbranch="Kolab16"
branch="TBitsKolab16Dev"

# version from 31 March 2019
githash=0ff781639ce63d038edaacfa41b5be1530e34c20
# version from July 2018
#githash_roundcubemail=4b631825f9afcfae3be3a806e2d31da3ee63180c
#githash_roundcubemail_plugins_kolab=$githash_roundcubemail
#githash_roundcubemail_skin_chameleon=$githash_roundcubemail
#githash_roundcubemail_plugin_contextmenu=$githash_roundcubemail

TBITSPATCHESPATH=~/tmp/lbs-$branch/updatePackages
PATCHESPATH=~/tmp/KolabScripts/kolab/patches
TBITSSCRIPTSPATH=~/tmp/KolabUpgradeScripts
OBSPATH=~/tmp/lbs-kolab
CURRENTPATH=`pwd`

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

if [ -d ~/tmp/lbs-$branch ]
then
  cd ~/tmp/lbs-$branch
  git pull || exit -1
else
  cd ~/tmp
  git clone --depth 1 -b $branch https://github.com/TBits/lbs-TBitsKolab.git lbs-$branch || exit -1
fi

rm -Rf ~/tmp/lbs-$branch/updatePackages
mkdir -p ~/tmp/lbs-$branch/updatePackages
cp -R $CURRENTPATH/* ~/tmp/lbs-$branch/updatePackages

if [ -d ~/tmp/ude_login ]
then
  cd ~/tmp/ude_login
  git pull || exit -1
else
  cd ~/tmp
  git clone --depth 1 https://github.com/TBits/ude_login.git || exit -1
fi
ude_login_version=4.0.0
mkdir -p ~/tmp/roundcubemail-plugin-ude_login-$ude_login_version/plugins/ude_login
cp ~/tmp/ude_login/* ~/tmp/roundcubemail-plugin-ude_login-$ude_login_version/plugins/ude_login
cd ~/tmp/roundcubemail-plugin-ude_login-$ude_login_version/plugins/ude_login
mv ude_login.inc.php config.inc.php.dist
cd ~/tmp; tar czf roundcubemail-plugin-ude_login-$ude_login_version.tar.gz roundcubemail-plugin-ude_login-$ude_login_version

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
  git clone --depth 25 -b $obsbranch https://github.com/TBits/lbs-kolab.git || exit -1
fi

# for the moment lets stay on a defined version
cd ~/tmp/lbs-kolab
git checkout $githash || exit -1
cd -

unmodified_pkgnames=( libcalendaring libkolabxml libkolab kolab-utils python-sievelib python-icalendar mozldap roundcubemail-skin-chameleon php-sabre-vobject php-sabre-http php-sabre-dav php-sabre-event php-endroid-qrcode php-enygma-yubikey php-spomky-labs-otphp php-christianriesen-base32 kolab-syncroton chwala iRony kolab-schema )

for pkgname in "${unmodified_pkgnames[@]}"
do
    echo "working on $pkgname"
    rm -Rf ~/tmp/lbs-$branch/$pkgname/*
    mkdir -p ~/tmp/lbs-$branch/$pkgname
    cp -R $OBSPATH/$pkgname ~/tmp/lbs-$branch/
    rm -Rf ~/tmp/lbs-$branch/$pkgname/debian
    rm -f ~/tmp/lbs-$branch/$pkgname/*.dsc
done

modified_pkgnames=( pykolab kolab-webadmin roundcubemail-plugin-contextmenu roundcubemail-plugins-kolab roundcubemail-plugin-ude_login roundcubemail kolab cyrus-imapd kolab-autoconf kolab-freebusy )

for pkgname in "${modified_pkgnames[@]}"
do
    echo "working on modified $pkgname"
    mkdir -p $OBSPATH/$pkgname
    cd $OBSPATH/$pkgname

    git reset --hard
    pkggithash="githash_"${pkgname//-/_}
    if [[ ! -z "${!pkggithash}" ]]
    then
      echo "getting special git version for package $pkgname"
      git checkout ${!pkggithash} || exit -1
    else
      git checkout $githash || exit -1
    fi

    # sometimes new files are added in master, which we have to add in the spec file, eg. roundcubemail-plugins-kolab
    if [ -f $TBITSPATCHESPATH/$pkgname.patch ]
    then
      cp $pkgname.spec $pkgname.upstream
      patch -p1 < $TBITSPATCHESPATH/$pkgname.patch || exit -1
    fi

    # we need a new tarball for roundcubemail, but not beta
    if ls $TBITSPATCHESPATH/$pkgname*.tar.gz 1> /dev/null 2>&1;
    then
      rm $pkgname*.tar.gz
      cp $TBITSPATCHESPATH/$pkgname*.tar.gz .
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

      # template for cyrus.conf without guam
      cp $TBITSPATCHESPATH/pykolab_no_guam.patch .
    fi

    if [[ "$pkgname" == "roundcubemail-plugins-kolab" ]]
    then
      # from initSetupKolabPatches.sh
      cp $PATCHESPATH/roundcubeStorageMariadbBug4883.patch .
      cp $PATCHESPATH/roundcube_calendar_etc_timezone_T2666.patch .

      # from initMultiDomain.sh
      cp $PATCHESPATH/canonification_via_uid_roundcube.patch .
    fi

    if [[ "$pkgname" == "roundcubemail-plugin-ude_login" ]]
    then
      cp $TBITSPATCHESPATH/comm.py .
      cp ~/tmp/lbs-$branch/$pkgname/*.spec .
      cp ~/tmp/lbs-$branch/$pkgname/*.tar.gz .
      if [ ! -f roundcubemail-plugin-ude_login-$ude_login_version.tar.gz ]
      then
        rm -f *.tar.gz
        cp ~/tmp/roundcubemail-plugin-ude_login-$ude_login_version.tar.gz .
      fi
    fi

    if [[ "$pkgname" == "roundcubemail" ]]
    then
      # from initTBitsISP.sh
      cp $PATCHESPATH/optional_disable_addressbook_export.patch .
    fi

    if [[ "$pkgname" == "cyrus-imapd" ]]
    then
      cp $PATCHESPATH/cyrus_filter_kolab_mailboxes.patch .
    fi

    # Adjust spec file for customized builds
    sed -i "s#Release:.*#Release:        $RELEASE.tbits%(date +%%Y%%m%%d)%{?dist}#g" $pkgname.spec

    # for logging the differences
    # git status
    # git diff | cat

    rm -Rf ~/tmp/lbs-$branch/$pkgname/*
    mkdir -p ~/tmp/lbs-$branch/$pkgname
    cp -R $OBSPATH/$pkgname ~/tmp/lbs-$branch/
    rm -Rf ~/tmp/lbs-$branch/$pkgname/debian
    rm -f ~/tmp/lbs-$branch/$pkgname/*.dsc
done

cd ~/tmp/lbs-$branch
find . -type f -name "*.orig" -delete
git add  --all .
git config --local user.name "LBS BuildBot"
git config --local user.email tp@tbits.net

cd updatePackages
./checkVersions.sh > ../packages.txt
cd -

# only commit if there is actually something new
git diff-index --quiet HEAD || git commit -a -m "latest build for TBits" || exit -1

git push || exit -1
