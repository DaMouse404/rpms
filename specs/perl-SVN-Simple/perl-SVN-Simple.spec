# $Id$
# Authority: dries
# Upstream: Chia-liang Kao <clkao$clkao,org>

%define real_name SVN-Simple
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Simple interface for delta editors
Name: perl-SVN-Simple
Version: 0.26
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Simple/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/SVN-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, subversion-perl

%description
SVN::Simple is a simple interface to subversion's editor interface.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/SVN/Simple/*.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/SVN/Simple/Edit/.packlist

%changelog
* Sun Nov 14 2004 Dries Verachtert <dries@ulyssis.org> - 0.26-1
- Updated to release 0.26.

* Wed Nov 03 2004 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
