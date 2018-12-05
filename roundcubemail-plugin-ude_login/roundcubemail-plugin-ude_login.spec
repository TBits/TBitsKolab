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
%if 0%{?plesk}
%global httpd_group roundcube_sysgroup
%global httpd_name httpd
%global httpd_user roundcube_sysuser
%else
%global httpd_group apache
%global httpd_name httpd
%global httpd_user apache
%endif
%endif

%global roundcube_version 1.2
%global datadir %{_datadir}/roundcubemail
%global plugindir %{datadir}/plugins
%global confdir %{_sysconfdir}/roundcubemail
%global tmpdir %{_var}/lib/roundcubemail

Name:           roundcubemail-plugin-ude_login
Version:        4.0.0
Release:        106.tbits%(date +%%Y%%m%%d)%{?dist}
Summary:        Plugin ude_login for Roundcube

Group:          Applications/Internet
License:        AGPLv3+ and GPLv3+
URL:            http://www.kolab.org

Source0:        %{name}-%{version}.tar.gz
Source1:        comm.py

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

BuildRequires:  composer

%if "%{_arch}" != "ppc64" && "%{_arch}" != "ppc64le" && 0%{?suse_version} < 1
BuildRequires:  python-cssmin
BuildRequires:  uglify-js
%else
BuildRequires:  roundcubemail(core)
%endif

BuildRequires:  python

Requires:       php-kolabformat >= 1.0
Requires:       php-kolab >= 0.5
Requires:       php-pear(HTTP_Request2)
%if 0%{?plesk} < 1
Requires:       php-kolab-net-ldap3
%endif
Requires:       php-pear(Mail_Mime) >= 1.8.5
Requires:       roundcubemail >= %{roundcube_version}

Requires:       roundcubemail(core) >= %{roundcube_version}
Requires:       roundcubemail(plugin-ude_login-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(plugin-ude_login-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-ude_login) = %{?epoch:%{epoch}:}%{version}-%{release}

%description
A plugin for managing permissions per user or per domain for Roundcube

%package -n roundcubemail-plugin-ude_login-assets
Summary:        Plugin ude_login Assets
Group:          Applications/Internet
Provides:       roundcubemail(plugin-ude_login-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-ude_login-assets
Plugin ude_login Assets

%package -n roundcubemail-plugin-ude_login-skin-larry
Summary:        Plugin ude_login / Skin larry
Group:          Applications/Internet
Requires:       roundcubemail(plugin-ude_login) = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-larry) >= %{roundcube_version}
Requires:       roundcubemail(plugin-ude_login-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-ude_login-skin) = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       roundcubemail(plugin-ude_login-skin-larry) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-ude_login-skin-larry
Plugin ude_login / Skin larry

%package -n roundcubemail-plugin-ude_login-skin-larry-assets
Summary:        Plugin ude_login / Skin larry (Assets)
Group:          Applications/Internet
Provides:       roundcubemail(plugin-ude_login-skin-larry-assets) = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n roundcubemail-plugin-ude_login-skin-larry-assets
Plugin ude_login / Skin larry (Assets Package)

%prep
%setup -q -c %{name}-%{version}
rm %{name}-%{version}/plugins/ude_login/users.txt
rm %{name}-%{version}/plugins/ude_login/composer.json

for plugin in $(find %{name}-%{version}/plugins -mindepth 1 -maxdepth 1 -type d | sort); do
    target_dir=$(echo ${plugin} | %{__sed} -e "s|%{name}-%{version}|%{name}-plugin-$(basename ${plugin})-%{version}|g")
    %{__mkdir_p} $(dirname ${target_dir})
    cp -av ${plugin} ${target_dir}

    (
        echo "%package -n roundcubemail-plugin-$(basename ${plugin})"
        echo "Summary:        Plugin $(basename ${plugin})"
        echo "Group:          Applications/Internet"
        echo "Requires:       roundcubemail(core) >= %%{roundcube_version}"
        echo "Requires:       roundcubemail(plugin-$(basename ${plugin})-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        if [ -d "${plugin}/skins/" ]; then
            echo "Requires:       roundcubemail(plugin-$(basename ${plugin})-skin) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        fi

        for rplugin in $(grep -rn "require_plugin" ${plugin}/ | cut -d"'" -f2 | sort); do
            if [ -d "%{name}-%{version}/plugins/${rplugin}" ]; then
                echo "Requires:       roundcubemail(plugin-${rplugin}) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
            else
                echo "Requires:       roundcubemail(plugin-${rplugin}) >= %%{roundcube_version}"
            fi
        done

        if [ "$(basename ${plugin})" == "kolab_files" ]; then
            echo "Requires:       php-curl"
        elif [ "$(basename ${plugin})" == "kolab_2fa" ]; then
            echo "Requires:       php-endroid-qrcode"
            echo "Requires:       php-enygma-yubikey"
            echo "Requires:       php-spomky-labs-otphp"
        elif [ "$(basename ${plugin})" == "html_converter" ]; then
            echo "Requires:       lynx"
        fi

        echo "Provides:       roundcubemail(plugin-$(basename ${plugin})) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo ""
        echo "%description -n roundcubemail-plugin-$(basename ${plugin})"
        echo "Plugin $(basename ${plugin})"
        echo ""
    ) >> plugins.packages

    (
        echo "%files -f plugin-$(basename ${plugin}).files"
        echo "%defattr(-,root,root,-)"
        if [ -d "${plugin}/config" -o -f "${plugin}/config.inc.php" -o -f "${plugin}/config.inc.php.dist" ]; then
            echo "%attr(0640,root,%%{httpd_group}) %config(noreplace) %%{_sysconfdir}/roundcubemail/$(basename ${plugin}).inc.php"
        fi
        echo ""
    ) >> plugins.files

    touch plugins.pre
    (
        echo "%pre -n roundcubemail-plugin-$(basename ${plugin})"
        echo "if [ -f \"%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted\" ]; then"
        echo "    %%{__rm} -f \"%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted\""
        echo "fi"
        echo ""
    ) >> plugins.pre

    touch plugins.post
    (
        echo "%posttrans -n roundcubemail-plugin-$(basename ${plugin})"
        echo "if [ ! -f \"%%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted\" ]; then"
        echo "    if [ -f \"%%{php_inidir}/apc.ini\"  -o -f \"%%{php_inidir}/apcu.ini\" ]; then"
        echo "        if [ ! -z \"\$(grep ^apc.enabled=1 %%{php_inidir}/apc{,u}.ini 2>/dev/null)\" ]; then"
        echo "%if 0%%{?with_systemd}"
        echo "            /bin/systemctl condrestart %%{httpd_name}.service"
        echo "%else"
        echo "            /sbin/service %%{httpd_name} condrestart"
        echo "%endif"
        echo "        fi"
        echo "    fi"
        echo "    %%{__mkdir_p} %%{_localstatedir}/lib/rpm-state/roundcubemail/"
        echo "    touch %%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
        echo "fi"
        echo ""
        if [ ! -z "$(find ${plugin} -type d -name SQL)" ]; then
            echo "for dir in \$(find /usr/share/roundcubemail/plugins/$(basename ${plugin})/ -type d -name SQL); do"
            echo "    # Skip plugins with multiple drivers and no kolab driver"
            echo "    if [ ! -z \"\$(echo \${dir} | grep driver)\" ]; then"
            echo "        if [ -z \"\$(echo \${dir} | grep kolab)\" ]; then"
            echo "            continue"
            echo "        fi"
            echo "    fi"
            echo ""
            echo "    /usr/share/roundcubemail/bin/updatedb.sh \\"
            echo "        --dir \${dir} \\"
            echo "        --package $(basename ${plugin}) \\"
            echo "        >/dev/null 2>&1 || :"
            echo ""
            echo "done"
            echo ""
        fi
    ) >> plugins.post

    touch plugins-assets.packages
    (
        echo "%package -n roundcubemail-plugin-$(basename ${plugin})-assets"
        echo "Summary:        Plugin $(basename ${plugin}) Assets"
        echo "Group:          Applications/Internet"
        echo "Provides:       roundcubemail(plugin-$(basename ${plugin})-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
        echo ""
        echo "%description -n roundcubemail-plugin-$(basename ${plugin})-assets"
        echo "Plugin $(basename ${plugin}) Assets"
        echo ""
    ) >> plugins-assets.packages

    touch plugins-assets.files
    (
        echo "%files -n roundcubemail-plugin-$(basename ${plugin})-assets -f plugin-$(basename ${plugin})-assets.files"
        echo "%defattr(-,root,root,-)"
        echo ""
    ) >> plugins-assets.files

    touch plugins-skins.packages
    touch plugins-skins.files
    touch plugins-skins-assets.packages
    touch plugins-skins-assets.files
    for skin in larry classic; do
        for dir in $(find ${target_dir} -type d -name "${skin}" | grep -v "helpdocs" | sort); do
            starget_dir=$(echo ${dir} | %{__sed} -e "s|%{name}-plugin-$(basename ${plugin})-%{version}|%{name}-plugin-$(basename ${plugin})-skin-${skin}-%{version}|g")
            %{__mkdir_p} $(dirname ${starget_dir})
            %{__mv} ${dir} ${starget_dir}

            (
                echo "%package -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}"
                echo "Summary:        Plugin $(basename ${plugin}) / Skin ${skin}"
                echo "Group:          Applications/Internet"
                echo "Requires:       roundcubemail(plugin-$(basename ${plugin})) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Requires:       roundcubemail(skin-${skin}) >= %%{roundcube_version}"
                echo "Requires:       roundcubemail(plugin-$(basename ${plugin})-skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Provides:       roundcubemail(plugin-$(basename ${plugin})-skin) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo "Provides:       roundcubemail(plugin-$(basename ${plugin})-skin-${skin}) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo ""
                echo "%description -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}"
                echo "Plugin $(basename ${plugin}) / Skin ${skin}"
                echo ""
            ) >> plugins-skins.packages

            (
                echo "%files -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin} -f plugin-$(basename ${plugin})-skin-${skin}.files"
                echo "%defattr(-,root,root,-)"
                echo ""
            ) >> plugins-skins.files

            (
                echo "%package -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}-assets"
                echo "Summary:        Plugin $(basename ${plugin}) / Skin ${skin} (Assets)"
                echo "Group:          Applications/Internet"
                echo "Provides:       roundcubemail(plugin-$(basename ${plugin})-skin-${skin}-assets) = %%{?epoch:%%{epoch}:}%%{version}-%%{release}"
                echo ""
                echo "%description -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}-assets"
                echo "Plugin $(basename ${plugin}) / Skin ${skin} (Assets Package)"
                echo ""
            ) >> plugins-skins-assets.packages

            (
                echo "%files -n roundcubemail-plugin-$(basename ${plugin})-skin-${skin}-assets -f plugin-$(basename ${plugin})-skin-${skin}-assets.files"
                echo "%defattr(-,root,root,-)"
                echo ""
            ) >> plugins-skins-assets.files
        done
    done
done

cat \
    plugins.packages \
    plugins-assets.packages \
    plugins-skins.packages \
    plugins-skins-assets.packages \
    > packages

cat \
    plugins.files \
    plugins-assets.files \
    plugins-skins.files \
    plugins-skins-assets.files \
    > files

find | sort | tee files.find >/dev/null

%build

%install
%{__install} -pm 755 %{SOURCE1} .

function new_files() {
    find %{buildroot}%{datadir} -type d -exec echo "%dir {}" \; > current-new.files
    find %{buildroot}%{datadir} -type f >> current-new.files
    find %{buildroot}%{datadir} -type l >> current-new.files

    if [ -f "current.files" ]; then
        %{_bindir}/python ./comm.py current.files current-new.files
    else
        cat current-new.files
    fi

    %{__mv} current-new.files current.files
}

%{__rm} -rf %{buildroot}

%{__install} -d \
    %{buildroot}%{confdir} \
    %{buildroot}%{datadir}/public_html \
    %{buildroot}%{plugindir}

if [ -d "%{buildroot}%{datadir}/public_html/" ]; then
    asset_path="%{buildroot}%{datadir}/public_html/assets"
else
    asset_path="%{buildroot}%{datadir}/assets"
fi

%{__mkdir_p} ${asset_path}

echo "================================================================="
echo "Dividing Plugins, Plugin Assets, Plugin Skins and Plugin Skin Assets and Non-Assets"
echo "================================================================="

for plugin in $(find %{name}-%{version}/plugins/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort); do
    for skin in larry classic; do
        orig_dir="%{name}-plugin-${plugin}-skin-${skin}-%{version}"
        asset_dir="%{name}-plugin-${plugin}-skin-${skin}-assets-%{version}"

        # Compress the CSS
        for file in `find ${orig_dir} -type f -name "*.css"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            cat ${file} | %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) && \
                %{__rm} -rf ${file} || \
                %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
        done || :

        # Compress the JS, but not the already minified
        for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            uglifyjs ${file} > ${asset_loc}/$(basename ${file}) && \
                %{__rm} -rf ${file} || \
                %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
        done || :

        # The already minified JS can just be copied over to the assets location
        for file in `find ${orig_dir} -type f -name "*.min.js"`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
        done || :

        # Other assets
        for file in $(find ${orig_dir} -type f \
                -name "*.eot" -o \
                -name "*.gif" -o \
                -name "*.ico" -o \
                -name "*.jpg" -o \
                -name "*.mp3" -o \
                -name "*.png" -o \
                -name "*.svg" -o \
                -name "*.swf" -o \
                -name "*.tif" -o \
                -name "*.ttf" -o \
                -name "*.woff"
            ); do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
            %{__mkdir_p} ${asset_loc}
            %{__mv} -vf ${file} ${asset_loc}/$(basename $file)
        done || :

        # Purge empty directories
        find ${orig_dir} -type d -empty -delete || :
    done

    # Skin-independent assets
    orig_dir="%{name}-plugin-${plugin}-%{version}"
    asset_dir="%{name}-plugin-${plugin}-assets-%{version}"

    # Compress the CSS
    for file in `find ${orig_dir} -type f -name "*.css"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        cat ${file} | %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) && \
            %{__rm} -rf ${file} || \
            %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
    done

    # Compress the JS, but not the already minified
    for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        uglifyjs ${file} > ${asset_loc}/$(basename ${file}) && \
            %{__rm} -rf ${file} || \
            %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
    done

    # The already minified JS can just be copied over to the assets location
    for file in `find ${orig_dir} -type f -name "*.min.js"`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
    done

    # Other assets
    for file in $(find ${orig_dir} -type f \
            -name "*.eot" -o \
            -name "*.gif" -o \
            -name "*.ico" -o \
            -name "*.jpg" -o \
            -name "*.mp3" -o \
            -name "*.png" -o \
            -name "*.svg" -o \
            -name "*.swf" -o \
            -name "*.tif" -o \
            -name "*.ttf" -o \
            -name "*.woff"
        ); do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__mv} -vf ${file} ${asset_loc}/$(basename $file)
    done

    if [ "${plugin}" == "pdfviewer" ]; then
        %{__mv} -vf ${orig_dir}/plugins/pdfviewer/viewer/locale ${asset_dir}/plugins/pdfviewer/viewer/.
        %{__mv} -vf ${orig_dir}/plugins/pdfviewer/viewer/viewer.html ${asset_dir}/plugins/pdfviewer/viewer/.
    fi

    # Purge empty directories
    find ${orig_dir} -type d -empty -delete || :

    # Install the assets
    for file in `find %{name}-plugin-${plugin}-assets-%{version} -type f`; do
        asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|%{name}-plugin-${plugin}-assets-%{version}|${asset_path}|g"))
        %{__mkdir_p} ${asset_loc}
        %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
    done || :

    new_files > plugin-${plugin}-assets.files

    echo "== Files for plugin ${plugin}: =="
    cat plugin-${plugin}-assets.files
    echo "==========================="

    %{__mkdir_p} %{buildroot}%{plugindir}
    cp -a %{name}-plugin-${plugin}-%{version}/plugins/${plugin} %{buildroot}%{plugindir}/.

    if [ -f "%{buildroot}%{plugindir}/${plugin}/config.inc.php.dist" ]; then
        pushd %{buildroot}%{plugindir}/${plugin}
        %{__mv} config.inc.php.dist %{buildroot}%{confdir}/${plugin}.inc.php
        ln -s ../../../../..%{confdir}/${plugin}.inc.php config.inc.php
        popd
    fi

    if [ -f "%{buildroot}%{plugindir}/${plugin}/logon_page.html" ]; then
        %{__mkdir_p} %{buildroot}%{confdir}
        %{__mv} -vf %{buildroot}%{plugindir}/${plugin}/logon_page.html %{buildroot}%{confdir}
        pushd %{buildroot}%{plugindir}/${plugin}/
        ln -s ../../../../..%{confdir}/logon_page.html logon_page.html
        popd
    fi

    new_files > plugin-${plugin}.files

    echo "== Files for plugin ${plugin}: =="
    cat plugin-${plugin}.files
    echo "==========================="
done

for plugin in $(find %{name}-%{version}/plugins/ -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort); do
    for skin in larry classic; do
        touch plugin-${plugin}-skin-${skin}.files
        touch plugin-${plugin}-skin-${skin}-assets.files

        if [ -d "%{name}-plugin-${plugin}-skin-${skin}-%{version}/plugins/${plugin}/skins/${skin}" ]; then
            %{__install} -d %{buildroot}%{plugindir}/${plugin}/skins/
            cp -a %{name}-plugin-${plugin}-skin-${skin}-%{version}/plugins/${plugin}/skins/${skin} %{buildroot}%{plugindir}/${plugin}/skins/.

            new_files > plugin-${plugin}-skin-${skin}.files

            echo "== Files for skin ${plugin}-${skin}: =="
            cat plugin-${plugin}-skin-${skin}.files
            echo "==========================="
        fi

        # Install the assets
        for file in `find %{name}-plugin-${plugin}-skin-${skin}-assets-%{version} -type f`; do
            asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|%{name}-plugin-${plugin}-skin-${skin}-assets-%{version}|${asset_path}|g"))
            %{__mkdir_p} ${asset_loc}
            %{__cp} -av ${file} ${asset_loc}/$(basename ${file})
        done || :

        new_files > plugin-${plugin}-skin-${skin}-assets.files

        echo "== Files for skin ${plugin}-${skin}: =="
        cat plugin-${plugin}-skin-${skin}-assets.files
        echo "==========================="

    done
done

# Provide the rpm state directory
%{__mkdir_p} %{buildroot}/%{_localstatedir}/lib/rpm-state/roundcubemail/

%{__sed} -r -i \
    -e 's|%{buildroot}||g' \
    -e '/^%dir\s*$/d' \
    -e '/^(%dir )*\/etc\/roundcubemail\//d' \
    -e '/^(%dir )*\/var\//d' \
    *.files

%pre -n roundcubemail-plugin-ude_login
if [ -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    %{__rm} -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted"
fi

%posttrans -n roundcubemail-plugin-ude_login
if [ ! -f "%{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted" ]; then
    if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
        if [ ! -z "$(grep ^apc.enabled=1 %{php_inidir}/apc{,u}.ini)" ]; then
%if 0%{?with_systemd}
            /bin/systemctl condrestart %{httpd_name}.service
%else
            /sbin/service %{httpd_name} condrestart
%endif
        fi
    fi
    %{__mkdir_p} %{_localstatedir}/lib/rpm-state/roundcubemail/
    touch %{_localstatedir}/lib/rpm-state/roundcubemail/httpd.restarted
fi

%clean
rm -rf %{buildroot}

%files -f plugin-ude_login.files
%defattr(-,root,root,-)
%attr(0640,root,%{httpd_group}) %config(noreplace) %{confdir}/ude_login.inc.php

%files -n roundcubemail-plugin-ude_login-assets -f plugin-ude_login-assets.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-ude_login-skin-larry -f plugin-ude_login-skin-larry.files
%defattr(-,root,root,-)

%files -n roundcubemail-plugin-ude_login-skin-larry-assets -f plugin-ude_login-skin-larry-assets.files
%defattr(-,root,root,-)

%changelog
* Mon Dec 03 2018 Timotheus Pokorra <tp@tbits.net> - 3.3.6-2
- separate package for plugin ude_login
