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
%define _svnrev r26065
%define branch trunk

#
# Basic descriptive tags for this package:
#
Name:       mythtv-themes
Summary:    Additional themes for mythtv's frontend
URL:        http://www.mythtv.org/
Group:      Applications/Multimedia
License:    GPLv2

# Version/Release info
Version: 0.24
%if "%{branch}" == "trunk"
Release: 0.1.svn.%{_svnrev}%{?dist}
%else
Release: 1%{?dist}
%endif

################################################################################

# Tarballs created from svn directories, should be formal tarballs after release
# Source0 is http://www.mythtv.org/download/themes/0.23, which redirects to
# the primary download mirror at osuosl.rg
Source0:        ftp://ftp.osuosl.org/pub/mythtv/myththemes-%{version}.tar.bz2
# Robert Siebert's user-contributed theme, included at his (and users') request
Source1:	ftp://miroku.no-ip.com/blue-abstract-wide.2010.07.15.tar.bz2
# svnfixes branch patch
#Patch0:		myththemes-0.23-svnfixes.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

################################################################################

BuildRequires:  mythtv-devel = %{version}
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
%setup -q -c -a 1
cd myththemes-%{version}
# Patch is currently empty after 0.23.1 rebase
#patch0 -p1
cd ..

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
# move font files to more appropriate locations
mkdir -p %{buildroot}%{_datadir}/fonts/%{name}
mv %{buildroot}%{_datadir}/mythtv/themes/Arclight/*.otf \
	%{buildroot}%{_datadir}/fonts/%{name}/
cd ..

cp -a blue-abstract-wide %{buildroot}%{_datadir}/mythtv/themes/

################################################################################

%clean
rm -rf %{buildroot}

################################################################################

%post
%{_bindir}/fc-cache -f

%files
%defattr(-,root,root,-)
%{_datadir}/mythtv/themes/*
%dir %{_datadir}/fonts/%{name}
%{_datadir}/fonts/%{name}/*.otf

%changelog
* Wed Sep 01 2010 Jarod Wilson <jarod@wilsonet.com> 0.24-0.1.svn.r26065
- Update to svn trunk, rev 26065

* Sat Aug 28 2010 Jarod Wilson <jarod@wilsonet.com> 0.23.1-1
- Update to 0.23.1 + svnfixes at revision 25902

* Tue Jul 20 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-2
- Update to 0-23-release-fixes at svn revision 25830
- Include user-contributed blue-abstract-wide theme, 2010.07.15 edition

* Mon May 10 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-1
- Update to 0.23 release (svn rev 24509)

* Fri May 07 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.7.rc3
- Update to post-rc3 svn snapshot, revision 24473

* Tue May 04 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.6.rc3
- Update to post-rc3 svn snapshot, revision 24414
- Includes addition of theming contest winner "Childish"

* Fri Apr 16 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.5.rc2
- Update to post-rc2 svn snapshot, revision 24159

* Tue Apr 06 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.4.rc2
- Update to post-rc2 svn snapshot, revision 24014

* Thu Apr 01 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.3.rc1
- Update to post-rc1 snapshot
- Start tracking release-0-23-fixes branch

* Tue Mar 23 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.2.rc1
- Update to svn trunk, revision 23781, aka MythTV 0.23 RC1 (more or less)

* Tue Mar 09 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.1.svn.r23702
- Update to pre-0.23 svn trunk, rev 23702

* Thu Mar 04 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.1.svn.r23662
- Update to pre-0.23 svn trunk, rev 23662

* Sun Feb 28 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.1.svn.r23627
- Update to pre-0.23 svn trunk, rev 23627

* Fri Feb 05 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.1.svn.r23586
- Update to pre-0.23 svn trunk, rev 23586

* Fri Feb 05 2010 Jarod Wilson <jarod@wilsonet.com> 0.23-0.1.svn.r23479
- Update to pre-0.23 svn trunk, rev 23479
- Add hacky install of Arclight themes, still needs to be done Right

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

