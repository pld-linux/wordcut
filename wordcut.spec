Summary:	Thai word segmentation utility
Summary(pl.UTF-8):	Narzędzie do dzielenia słów w języku tajskim
Name:		wordcut
Version:	0.5.1
%define	subver	b2
Release:	0.%{subver}.1
License:	BSD
Group:		Libraries
Source0:	http://downloads.sourceforge.net/thaiwordseg/%{name}-%{version}%{subver}.tar.gz
# Source0-md5:	6fc6cc07d84085416e03456f4882888b
URL:		http://thaiwordseg.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thai word segmentation utility.

%description -l pl.UTF-8
Narzędzie do dzielenia słów w języku tajskim.

%package devel
Summary:	Header files for wordcut library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki wordcut
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for wordcut library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki wordcut.

%package static
Summary:	Static wordcut library
Summary(pl.UTF-8):	Statyczna biblioteka wordcut
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static wordcut library.

%description static -l pl.UTF-8
Statyczna biblioteka wordcut.

%prep
%setup -q -n %{name}-%{version}%{subver}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libwordcut.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/wordcut
%attr(755,root,root) %{_bindir}/wordcut_dict_dump
%attr(755,root,root) %{_bindir}/wordcut_mkdict
%attr(755,root,root) %{_libdir}/libwordcut.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwordcut.so.0
%{_datadir}/wordcut

%files devel
%defattr(644,root,root,755)
%doc docs/manual.pdf
%attr(755,root,root) %{_libdir}/libwordcut.so
%{_includedir}/wordcut
%{_pkgconfigdir}/wordcut.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwordcut.a
