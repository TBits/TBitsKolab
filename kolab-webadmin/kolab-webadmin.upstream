%{!?php_inidir: %global php_inidir %{_sysconfdir}/php.d}

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
%global httpd_group apache
%global httpd_name httpd
%global httpd_user apache
%endif

%global _ap_sysconfdir %{_sysconfdir}/%{httpd_name}

%global kolab_user kolab
%global kolab_user_id 412
%global kolab_group kolab
%global kolab_group_id 412

%global kolabn_user kolab-n
%global kolabn_user_id 413
%global kolabn_group kolab-n
%global kolabn_group_id 413

%global kolabr_user kolab-r
%global kolabr_user_id 414
%global kolabr_group kolab-r
%global kolabr_group_id 414

Name:           kolab-webadmin
Version:        3.2.12
Release:        2%{?dist}
Summary:        Kolab Groupware Server Web Administration Interface
License:        AGPLv3+
Group:          Productivity/Office/Organizers
Url:            http://www.kolab.org

Source0:        kolab-webadmin-3.2.12.tar.gz

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

# need /usr/lib64/httpd/modules/libphp5.so for php_value in /etc/httpd/conf.d/kolab-webadmin.conf (#3678)
Requires:       php >= 5.3

%if 0%{?suse_version}
Requires:       http_daemon
Recommends:     mod_php_any
%else
Requires:       webserver
%endif

Requires:       mozldap-tools
Requires:       php-Smarty >= 3.1.7
Requires:       php-pear(HTTP_Request2)
%if 0%{?suse_version}
Requires:       php-pear-Mail
%else
Requires:       php-pear(Mail)
%endif
Requires:       php-pear(Net_Socket)
Requires:       php-pear(Net_LDAP2)
Requires:       php-kolab-net-ldap3
Requires:       php-pear(Net_SMTP)
Requires:       php-pear(Net_URL2)
Requires:       php-gettext
Requires:       php-ldap
Requires:       php-mbstring
Requires:       php-mysqlnd

%description
Web based admin - and user interface for the Kolab Groupware Server

%prep
%setup -q

for file in `find . -type f -name "*.enterprise"`; do
    if [ 0%{?kolab_enterprise} -gt 0 ]; then
        mv -v $file $(echo $file | sed -e 's/.enterprise$//g')
    else
        rm -rvf $file
    fi
done

%build

%install
mkdir -p \
    %{buildroot}/%{_datadir}/%{name}/ \
    %{buildroot}/%{_ap_sysconfdir}/conf.d/ \
    %{buildroot}/%{_var}/log/%{name} \
    %{buildroot}/%{_var}/cache/%{name}

# Remove the lib/'s we can depend on
rm -rf lib/ext/

cp -a bin %{buildroot}/%{_datadir}/%{name}/.
cp -a lib/ public_html/ hosted/ %{buildroot}/%{_datadir}/%{name}/.
cp -a doc/kolab-webadmin.conf %{buildroot}/%{_ap_sysconfdir}/conf.d/
cp -a doc/hosted-kolab.conf %{buildroot}/%{_ap_sysconfdir}/conf.d/
pushd %{buildroot}/%{_datadir}/%{name}/
ln -s ../../..%{_var}/cache/%{name} cache
ln -s ../../..%{_var}/log/%{name} logs
pushd hosted/skins/kolabsys
ln -sf ../../../public_html/skins/default/style.css style.css
ln -sf ../../../public_html/skins/default/ui.js ui.js
rm -rf images
ln -sf ../../../public_html/skins/default/images images
popd
popd

%clean
%__rm -rf %{buildroot}

%pre
# Add the kolab user and group accounts
getent group %{kolab_group} >/dev/null 2>&1 || groupadd -r %{kolab_group} -g %{kolab_group_id} >/dev/null 2>&1 || :
getent passwd %{kolab_user} >/dev/null 2>&1 || \
    useradd -r -u %{kolab_user_id} -g %{kolab_group} -d %{_localstatedir}/lib/%{kolab_user} -s /sbin/nologin \
        -c "Kolab System Account" %{kolab_user} >/dev/null 2>&1 || :

gpasswd -a %{httpd_user} kolab >/dev/null 2>&1 || :

# Previous versions of kolab-webadmin installed separate directories for public_html/ and hosted/*,
# that are now merged in to public_html/. For the sake of being able to serve up hosted/ and not
# public_html/ though, these are to be / become symbolic links.
if [ $1 -gt 1 ]; then
    if [ ! -L "/usr/share/kolab-webadmin/hosted/js" -a -d "/usr/share/kolab-webadmin/hosted/js" ]; then
        rm -rf /usr/share/kolab-webadmin/hosted/js >/dev/null 2>&1 || :
    fi

    if [ ! -L "/usr/share/kolab-webadmin/hosted/skins" -a -d "/usr/share/kolab-webadmin/hosted/skins" ]; then
        rm -rf /usr/share/kolab-webadmin/hosted/skins >/dev/null 2>&1 || :
    fi

    if [ ! -L "/usr/share/kolab-webadmin/public_html/skins/minimal/images" -a -d "/usr/share/kolab-webadmin/public_html/skins/minimal/images" ]; then
        rm -rf /usr/share/kolab-webadmin/public_html/skins/minimal/images >/dev/null 2>&1 || :
    fi
fi

%post
if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
    if [ ! -z "`grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini`" ]; then
%if 0%{?with_systemd}
        /bin/systemctl condrestart %{httpd_name}.service
%else
        /sbin/service %{httpd_name} condrestart
%endif
    fi
fi

%files
%defattr(-, root, root)
%doc doc/*
%if 0%{?suse_version}
%dir %{_ap_sysconfdir}
%dir %{_ap_sysconfdir}/conf.d
%endif
%config(noreplace) %{_ap_sysconfdir}/conf.d/%{name}.conf
%config(noreplace) %{_ap_sysconfdir}/conf.d/hosted-kolab.conf
%{_datadir}/%{name}
%attr(0770,%{httpd_user},%{httpd_group}) %{_var}/cache/%{name}
%attr(0770,%{httpd_user},%{httpd_group}) %{_var}/log/%{name}

%changelog
* Sat Dec 01 2018 Timotheus Pokorra <tp@tbits.net> - 3.2.12-2
- require php-kolab-net-ldap3 because it was upgraded in EPEL

* Fri Nov 17 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.12-1
- Release 3.2.12

* Wed Jan 13 2016 Timotheus Pokorra <tp@tbits.net> - 3.2.11-2
- requires php because libphp5.so provides php_value needed in kolab-webadmin.conf (#3678)

* Fri Mar 27 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.7-1
- Upstream release of version 3.2.7

* Thu Feb 26 2015 Daniel Hoffend <dh@dotlan.net> - 3.2.6-4
- adding default acl for domainrelated object. fixes #4731

* Wed Feb 25 2015 Daniel Hoffend <dh@dotlan.net> - 3.2.6-3
- Applied fix for get_valid_domains #4731

* Thu Feb 19 2015 Daniel Hoffend <dh@dotlan.net> - 3.2.6-2
- Feature: Autogenerated kolabtargetfolder for shared mail folders #3335

* Fri Jan 23 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.6-1
- Upstream release of version 3.2.6

* Fri Nov 28 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.5-1
- New upstream release
- Resolve #3613, #3821, #3987, #4000, #4002

* Wed Nov 19 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.4-1
- New upstream release

* Tue Nov 11 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.3-1
- New upstream release

* Fri Oct 10 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.2-1
- New upstream release

* Fri Aug 29 2014 Daniel Hoffend <dh@dotlan.net> - 3.2.1-3
- removed debugging

* Fri Aug 29 2014 Daniel Hoffend <dh@dotlan.net> - 3.2.1-2
- updated translations

* Wed Aug 20 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2.1-1
- New upstream release

* Thu Apr  3 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.2-1
- First snapshot in the new development series

* Mon Feb 17 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.5-1
- New upstream release

* Wed Jan 15 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.4-3
- Trigger rebuild for changed project configuration

* Thu Jan  9 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.4-2
- Fix typos in memcached related methods

* Tue Jan  7 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.4-1
- New upstream release

* Wed Nov 27 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.3-2
- Fix #2596, which incidentally allowed the primary address to be
  defined as a secondary address.

* Sun Nov 24 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.3-1
- New upstream version

* Fri Nov 15 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.2-1
- New upstream release
- Rebase initial sql file for object types
- Include enterprise considerations (logos, templates)

* Tue Oct 29 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.1-2
- Do not require httpd nor php directly

* Thu Oct 24 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.1-1
- New upstream release

* Fri Sep 13 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1.0-1
- New upstream release

* Fri Jul 12 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.1-0.1
- Check in today's development snapshot
- Make sure replicas and replication agreements are created when adding
  new domains

* Tue Mar 12 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.4-2
- Correct packaging provided feedback in rhbz #812526

* Tue Jan 15 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.4-1
- New upstream release

* Thu Dec 20 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.3-6

* Thu Nov 29 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.3-5
- Ship fix for not being able to add a domain
- Attempt to correct the removal of directories that are now symbolic links

* Mon Nov 26 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.3-3
- Fix replacing directory by symbolic link (Fix typo)
- New upstream version

* Tue Sep 18 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.2-3
- Allow a setting to control whether hosted domain aliases are shown
- Fix symbolic links introduced by patch
- New upstream release

* Tue Sep  4 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.1-1
- New upstream release

* Sun Aug 12 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0.0-1
- New upstream release

* Mon Jul 30 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0-0.3
- Add apache user to kolab group for read permissions on configuration

* Wed Jul 11 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 3.0-0.2
- Development snapshot version for Kolab 3.0

* Fri May 18 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.2-1
- New upstream release

* Fri May 11 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.1-1
- New upstream release

* Tue May  8 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.0-5
- Also require php-pear(Net_LDAP2)

* Thu May  3 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.0-4
- Ship some very nice patches

* Thu Apr 12 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.0-3
- Re-packaged sources
- Require mozldap-tools

* Thu Apr 12 2012 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.4.0-2
- Re-packaged sources
- First release of the new Kolab Web Admin
