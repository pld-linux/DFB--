Summary:	C++ binding for DirectFB
Summary(pl):	Interfejs C++ do DirectFB
Name:		DFB++
Version:	0.9.18
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/DirectFB/%{name}-%{version}.tar.gz
# Source0-md5:	2d4dff9031b82aa9a6f7cc55c6cb3164
URL:		http://www.directfb.org/
BuildRequires:	DirectFB-devel >= %{version}
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DFB++ is a C++ binding for DirectFB providing a much easier usage. One
advantage is that the 'thiz' doesn't need to be passed as the first
argument of every interface function. Another feature is the usage of
exceptions. It's annoying having these error checking stuff with
growing deinitialization stacks. Most functions are 'void'. As soon as
a DirectFB function returns an error a DFBException is thrown.
		
%description -l pl
DFB++ jest interfejsem C++ do biblioteki DirectFB, u³atwiaj±cym jej
u¿ywanie. Jedn± z zalet jest brak konieczno¶ci przekazywania 'thiz'
jako pierwszego parametru ka¿dej funkcji. Kolejn± jest korzystanie z
wyj±tków. Ci±g³e sprawdzanie b³êdów z powiêkszaj±cym stosem
deinicjalizacji mo¿e byæ dokuczliwe. W DFB++, kiedy funkcja DirectFB
zwraca b³±d, rzucany jest wyj±tek DFBException.

%package devel
Summary:	DFB++ header files
Summary(pl):	Pliki nag³ówkowe DFB++
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for DFB++ library.

%description devel -l pl
Pliki nag³ówkowe biblioteki DFB++.

%package static
Summary:	DFB++ static library
Summary(pl):	Statyczna biblioteka DFB++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
DFB++ static library.

%description static -l pl
Statyczna biblioteka DFB++.

%prep
%setup -q

%build
%{__autoconf}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/simple.cpp $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_bindir}/dfb++-config
%{_includedir}/dfb++
%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
