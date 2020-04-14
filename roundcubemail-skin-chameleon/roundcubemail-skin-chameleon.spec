Name:           roundcubemail-skin-chameleon
Version:        0.3.11
Release:        1.11%{?dist}.kolab_16
Summary:        Kolab skin for Roundcube

Group:          Web/Applications
License:        CC-BY-SA
URL:            http://www.kolab.org
Source0:        http://mirror.kolabsys.com/pub/releases/%{name}-%{version}.tar.gz

BuildArch:      noarch

%if "%{_arch}" != "ppc64" && "%{_arch}" != "ppc64le"
BuildRequires:  nodejs-less
%if 0%{?suse_version} < 1
BuildRequires:  uglify-js
%endif
%else
BuildRequires:  php-lessphp
%endif

BuildRequires:  python

Requires:       roundcubemail(skin-chameleon) = %{?epoch:%%{epoch}:}%{version}-%{release}
Requires:       roundcubemail(skin-chameleon-assets) = %{?epoch:%%{epoch}:}%{version}-%{release}

%description
This package contains a Kolab Groupware skin for the Roundcube web mail
interface.

%package core
Summary:        Chameleon skin for Roundcube
Group:          Applications/Internet
Requires:       roundcubemail(core) >= 1.1
Requires:       roundcubemail(skin-larry) >= 1.1
Provides:       roundcubemail(skin-chameleon) = %{?epoch:%%{epoch}:}%{version}-%{release}

%description core
Kolab skin for Roundcube

%package assets
Summary:        Assets for the Chameleon skin
Group:          Applications/Internet
Requires:       roundcubemail(skin-larry-assets) >= 1.1
Provides:       roundcubemail(skin-chameleon-assets) = %{?epoch:%%{epoch}:}%{version}-%{release}

%description assets
Assets for the Chameleon skin

%prep
%setup -q

%build

%install

mkdir -p %{buildroot}/%{_datadir}/roundcubemail/skins/
cp -a skins/chameleon/ %{buildroot}/%{_datadir}/roundcubemail/skins/.

orig_dir=%{buildroot}/%{_datadir}/roundcubemail/skins/chameleon/
asset_dir=%{buildroot}/%{_datadir}/roundcubemail/public_html/assets/skins/chameleon/

# Compile and compress the CSS
for file in `find ${orig_dir} -type f -name "*.less" ! -name "colors.less" | grep -vE "${orig_dir}/(plugins|skins)/"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|$asset_dir|g"))
    %{__mkdir_p} ${asset_loc}
    %{_bindir}/lessc -x ${file} > ${asset_loc}/$(basename ${file} .less).css || \
        cat $(dirname ${file})/colors.less ${file} | %{_bindir}/plessc -r -f=compressed > ${asset_loc}/$(basename ${file} .less).css
done

# Compress the JS, but not the already minified
for file in `find ${orig_dir} -type f -name "*.js" ! -name "*.min.js" | grep -vE "${orig_dir}/(plugins|skins)/"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|$asset_dir|g"))
    %{__mkdir_p} ${asset_loc}
    uglifyjs ${file} > ${asset_loc}/$(basename ${file}) && \
        %{__rm} -rf ${file} || \
        %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
done

# The already minified JS can just be copied over to the assets location
for file in `find ${orig_dir} -type f -name "*.min.js" | grep -vE "${orig_dir}/(plugins|skins)/"`; do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|$asset_dir|g"))
    %{__mkdir_p} ${asset_loc}
    %{__mv} -v ${file} ${asset_loc}/$(basename ${file})
done

# Other assets
for file in $(find ${orig_dir} -type f \
        -name "*.eot" -o \
        -name "*.gif" -o \
        -name "*.ico" -o \
        -name "*.jpg" -o \
        -name "*.png" -o \
        -name "*.svg" -o \
        -name "*.swf" -o \
        -name "*.tif" -o \
        -name "*.ttf" -o \
        -name "*.woff" | \
        grep -vE "${orig_dir}/(plugins|skins)/"
    ); do
    asset_loc=$(dirname $(echo ${file} | %{__sed} -e "s|${orig_dir}|$asset_dir|g"))
    %{__mkdir_p} ${asset_loc}
    %{__mv} -vf ${file} ${asset_loc}/$(basename $file)
done

mv %{buildroot}/%{_datadir}/roundcubemail/skins/chameleon/watermark.html \
    %{buildroot}/%{_datadir}/roundcubemail/public_html/assets/skins/chameleon/watermark.html

%files
%defattr(-,root,root,-)

%files core
%defattr(-,root,root,-)
%if 0%{?suse_version}
%dir %{_datadir}/roundcubemail/
%dir %{_datadir}/roundcubemail/skins/
%dir %{_datadir}/roundcubemail/public_html/
%dir %{_datadir}/roundcubemail/public_html/assets/
%dir %{_datadir}/roundcubemail/public_html/assets/skins/
%endif
%{_datadir}/roundcubemail/skins/chameleon/

%files assets
%{_datadir}/roundcubemail/public_html/assets/skins/chameleon/

%changelog
* Thu Mar 21 2019 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.11-1
- Release 0.3.11

* Sat Jan 19 2019 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.10-2
- Patch T4371

* Wed Oct  3 2018 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.10-1
- Release of version 0.3.10

* Wed Apr 11 2018 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.9-2
- Rebuild

* Wed Aug  2 2017 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.9-1
- Release 0.3.9

* Sun Mar  6 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.8-1
- Release 0.3.8

* Sat Jan 16 2016 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.7-1
- Release 0.3.7

* Thu Dec  3 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.6-3
- Allow building with php-based less

* Fri Mar 27 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.6-1
- Release of version 0.3.6, see:

  https://issues.kolab.org/buglist.cgi?target_milestone=0.3.6&product=Chameleon%20Skin

* Wed Feb 25 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.5-1
- Release of version 0.3.5, see:

  https://issues.kolab.org/buglist.cgi?target_milestone=0.3.5&product=Chameleon%20Skin

* Tue Feb 17 2015 Daniel Hoffend <dh@dotlan.net> - 0.3.4-2
- Applied 2 patches (button overlay)

* Thu Feb  5 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.4-1
- Release of version 0.3.4, see:

  https://issues.kolab.org/buglist.cgi?target_milestone=0.3.4&product=Chameleon%20Skin

* Thu Jan 29 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.3-1
- Release of version 0.3.3, see:

  https://issues.kolab.org/buglist.cgi?target_milestone=0.3.3&product=Chameleon%20Skin

* Wed Jan 21 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.2-1
- Release of version 0.3.2, see:

  https://issues.kolab.org/buglist.cgi?product=Chameleon Skin&target_milestone=0.3.2

* Wed Jan  7 2015 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.1-1
- Multiple fixes for the Chameleon skin, see:

  https://issues.kolab.org/buglist.cgi?product=Chameleon Skin&target_milestone=0.3.1

* Fri Dec 19 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.3.0-1
- Multiple fixes for the Chameleon skin, see:

  https://issues.kolab.org/buglist.cgi?product=Chameleon Skin&target_milestone=0.3.0

* Tue Dec  9 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.2-1
- Some improvements and better icons

* Sun Dec  7 2014 Jeroen van Meeuwen <vanmeeuwen@kolabsys.com> - 0.1-1
- First package
