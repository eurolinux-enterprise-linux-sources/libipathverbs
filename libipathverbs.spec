%global dracutdir %{_prefix}/lib/dracut/modules.d

Name: libipathverbs
Version: 1.3
Release: 2%{?dist}
Summary: QLogic InfiniPath HCA Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
Patch0: libipathverbs-1.3-modprobe.patch
Patch1: libipathverbs-1.3-dracut.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel > 1.1.4, valgrind-devel, dracut
Requires: /bin/bash, rdma
ExclusiveArch: x86_64
Provides: libibverbs-driver.%{_arch}
%description
QLogic hardware driver for use with libibverbs user space verbs access
library.  This driver supports QLogic InfiniPath based cards.

%package static
Summary: Static version of the libipathverbs driver
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
%description static
Static version of libipathverbs that may be linked directly to an
application.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure --with-valgrind
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/*.so*
%{_sysconfdir}/libibverbs.d/*.driver
%{_sysconfdir}/modprobe.d/truescale.conf
%dir %{dracutdir}/90qib
%{dracutdir}/90qib/*
%{_sbindir}/truescale-serdes.cmds
%doc AUTHORS COPYING README

%files static
%defattr(-,root,root,-)
%{_libdir}/*.a

%changelog
* Tue Dec 23 2014 Doug Ledford <dledford@redhat.com> - 1.3-2
- Add requires on rdma package
- Related: bz1164618

* Fri Oct 17 2014 Doug Ledford <dledford@redhat.com> - 1.3-1
- Update to latest upstream release and build against latest libibverbs
- Resolve mezzanine configure issue (1085946)
- Related: bz1137044

* Mon Mar 03 2014 Doug Ledford <dledford@redhat.com> - 1.2-8
- Bump and rebuild against latest libibverbs
- Related: bz1062281

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2-7
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Doug Ledford <dledford@redhat.com> - 1.2-3
- Initial import into Fedora
- Fix pseudoprovide to match what the fedora libibverbs expects

* Mon Jan 25 2010 Doug Ledford <dledford@redhat.com> - 1.2-2.el6
- Minor updates for pkgwrangler review
- Related: bz543948

* Mon Dec 21 2009 Doug Ledford <dledford@redhat.com> - 1.2-1.el6
- Update to latest upstream source
- Change BuildRequires from valgrind to valgrind-devel for rhel6
- Drop ppc64 build as it isn't officially supported upstream
- Related: bz543948

* Mon Jun 22 2009 Doug Ledford <dledford@redhat.com> - 1.1-14.el5
- Rebuild against libibverbs that isn't missing the proper ppc wmb() macro
- Related: bz506258

* Sun Jun 21 2009 Doug Ledford <dledford@redhat.com> - 1.1-13.el5
- Build against non-XRC libibverbs
- Enabled valgrind annotations
- Related: bz506258, bz504284

* Fri Apr 17 2009 Doug Ledford <dledford@redhat.com> - 1.1-12
- Update source to ofed 1.4.1-rc3 version
- Related: bz459652

* Tue Sep 16 2008 Doug Ledford <dledford@redhat.com> - 1.1-11
- Bump and rebuild against libibverbs-1.1.2
- Resolves: bz451456

* Tue Apr 01 2008 Doug Ledford <dledford@redhat.com> - 1.1-10
- Update to the OFED 1.3 version of libipathverbs-1.1.tar.gz (there is a 300k
  size difference between the libipathverbs-1.1.tar.gz in the OFED release
  and the file by the same name at openfabrics.org/downloads/...which is
  just insane, they should have different release numbers, but they don't,
  so for anyone to duplicate what I have here, you will need to get the
  libipathverbs-1.1.tar.gz file out of the libipathverbs-1.1-1.ofed1.3 src
  rpm out of the OFED-1.3.tar.gz download at the openfabrics site)
- Related: bz428197

* Thu Feb 14 2008 Doug Ledford <dledford@redhat.com> - 1.1-9
- Obsolete the old -devel package
- Related: bz432765

* Thu Feb 07 2008 Doug Ledford <dledford@redhat.com> - 1.1-8
- Bump version to be higher than the OFED 1.2 libipathverbs and rebuild
- Related: bz428197

* Tue Jan 15 2008 Doug Ledford <dledford@redhat.com> - 1.1-0.1
- Initial import to CVS

