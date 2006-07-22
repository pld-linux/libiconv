Summary:	Character set conversion library
Summary(pl):	Biblioteka konwersji zestaw�w znak�w
Name:		libiconv
Version:	1.11
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/libiconv/%{name}-%{version}.tar.gz
# Source0-md5:	b77a17e4a5a817100ad4b2613935055e
Patch0:		%{name}-pl.po-update.patch
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
Ta biblioteka dostarcza implementacj� iconv() do u�ywania z systemami,
kt�re takiej funkcji nie posiadaj�, lub na kt�rych implementacja nie
potrafi konwertowa� z/do Unikodu.

%package devel
Summary:	libiconv header files
Summary(pl):	Pliki nag��wkowe biblioteki libiconv
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if "%{_includedir}" == "/usr/include"
Conflicts:	glibc-devel
%endif

%description devel
This package contains libiconv header files.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe biblioteki libiconv.

%package static
Summary:	libiconv static library
Summary(pl):	Statyczna biblioteka libiconv
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains static libiconv library.

%description static -l pl
Pakiet ten zawiera statyczn� bibliotek� libiconv.

%prep
%setup -q
%patch0 -p1

rm -f po/stamp-po

%build
cp -f /usr/share/automake/config.sub libcharset/autoconf
cp -f /usr/share/automake/config.sub autoconf
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
#%attr(755,root,root) %{_bindir}/iconv
%attr(755,root,root) %{_libdir}/libcharset.so.*.*.*
%attr(755,root,root) %{_libdir}/libiconv.so.*.*.*
%attr(755,root,root) %{_libdir}/preloadable_libiconv.so
#%{_mandir}/man1/iconv.1*

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
