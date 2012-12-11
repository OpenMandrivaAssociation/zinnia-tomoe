%define tomoe_version 0.6.0
%define snapdate 20080911

Summary: 	Zinnia Recognition models
Name: 		zinnia-tomoe
Version: 	%{tomoe_version}.%{snapdate}
Release: 	%mkrel 2
License: 	LGPLv2+
Group: 		System/Internationalization
Source: 	http://downloads.sourceforge.net/zinnia/%name-%tomoe_version-%snapdate.tar.bz2
URL: 		http://zinnia.sourceforge.net/
Buildroot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch
BuildRequires:	zinnia >= 0.02
Requires:	zinnia >= 0.02

%description
Model files trained with Tomoe data.

%package ja
Summary:	Zinnia Recognition models - Japanese data
Group:		System/Internationalization
Provides:	%name = %version-%release
Requires:	locales-ja

%description ja
Japanese Model files trained with Tomoe data.

%package zh_CN
Summary:	Zinnia Recognition models - Simplified Chinese data
Group:		System/Internationalization
Provides:	%name = %version-%release
Requires:	locales-zh_CN

%description zh_CN
Simplified Chinese Model files trained with Tomoe data.

%prep
%setup -qn %name-%tomoe_version-%snapdate

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files ja
%defattr (-,root,root)
%{_prefix}/lib/zinnia/model/tomoe/handwriting-ja.model

%files zh_CN
%defattr (-,root,root)
%{_prefix}/lib/zinnia/model/tomoe/handwriting-zh_CN.model


%changelog
* Mon Sep 21 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6.0.20080911-2mdv2010.0
+ Revision: 446328
- rebuild

* Sun Feb 15 2009 Funda Wang <fundawang@mandriva.org> 0.6.0.20080911-1mdv2009.1
+ Revision: 340516
- add groups
- import zinnia-tomoe


