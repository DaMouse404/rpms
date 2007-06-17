# $Id$
# Authority: dries
# Upstream: <xern$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-PT-Stemmer

Summary: Galician Stemmer
Name: perl-Lingua-PT-Stemmer
Version: 0.01
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-PT-Stemmer/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-PT-Stemmer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Stemmers for Portuguese and Galician.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/GL/
%{perl_vendorlib}/Lingua/GL/Stemmer.pm
%{perl_vendorlib}/Lingua/PT/Stemmer.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
