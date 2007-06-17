# $Id$

# Authority: dries
# Upstream: Michael Robinton <michael$bizsystems,com>

%define real_name Net-DNS-ToolKit
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Routines to pick apart, examine and put together DNS packets
Name: perl-Net-DNS-ToolKit
Version: 0.26
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-DNS-ToolKit/

Source: http://www.cpan.org/modules/by-module/Net/Net-DNS-ToolKit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Routines to pick apart, examine and put together DNS packets. They can
be used for diagnostic purposes or as building blocks for DNS
applications such as DNS servers and clients or to allow user
applications to interact directly with remote DNS servers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Net/DNS/ToolKit.pm
%{perl_vendorarch}/Net/DNS/ToolKit
%{perl_vendorarch}/auto/Net/DNS/ToolKit

%changelog
* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.25-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Updated to release 0.25.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.24-1
- Updated to release 0.24.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 0.23-1
- Updated to release 0.23.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
