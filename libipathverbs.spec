%global dracutdir %{_prefix}/share/dracut/modules.d

Name: libipathverbs
Version: 1.3
Release: 3%{?dist}
Summary: QLogic InfiniPath HCA Userspace Driver
Group: System Environment/Libraries
License: GPLv2 or BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/%{name}/%{name}-%{version}.tar.gz
Patch0: libipathverbs-1.3-modprobe.patch
Patch1: libipathverbs-1.3-dracut.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libibverbs-devel >= 1.1.3, valgrind-devel, dracut
#BuildRequires:autoconf, automake, libtool
ExclusiveArch: x86_64
Obsoletes: %{name}-devel
Provides: libibverbs-driver.%{_arch}
Requires: /bin/bash
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
#./autogen.sh
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
* Thu Sep 11 2014 Doug Ledford <dledford@redhat.com> - 1.3-3
- Add missing files to dracut install command, including bash
  as the truescale-serdes.cmds will not work with dash and
  can not be reasonably ported to dash.
- Related: bz1024903

* Thu Aug 07 2014 Doug Ledford <dledford@redhat.com> - 1.3-2
- The modprobe file needs a full path or else modprobe fails
- Related: bz1024903

* Wed Jul 30 2014 Doug Ledford <dledford@redhat.com> - 1.3-1
- Pick up real upstream tarball release
- Related: bz1024903

* Thu Jul 24 2014 Doug Ledford <dledford@redhat.com> - 1.2-6
- Bump and rebuild against latest libibverbs
- Related: bz1024903

* Wed Jul 23 2014 Doug Ledford <dledford@redhat.com> - 1.2-5
- Update to git repo archive from upstream
- Add truescale-serdes.cmds and related code from git archive
- Resolves: bz1024903

* Mon Jan 23 2012 Doug Ledford <dledford@redhat.com> - 1.2-4
- Bump and rebuild against latest libibverbs
- Related: bz750609

* Mon Jul 25 2011 Doug Ledford <dledford@redhat.com> - 1.2-3.el6
- Add missing arch macro to libibverbs-driver provide
- Related: bz725016

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

