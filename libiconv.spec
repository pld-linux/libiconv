# NOTE: don't send this (glibc based) build to builders
Summary:	Character set conversion library
Summary(pl.UTF-8):	Biblioteka konwersji zestawów znaków
Name:		libiconv
Version:	1.18
Release:	0.1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/libiconv/%{name}-%{version}.tar.gz
# Source0-md5:	1af69958b42981d3c3029ffb4c7ebaed
URL:		http://www.gnu.org/software/libiconv/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libtool >= 2:2.0
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

%{__rm} po/stamp-po

# struggling to get it regenerated, but i fail, these still remain:
#-rw-r--r-- 1 glen users 281073 24. sept   2010 ./libcharset/m4/libtool.m4
#-rw-r--r-- 1 glen users 281073 24. sept   2010 ./m4/libtool.m4
%{__rm} libcharset/m4/{libtool,lt*}.m4
%{__rm} m4/{libtool,lt*}.m4

%build
cp -f /usr/share/automake/config.sub build-aux
cp -f /usr/share/automake/config.sub libcharset/build-aux
cd libcharset
%{__libtoolize}
%{__aclocal} -I m4 -I ../srcm4
%{__autoconf}
%{__autoheader}
cd ..
%{__libtoolize}
%{__aclocal} -I m4 -I srcm4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_docdir}/*.html

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DESIGN NEWS NOTES README THANKS
%attr(755,root,root) %{_libdir}/libcharset.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcharset.so.1
%attr(755,root,root) %{_libdir}/libiconv.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiconv.so.2

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
