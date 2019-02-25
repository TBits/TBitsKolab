%if 0%{?opensuse_bs}
#!BuildIgnore:  caddy
#!BuildIgnore:  lighttpd
#!BuildIgnore:  nginx
%endif

%global datadir %{_datadir}/roundcubemail
%global plugindir %{datadir}/plugins

%global rc_version 3.0
%global rc_rel_suffix beta1
%global dot_rel_suffix %{?rc_rel_suffix:.%{rc_rel_suffix}}
%global dash_rel_suffix %{?rc_rel_suffix:-%{rc_rel_suffix}}

Name:           roundcubemail-plugin-contextmenu
Version:        %{rc_version}
Release:        2%{?dot_rel_suffix}%{?dist}
Summary:        Contextmenu plugin for Roundcube Webmail

Group:          Applications/Internet
License:        AGPLv3+ and GPLv3+
URL:            http://www.kolab.org

# From 89554367bc1d02526ebfbfb9be73267b995a7c74
Source0:        %{name}-%{version}%{?dash_rel_suffix}.tar.gz

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

%if "%{_arch}" != "ppc64" && "%{_arch}" != "ppc64le"
BuildRequires:  nodejs-less
%if 0%{?suse_version} < 1
BuildRequires:  python-cssmin
BuildRequires:  uglify-js
%endif
%endif

BuildRequires:  roundcubemail(skin-elastic)

Requires:       roundcubemail(core) >= 1.1

%description
Adds context menus to the message list, folder list and address book.
The menu includes the abilities mark messages as read/unread, delete,
reply and forward.

%prep
%setup -q -n %{name}-%{version}%{?dash_rel_suffix}

find . -type f -name "*.less" | while read file; do
    sed -i -e 's|../../../../skins/elastic/styles/|../../../../../../../../usr/share/roundcubemail/skins/elastic/styles/|g' ${file}
done

%build

%install
rm -rf %{buildroot}
mkdir -p \
    %{buildroot}%{plugindir}/contextmenu
cp -a * %{buildroot}%{plugindir}/contextmenu

asset_path="%{buildroot}%{datadir}/public_html/assets"

mkdir -p ${asset_path}

orig_dir="%{buildroot}%{datadir}/plugins/"
asset_dir="$asset_path/plugins/"

# Compile and compress the CSS
for file in `find ${orig_dir} -type f -name "*.less" ! -name "colors.less"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|${asset_dir}|g"))
    %{__mkdir_p} ${asset_loc}
    %{_bindir}/lessc --relative-urls -x ${file} > ${asset_loc}/$(basename ${file} .less).css || \
        cat ${file} | %{_bindir}/plessc -r -f=compressed > ${asset_loc}/$(basename ${file} .less).css || :
done
find ${asset_loc} -type f -name "*.css" -empty -delete
find ${asset_loc} -type d -empty -delete

# Compress the CSS
for file in `find $orig_dir -type f -name "*.css"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|$orig_dir|$asset_dir|g"))
    %{__mkdir_p} ${asset_loc}
    cat ${file} | %{_bindir}/python-cssmin > ${asset_loc}/$(basename ${file}) && \
        %{__rm} -rf ${file} || \
        %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
done

# Compress the JS, but not the already minified
for file in `find $orig_dir -type f -name "*.js" ! -name "*.min.js"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|$orig_dir|$asset_dir|g"))
    %{__mkdir_p} ${asset_loc}
    uglifyjs ${file} > ${asset_loc}/$(basename ${file}) && \
        %{__rm} -rf ${file} || \
        %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
done

# The already minified JS can just be copied over to the assets location
for file in `find $orig_dir -type f -name "*.min.js"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|$orig_dir|$asset_dir|g"))
    %{__mkdir_p} ${asset_loc}
    %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
done

# Other assets
for file in $(find $orig_dir -type f \
        -name "*.eot" -o \
        -name "*.gif" -o \
        -name "*.ico" -o \
        -name "*.jpg" -o \
        -name "*.png" -o \
        -name "*.svg" -o \
        -name "*.swf" -o \
        -name "*.tif" -o \
        -name "*.ttf" -o \
        -name "*.woff"
    ); do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|$orig_dir|$asset_dir|g"))
    %{__mkdir_p} ${asset_loc}
    %{__mv} -vf ${file} ${asset_loc}/$(basename $file)
done

%post
if [ -f "%{php_inidir}/apc.ini" -o -f "%{php_inidir}/apcu.ini" ]; then
    if [ ! -z "`grep apc.enabled=1 %{php_inidir}/apc{,u}.ini`" ]; then
%if 0%{?fedora} > 15
        /bin/systemctl condrestart httpd.service
%else
    /sbin/service httpd condrestart
%endif
    fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{datadir}
%dir %{plugindir}
%{plugindir}/contextmenu
%dir %{datadir}/public_html/
%dir %{datadir}/public_html/assets/
%dir %{datadir}/public_html/assets/plugins/
%{datadir}/public_html/assets/plugins/contextmenu/

%changelog
* Sat Jan 19 2019 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 3.0-4.beta1
- Rebuild against core updates

* Fri Dec  7 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 3.0-3.beta1
- Another pre-release of version 3.0

* Thu Apr 12 2018 Jeroen van Meeuwen (Kolab Systems) <vanmeeuwen@kolabsys.com> - 3.0-1.alpha0
- Pre-release of version 3.0

* Wed Aug  2 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.3-1
- Release of version 2.3

* Tue Mar 31 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.1.1-1
- Release of version 2.1.1

* Sat Sep  6 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 2.1-1
- New upstream version

* Thu Apr  3 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.13-1
- New upstream version

* Mon Nov 25 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.10-2
- Repack of 1.10 with interface fixes for the most recent Roundcube

* Fri Jun 14 2013 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 1.10-1
- Initial package version
