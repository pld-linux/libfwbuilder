Summary:	Firewall Builder API
Summary(pl):	Biblioteka Firewall Buildera
Name:		libfwbuilder
Version:	0.10.13
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://belnet.dl.sourceforge.net/sourceforge/fwbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	b379556ef5f4257de734298093df83b8
URL:		http://www.fwbuilder.org/
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.7
BuildRequires:	libsigc++1-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	net-snmp-compat-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Firewall Builder API Library.

%description -l pl
Biblioteka Firewall Buildera.

%package devel
Summary:	Header files and develpment documentation for libfwbuilder
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libfwbuilder
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libstdc++-devel

%description devel
Header files and develpment documentation for libfwbuilder.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libfwbuilder.

%package static
Summary:	Static libfwbuilder library
Summary(pl):	Biblioteka statyczna libfwbuilder
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libfwbuilder library.

%description static -l pl
Biblioteka statyczna libfwbuilder.

%prep
%setup  -q

%build
CFLAGS="`xslt-config --cflags` %{rpmcflags}"
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,ChangeLog,Credits,README}
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
