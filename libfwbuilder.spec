#
# Conditional build:
%bcond_without	snmp		# disable SNMP
%bcond_without	threadsafe_dns	# disable thread safe DNS
#
%define		_majver		2
%define		_minver		1

Summary:	Firewall Builder API
Summary(pl):	Biblioteka Firewall Buildera
Name:		libfwbuilder
Version:	%{_majver}.%{_minver}.5
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://www.fwbuilder.org/nightly_builds/build-109/%{name}-%{version}.tar.gz
# Source0-md5:	63a038b624900262074e7efc6e0f3894
Patch0:		%{name}-configure.patch
URL:		http://www.fwbuilder.org/
BuildRequires:	autoconf
BuildRequires:	automake
# it uses internal symbols from libresolv.a :/
%{?with_threadsafe_dns:BuildRequires:	glibc-static}
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel
%{?with_snmp:BuildRequires:	net-snmp-devel}
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
%{?with_threadsafe_dns:Requires:	glibc-static}
Requires:	libstdc++-devel
Requires:	libxml2-devel
Requires:	libxslt-devel
%{?with_snmp:Requires:	net-snmp-devel}
Requires:	openssl-devel
Obsoletes:	libfwbuilder-static

%description devel
Header files and develpment documentation for libfwbuilder.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libfwbuilder.

%prep
%setup -q
%patch0 -p1

%{__perl} -pi -e 's@/usr/lib/libresolv@/usr/%{_lib}/libresolv@' configure.in
%{__perl} -pi -e 's@/lib$@/%{_lib}@' qmake.inc.in

%build
export QTDIR="%{_usr}"
export QMAKESPEC="%{_datadir}/qt/mkspecs/linux-g++"

cp -f /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure \
	--with-templatedir=%{_datadir}/%{name}
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
%attr(755,root,root) %{_bindir}/libfwbuilder-config-%{_majver}.%{_minver}
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/fwb-%{_majver}.%{_minver}
