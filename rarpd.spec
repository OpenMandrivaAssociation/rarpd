Summary:	The RARP daemon
Name:		rarpd
Version:	ss981107
Release:	%mkrel 7
License:	GPL
Group:		System/Servers
URL:		ftp://ftp.inr.ac.ru/ip-routing/dhcp.bootp.rarp/
Source0:	rarpd-%{version}.tar.bz2
Patch0:		rarpd-%{version}.patch
Patch1:		rarpd-norun.patch
Patch2:		rarpd-ss981107-initscript.patch
Patch3:		rarpd-ss981107-override-tftpboot-dir.patch
Requires(post,preun):	rpm-helper
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
RARP (Reverse Address Resolution Protocol) is a protocol which allows
individual devices on an IP network to get their own IP addresses from the
RARP server.  Some machines (e.g. SPARC boxes) use this protocol instead
of e.g. DHCP to query their IP addresses during network bootup.
Linux kernels up to 2.2 used to provide a kernel daemon for this service,
but since 2.3 kernels it is served by this userland daemon.

You should install rarpd if you want to set up a RARP server on your
network.

%prep
%setup -q -n rarpd
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .initscript
%patch3 -p1 -b .tftpdir

%build
%make CFLAGS="%{optflags} -Wall -DTFTPDIR='\"%{_localstatedir}/lib/tftpboot\"'"

%install
rm -rf %{buildroot}

install -m755 rarpd.init -D %{buildroot}%{_initrddir}/rarpd
install -m755 rarpd -D %{buildroot}%{_sbindir}/rarpd
install -m644 rarpd.8 -D %{buildroot}%{_mandir}/man8/rarpd.8

%post
%_post_service %{name}

%preun
%_preun_service %{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%attr(0755,root,root) %{_initrddir}/rarpd
%{_sbindir}/rarpd
%{_mandir}/man8/*

