Name: mythtv-themes
Version: 0.21
Release: 4
Summary: Additional User Interface themes for MythTV
Group: Applications/Multimedia
License: GPLv2
URL: http://www.mythtv.org/
Source0: http://www.mythtv.org/mc/myththemes-%{version}.tar.bz2
# created from svn rev 17859:
# http://svn.mythtv.org/var/lib/svn/branches/release-0-21-fixes/themes
Source1: themes-%{version}.tar.bz2
# Upstream url dead, extracted from mythbuntu packages
Source2: glass-wide-20071107.tar.gz
Patch0: myththemes-0.21-svnfixes.patch
BuildRequires: libmyth-devel = %{version}
Requires: mythtv-themes = %{version}
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
MythTV provides a unified graphical interface for recording and viewing
television programs.  Refer to the mythtv-docs package for more information.

This package contains themes for the mythtv user interface.

%prep
%setup -q -c -a 1 -a 2
cd myththemes-%{version}
%patch0 -p1
cd ..

%build
cd myththemes-%{version}
%configure
cd ..

cd themes-%{version}
%configure
cd ..

%install
rm -rf %{buildroot}

cd myththemes-%{version}
make install INSTALL_ROOT=%{buildroot}
cd ..

cd themes-%{version}
make install INSTALL_ROOT=%{buildroot}
cd ..

cp -rp glass-wide %{buildroot}%{_datadir}/mythtv/themes/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/mythtv/themes/*

%changelog
* Thu Jun 04 2009 Jarod Wilson <jarod@wilsonet.com> - 0.21-4
- Rebuild

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.21-3
- rebuild

* Fri Jul 18 2008 Jarod Wilson <jarod@wilsonet.com> - 0.21-2
- Drop %%dist tag, this is noarch
- Patch in changes from release-0-21-fixes svn branch
- Add glass-wide

* Sun Mar 09 2008 Jarod Wilson <jarod@wilsonet.com> - 0.21-1
- Initial package
