Summary:	Character set conversion library
Summary(pl):	Biblioteka konwersji zestawów znaków
Name:		libiconv
Version:	1.8
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/pub/gnu/libiconv/%{name}-%{version}.tar.gz
# Source0-md5:	fd2a95a4b79fbdc8ea55ad093a8bb6cf
URL:		http://www.haible.de/bruno/packages-libcharset.html
Patch0:		%{name}-DESTDIR.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides an iconv() implementation, for use on systems
which don't have one, or whose implementation cannot convert from/to
Unicode.

%description -l pl

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
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog DESIGN NEWS NOTES PORTS README* THANKS
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libcharset.h
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
