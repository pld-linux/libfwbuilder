Summary:	Firewall Builder API
Summary(pl):	Biblioteka Firewall Buildera
Name:		libfwbuilder
Version:	1.0.2
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/fwbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	f5e50b8165b1dded26f461cf488553ea
Patch0:		%{name}-static.patch
URL:		http://www.fwbuilder.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.8
# it uses internal symbols from libresolv.a :/
BuildRequires:	glibc-static
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firewall Builder API Library.

%description -l pl
Biblioteka Firewall Buildera.

%package devel
Summary:	Header files and develpment documentation for libfwbuilder
Summary(pl):	Pliki nagłówkowe i dokumetacja do libfwbuilder
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib-devel
# it uses internal symbols from libresolv.a :/
Requires:	glibc-static
Requires:	libstdc++-devel
Requires:	libxml2-devel
Requires:	libxslt-devel
Requires:	net-snmp-devel
Requires:	openssl-devel

%description devel
Header files and develpment documentation for libfwbuilder.

%description devel -l pl
Pliki nagłówkowe i dokumetacja do libfwbuilder.

%package static
Summary:	Static libfwbuilder library
Summary(pl):	Biblioteka statyczna libfwbuilder
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfwbuilder library.

%description static -l pl
Biblioteka statyczna libfwbuilder.

%prep
%setup -q
%patch0 -p1

%{__perl} -pi -e 's@/usr/lib/libresolv@/usr/%{_lib}/libresolv@' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %{_bindir}/%{name}-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/fwbuilder
%{_includedir}/fwcompiler

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
