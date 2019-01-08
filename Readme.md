Disclaimer
==========

We provide adjusted packages of Kolab for use by TBits.net.

We recommend to use the official packages from Kolab Systems!

Differences
===========

We applied the patches available at https://github.com/tbits/kolabscripts

We drop guam, because we have patched Cyrus to show the same behaviour, hiding Kolab specific folders from other clients.

We drop amavis and clamav, because we have a separate server for filtering Spam at TBits.net.

We use a stable version of Roundcube, not a beta version.

Installation
============

This is for CentOS 7:

```
export branch=Kolab16
export repo=https://lbs.solidcharity.com/repos/tbits.net/TBitsKolab16Test/centos/7/lbs-tbits.net-TBitsKolab16Test.repo
export WITHOUTSPAMFILTER=1
export APPLYPATCHES=0
export dirmanagerpwd=test

yum -y install epel-release wget which bzip2 selinux-policy-targeted
sed -i 's/enforcing/permissive/g' /etc/selinux/config
wget -nv --tries=3 -O $branch.tar.gz https://github.com/TBits/KolabScripts/archive/$branch.tar.gz
tar xzf $branch.tar.gz
cd KolabScripts-$branch/kolab
echo "y" | ./reinstall.sh
./initSetupKolabPatches.sh
setup-kolab --default --mysqlserver=new --timezone=Europe/Berlin --directory-manager-pwd=$dirmanagerpwd
h=`hostname`

either
./initSSL.sh ${h:`expr index $h .`}
or
./initHttpTunnel.sh

./disableGuam.sh
./initMultiDomain.sh
./initMailForward.sh
./initMailCatchall.sh
for d in /etc/dirsrv/slapd*
do
  cp patches/99tbits.ldif $d/schema/
done
./initTBitsISP.sh
```
