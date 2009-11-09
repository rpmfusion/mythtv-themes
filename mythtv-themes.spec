#
# Specfile for building MythTV RPMs from a subversion checkout.
#
# by:   Chris Petersen <rpm@forevermore.net>
#       Jarod Wilson <jarod@wilsonet.com>
#
#  Modified/Extended from the great (non-svn based) work of:
#     Axel Thimm <Axel.Thimm@ATrpms.net>
#     and others; see changelog at bottom for details.
#
# The latest version of this file can be found at:
#
#     http://www.mythtv.org/wiki/index.php/Mythtv-themes-svn-rpmbuild.spec
#

# The vendor name we should attribute the aforementioned entries to
%define desktop_vendor  RPMFusion

# SVN Revision number and branch ID
%define _svnrev r22752
%define branch release

#
# Basic descriptive tags for this package:
#
Name:       mythtv-themes
Summary:    Additional themes for mythtv's frontend
URL:        http://www.mythtv.org/
Group:      Applications/Multimedia
License:    GPLv2

# Version/Release info
Version: 0.22
%if "%{branch}" == "trunk"
Release: 0.1.rc2%{?dist}
#Release: 0.5.svn.%{_svnrev}%{?dist}
%else
Release: 1%{?dist}
%endif

################################################################################

# Tarballs created from svn directories, should be formal tarballs after release
#Source0:        http://www.mythtv.org/mc/mythtv-themes-%{version}.tar.bz2
Source0:        myththemes-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

################################################################################

BuildRequires:  libmyth-devel = %{version}
BuildRequires:  qt4-devel

# Themes do require a frontend
Requires:       mythtv-frontend

# And obselete a bunch of packages from when themes were packaged individually
Obsoletes:      mythtv-theme-MythCenter
Obsoletes:      mythtv-theme-Retro
Obsoletes:      mythtv-theme-Titivillus
Obsoletes:      mythtv-theme-isthmus

################################################################################

%description
MythTV provides a unified graphical interface for recording and viewing
television programs.  Refer to the mythtv-docs package for more information.

This package contains additional themes for the mythtv user interface.

################################################################################

%prep
%setup -q -c

################################################################################

%build
cd myththemes-%{version}
%configure
cd ..

################################################################################

%install
rm -rf %{buildroot}

cd myththemes-%{version}
make install INSTALL_ROOT=%{buildroot}
cd ..

################################################################################

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%{_datadir}/mythtv/themes/*

%changelog
* Mon Nov 09 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-1
- Update to 0.22 release

* Sat Oct 31 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-0.9.rc2
- Update to 0.22-rc2

* Wed Oct 14 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.6.rc1
- Update to 0.22-rc1
- Drop oldthemes and unofficial themes at upstream's request, after
  verifying we'll gracefully fall back to a stock theme now

* Sun Oct 11 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.5.svn.r22366
- Update to pre-0.22 svn trunk, rev 22366
- Add back in new incarnation myththemes

* Wed Sep 16 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.5.svn.r21902
- Update to pre-0.22 svn trunk, rev 21902

* Fri Sep 11 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.5.svn.r21778
- The myththemes tarball is actually what become oldthemes. Oops.

* Fri Sep 11 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.4.svn.r21778
- Update to pre-0.22 svn trunk, rev 21778
- Add back old themes not fully updated for 0.22 yet

* Wed Sep 09 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.4.svn.r21745
- Update to pre-0.22 svn trunk, rev 21745

* Sun Sep 06 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.4.svn.r21685
- Update to pre-0.22 svn trunk, rev 21685

* Sat Aug 29 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.4.svn.r21591
- Update to pre-0.22 svn trunk, rev 21591
- Graphite is now an official theme included in mythtv svn

* Sat Aug 08 2009 Jarod Wilson <jarod@wilsonet.com> - 0.22-0.4.svn.r21179
- Update to pre-0.22 svn trunk, rev 21179
- Add Robert McNamara's excellent new Graphite theme

* Fri Jun 05 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.22-0.4.svn.r20488
- rebuilt

* Tue May 05 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.22-0.3.svn.r20488
- excludearch ppc64 to fix broken deps in RPM Fusions ppc64 repo

* Mon May 04 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-0.2.svn.r20488
- Update to pre-0.22 svn trunk, rev 20488

* Fri Apr 24 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-0.2.svn.r20448
- Update to pre-0.22 svn trunk, rev 20448

* Tue Apr 07 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-0.2.svn.r20317
- Update to pre-0.22 svn trunk, rev 20317

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.22-0.2.svn.r20196
- rebuild for new F11 features

* Thu Mar 12 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-0.1.svn.r20196
- Update to pre-0.22 svn trunk, rev 20196

* Wed Mar 04 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-0.1.svn.r20107
- Update to pre-0.22 svn trunk, rev 20107

* Mon Mar 02 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-0.1.svn.r20089
- Update to pre-0.22 svn trunk, rev 20089

* Sat Jan 24 2009 Jarod Wilson <jarod@wilsonet.com> 0.22-0.1.svn.r19811
- Update to pre-0.22 svn trunk, rev 19811

* Wed Dec 31 2008 Jarod Wilson <jarod@wilsonet.com> 0.22-0.1.svn.r19506
- Update to pre-0.22 svn trunk, rev 19506

* Wed Dec 17 2008 Jarod Wilson <jarod@wilsonet.com> 0.22-0.1.svn.r19390
- Build svn trunk themes to go with svn trunk mythtv, rev 19390
- Drop glass-wide

* Sat Nov 01 2008 Chris Petersen <rpm@forevermore.net> 0.22-0.1.svn
- Clean and standardize package to match mythtv-svn spec

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.21-3
- rebuild

* Fri Jul 18 2008 Jarod Wilson <jarod@wilsonet.com> - 0.21-2
- Drop %%dist tag, this is noarch
- Patch in changes from release-0-21-fixes svn branch
- Add glass-wide

* Sun Mar 09 2008 Jarod Wilson <jarod@wilsonet.com> - 0.21-1
- Initial package

