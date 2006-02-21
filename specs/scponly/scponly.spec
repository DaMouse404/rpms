# $Id$
# Authority: dag

Summary: Limited shell for secure file transfers
Name: scponly
Version: 4.6
Release: 1
License: GPL
Group: System Environment/Shells
URL: http://sublimation.org/scponly/

Source: http://sublimation.org/scponly/scponly-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssh >= 3.4, perl, openssh-server, openssh-clients

%description
scponly is an alternative 'shell' for system administrators 
who would like to provide access to remote users to both 
read and write local files without providing any remote 
execution priviledges. Functionally, it is best described 
as a wrapper to the "tried and true" ssh suite of applications. 

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} \
	OPTS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 scponly %{buildroot}%{_bindir}/scponly
%{__install} -Dp -m0644 scponly.8 %{buildroot}%{_mandir}/man8/scponly.8

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc AUTHOR CHANGELOG CONTRIB COPYING INSTALL README TODO
%doc %{_mandir}/man8/scponly.8*
%{_bindir}/scponly

%changelog
* Tue Feb 21 2006 Matthias Saou <http://freshrpms.net/> 4.6-1
- Update to 4.6.

* Tue May 10 2005 Dag Wieers <dag@wwieers.com> - 4.1-1
- Updated to release 4.1.

* Thu Mar 03 2005 Dag Wieers <dag@wwieers.com> - 4.0-1
- Initial package. (using DAR)

