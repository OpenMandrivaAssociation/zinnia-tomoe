%define tomoe_version 0.6.0
%define snapdate 20080911

Summary: 	Zinnia Recognition models
Name: 		zinnia-tomoe
Version:	0.6.0_20080911
Release:	1
License: 	LGPLv2+
Group: 		System/Internationalization
Source: 	http://downloads.sourceforge.net/zinnia/%{name}-%tomoe_version-%snapdate.tar.bz2
URL: 		http://zinnia.sourceforge.net/
BuildArch:	noarch
BuildRequires:	zinnia >= 0.02
Requires:	zinnia >= 0.02

%description
Model files trained with Tomoe data.

%package ja
Summary:	Zinnia Recognition models - Japanese data
Group:		System/Internationalization
Provides:	%{name} = %{version}-%{release}
Requires:	locales-ja

%description ja
Japanese Model files trained with Tomoe data.

%package zh_CN
Summary:	Zinnia Recognition models - Simplified Chinese data
Group:		System/Internationalization
Provides:	%{name} = %{version}-%{release}
Requires:	locales-zh

%description zh_CN
Simplified Chinese Model files trained with Tomoe data.

%prep
%setup -qn %{name}-%{tomoe_version}-%{snapdate}

%build
%configure2_5x
%make

%install
%makeinstall_std

%clean

%files ja
%{_prefix}/lib/zinnia/model/tomoe/handwriting-ja.model

%files zh_CN
%{_prefix}/lib/zinnia/model/tomoe/handwriting-zh_CN.model
