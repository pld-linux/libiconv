Summary:	Character set conversion library
Summary(pl):	Biblioteka konwersji zestawów znaków
Name:		libiconv
Version:	1.9.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/libiconv/%{name}-%{version}.tar.gz
# Source0-md5:	6bc300365053c815b10b800a21e0bc7e
URL:		http://www.haible.de/bruno/packages-libcharset.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides an iconv() implementation, for use on systems
which don't have one, or whose implementation cannot convert from/to
Unicode.

%description -l pl
Ta biblioteka dostarcza implementacjê iconv() do u¿ywania z systemami,
które takiej funkcji nie posiadaj±, lub na których implementacja nie
potrafi konwertowaæ z/do Unikodu.

%package devel
Summary:	libiconv header files
Summary(pl):	Pliki nag³ówkowe biblioteki libiconv
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains libiconv header files.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe biblioteki libiconv.

%package static
Summary:	libiconv static library
Summary(pl):	Statyczna biblioteka libiconv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains static libiconv library.

%description static -l pl
Pakiet ten zawiera statyczn± bibliotekê libiconv.

%prep
%setup -q

%build
%{__aclocal} -I m4
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DESIGN NEWS NOTES PORTS README* THANKS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/libiconv_plug.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*[!g].so
%{_libdir}/*.la
#%{_includedir}/iconv.h
%{_includedir}/libcharset.h
%{_includedir}/localcharset.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
