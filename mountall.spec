# TODO
# - system libnih, remove noautoreq when done
Summary:	Filesystem mounting tool
Name:		mountall
Version:	1.0.2
Release:	0.3
License:	GPL v2+
Group:		Base
Source0:	https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{version}.tar.gz
# Source0-md5:	1af4bd5309ffda85c5788236997df465
URL:		https://launchpad.net/ubuntu/+source/mountall
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	gettext-devel
BuildRequires:	libnih-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	udev-devel >= 146
Requires:	upstart >= 0.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Filter GLIBC_PRIVATE Requires
%define		_noautoreq	(GLIBC_PRIVATE)

%define		_sbindir	/sbin

%description
mountall mounts filesystems when the underlying block devices are
ready, or when network interfaces come up, checking the filesystems
first.

%prep
%setup -qn %{name}

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	NIH_DBUS_TOOL=nih-dbus-tool
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/init/mountall*.conf
%attr(755,root,root) %{_sbindir}/mountall
%{_mandir}/man8/mountall.8*
