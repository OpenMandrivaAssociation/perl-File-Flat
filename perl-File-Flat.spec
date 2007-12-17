%define real_name File-Flat

Summary:	Perl module that implements a flat filesystem 
Name:		perl-%{real_name}
Version:	1.02
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{real_name}-%{version}.tar.bz2
Requires:	perl-prefork >= 0.02
%if %mdkversion < 200600
BuildRequires:	perl-devel
%endif
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

%description
File::Flat implements a flat filesystem. A flat filesystem is a
filesystem in which directories do not exist. It provides an abstraction
over any normal filesystem which makes it appear as if directories do
not exist. In effect, it will automatically create directories as
needed. This is create for things like install scripts and such, as you
never need to worry about the existance of directories, just write to a
file, no matter where it is.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/File/Flat.pm
%{_mandir}/*/*


