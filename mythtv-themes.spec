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
%define _svnrev r20317
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
Version: 0.22
%if "%{branch}" == "trunk"
Release: 0.2.svn.%{_svnrev}%{?dist}
%else
Release: 1%{?dist}
%endif

################################################################################

# Tarballs created from svn "themes" and "myththemes" directories
# Hopefully these will merge before 0.22 is released.
Source0:        http://www.mythtv.org/mc/myththemes-%{version}.tar.bz2
Source1:        themes-%{version}.tar.bz2

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
%setup -q -c -a 1

################################################################################

%build
cd myththemes-%{version}
%configure
cd ..

cd themes-%{version}
%configure
cd ..

################################################################################

%install
rm -rf %{buildroot}

cd myththemes-%{version}
make install INSTALL_ROOT=%{buildroot}
cd ..

cd themes-%{version}
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

