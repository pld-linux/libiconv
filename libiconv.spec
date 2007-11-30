Summary:	Character set conversion library
Summary(pl.UTF-8):	Biblioteka konwersji zestawów znaków
Name:		libiconv
Version:	1.12
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/libiconv/%{name}-%{version}.tar.gz
# Source0-md5:	c2be282595751535a618ae0edeb8f648
Patch0:		%{name}-pl.po-update.patch
URL:		http://www.haible.de/bruno/packages-libcharset.html
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides an iconv() implementation, for use on systems
which don't have one, or whose implementation cannot convert from/to
Unicode.

%description -l pl.UTF-8
Ta biblioteka dostarcza implementację iconv() do używania z systemami,
które takiej funkcji nie posiadają, lub na których implementacja nie
potrafi konwertować z/do Unikodu.

%package devel
Summary:	libiconv header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libiconv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if "%{_includedir}" == "/usr/include"
Conflicts:	glibc-devel
%endif

%description devel
This package contains libiconv header files.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe biblioteki libiconv.

%package static
Summary:	libiconv static library
Summary(pl.UTF-8):	Statyczna biblioteka libiconv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libiconv library.

%description static -l pl.UTF-8
Pakiet ten zawiera statyczną bibliotekę libiconv.

%package utils
Summary:	iconv utility
Summary(pl.UTF-8):	Narzędzie iconv
License:	GPL v3+
Group:		Applications/Text
Requires:	%{name} = %{version}-%{release}
%if "%{_bindir}" == "/usr/bin"
Conflicts:	glibc-misc
%endif

%description utils
iconv utility.

%description utils -l pl.UTF-8
Narzędzie iconv.

%prep
%setup -q
%patch0 -p1

rm -f po/stamp-po

%build
cp -f /usr/share/automake/config.sub build-aux
cp -f /usr/share/automake/config.sub libcharset/build-aux
%{__aclocal} -I m4 -I srcm4
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
%attr(755,root,root) %{_libdir}/libcharset.so.*.*.*
%attr(755,root,root) %{_libdir}/libiconv.so.*.*.*
%attr(755,root,root) %{_libdir}/preloadable_libiconv.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcharset.so
%attr(755,root,root) %{_libdir}/libiconv.so
%{_libdir}/libcharset.la
%{_libdir}/libiconv.la
%{_includedir}/iconv.h
%{_includedir}/libcharset.h
%{_includedir}/localcharset.h
%{_mandir}/man3/iconv*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcharset.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/iconv
%{_mandir}/man1/iconv.1*
