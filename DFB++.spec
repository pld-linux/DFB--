Summary:	C++ binding for DirectFB
Summary(pl):	Interfejs C++ do DirectFB
Name:		DFB++
Version:	0.9.21
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/download/DirectFB-extra/%{name}-%{version}.tar.gz
# Source0-md5:	8184ade239bbdf93c5e31c71d1842133
URL:		http://www.directfb.org/index.php?path=Development/Projects/DFB++
BuildRequires:	DirectFB-devel >= 1:%{version}
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
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
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB-devel >= 1:%{version}
Requires:	libstdc++-devel

%description devel
Header files for DFB++ library.

%description devel -l pl
Pliki nag³ówkowe biblioteki DFB++.

%package static
Summary:	DFB++ static library
Summary(pl):	Statyczna biblioteka DFB++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
DFB++ static library.

%description static -l pl
Statyczna biblioteka DFB++.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%attr(755,root,root) %{_bindir}/dfbshow
%attr(755,root,root) %{_bindir}/dfbswitch
%attr(755,root,root) %{_libdir}/libdfb++-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dfb++-config
%attr(755,root,root) %{_libdir}/libdfb++.so
%{_libdir}/libdfb++.la
%{_includedir}/dfb++
%{_pkgconfigdir}/*.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libdfb++.a
