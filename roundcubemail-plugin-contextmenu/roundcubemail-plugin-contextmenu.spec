%global datadir %{_datadir}/roundcubemail
%global plugindir %{datadir}/plugins

Name:           roundcubemail-plugin-contextmenu
Version:        2.3
Release:        1%{?dist}
Summary:        Contextmenu plugin for Roundcube Webmail

Group:          Applications/Internet
License:        AGPLv3+ and GPLv3+
URL:            http://www.kolab.org

# From f3458e5a74372a64ad2387f90ceca33373e259ec
Source0:        %{name}-%{version}.tar.gz

BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch

%if "%{_arch}" != "ppc64" && "%{_arch}" != "ppc64le" && 0%{?suse_version} < 1
BuildRequires:  python-cssmin
BuildRequires:  uglify-js
%endif

Requires:       roundcubemail(core) >= 1.1

%description
Adds context menus to the message list, folder list and address book.
The menu includes the abilities mark messages as read/unread, delete,
reply and forward.

%prep
%setup -q

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
