Summary:	Firewall Builder API
Summary(pl):	Biblioteka Firewall Buildera
Name:		libfwbuilder
Version:	2.0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/fwbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	071440696ff7fc262929ec4a270a4d4b
Patch0:		%{name}-configure.patch
URL:		http://www.fwbuilder.org/
BuildRequires:	autoconf
BuildRequires:	automake
# it uses internal symbols from libresolv.a :/
BuildRequires:	glibc-static
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firewall Builder API Library.

%description -l pl
Biblioteka Firewall Buildera.

%package devel
Summary:	Header files and develpment documentation for libfwbuilder
Summary(pl):	Pliki nag³ówkowe i dokumetacja do libfwbuilder
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# it uses internal symbols from libresolv.a :/
Requires:	glibc-static
Requires:	libstdc++-devel
Requires:	libxml2-devel
Requires:	libxslt-devel
Requires:	net-snmp-devel
Requires:	openssl-devel
Obsoletes:	libfwbuilder-static

%description devel
Header files and develpment documentation for libfwbuilder.

%description devel -l pl
Pliki nag³ówkowe i dokumetacja do libfwbuilder.

%prep
%setup -q
%patch0 -p1

%{__perl} -pi -e 's@/usr/lib/libresolv@/usr/%{_lib}/libresolv@' configure.in
%{__perl} -pi -e 's@/lib$@/%{_lib}@' qmake.inc.in

%build
cp -f /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,ChangeLog,Credits,README}
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libfwbuilder-config-2
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/fwb-2.0
