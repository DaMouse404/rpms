# $Id$
# Authority: dries
# Upstream: Sean M. Burke <sburke$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIDI-Perl

Summary: Read, compose, modify, and write MIDI files
Name: perl-MIDI-Perl
Version: 0.81
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIDI-Perl/

Source: http://search.cpan.org/CPAN/authors/id/S/SB/SBURKE/MIDI-Perl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
MIDI-Perl is a suite of Perl modules that allows you to read, compose,
modify, and write MIDI files.  It is largely object-oriented, but if
you follow the example code, you should be able to get along fine.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/MIDI.pm
%{perl_vendorlib}/MIDI

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.81-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.81-1
- Initial package.
