Summary:	The RARP daemon
Name:		rarpd
Version:	ss981107
Release:	%mkrel 8
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



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> ss981107-8mdv2010.0
+ Revision: 433057
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> ss981107-7mdv2009.0
+ Revision: 260045
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> ss981107-6mdv2009.0
+ Revision: 247887
- rebuild

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> ss981107-4mdv2008.1
+ Revision: 126470
- kill re-definition of %%buildroot on Pixel's request


* Sat Jan 14 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> ss981107-4mdk
- fix path to tftpboot (P3)
- clean initscript and add pinit support (P2, updated)
- cosmetics
- fix requires(post,preun)
- %%mkrel

* Mon Feb 21 2005 Oden Eriksson <oeriksson@mandrakesoft.com> ss981107-3mdk
- rebuild
- misc spec file fixes

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com ss981107-2mdk
- rebuild

