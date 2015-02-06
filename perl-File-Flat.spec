%define upstream_name    File-Flat
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module that implements a flat filesystem 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-AutoInstall >= 0.49
BuildRequires:	perl-prefork >= 0.02
BuildRequires:	perl-File-NCopy >= 0.32
BuildRequires:	perl(Test::More) >= 0.47
BuildRequires:	perl(Test::ClassAPI) >= 1.02
BuildRequires:	perl(File::Find) >= 1.0
BuildRequires:	perl(File::Spec) >= 0.85
BuildRequires:	perl(File::Copy) >= 2.08
BuildRequires:	perl(File::Copy::Recursive)
BuildRequires:	perl-File-Slurp >= 9999.04
BuildRequires:	perl(File::Remove) >= 0.21
BuildRequires:	perl(File::Temp) >= 0.14
BuildRequires:	perl(IO::File) >= 1.10
BuildRequires:  perl(File::Copy::Recursive)
BuildArch:	noarch
Requires:	perl-prefork >= 0.02

%description
File::Flat implements a flat filesystem. A flat filesystem is a
filesystem in which directories do not exist. It provides an abstraction
over any normal filesystem which makes it appear as if directories do
not exist. In effect, it will automatically create directories as
needed. This is create for things like install scripts and such, as you
never need to worry about the existance of directories, just write to a
file, no matter where it is.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/File/Flat.pm
%{_mandir}/*/*


%changelog
* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 407690
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.04-2mdv2009.0
+ Revision: 268508
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2009.0
+ Revision: 194851
- update to new version 1.04
- update to new version 1.04

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2008.1
+ Revision: 178290
- update to new version 1.03

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdv2008.1
+ Revision: 118549
- new version


* Sat Mar 03 2007 Olivier Thauvin <nanardon@mandriva.org> 1.00-1mdv2007.0
+ Revision: 131670
- buildrequires
- 1.00
- 0.96
- Import perl-File-Flat

* Sat Sep 24 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.95-2mdk
- Add Requires on perl-prefork

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.95-1mdk
- initial Mandriva package

