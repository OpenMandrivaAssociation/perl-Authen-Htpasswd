%define realname Authen-Htpasswd
%define name	perl-%{realname}
%define	modprefix Authen

%define version	0.14
%define release	%mkrel 5

Summary:	Interface to read and modify Apache .htpasswd files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Digest)
BuildRequires:	perl(IO::LockedFile)
BuildRequires:  perl(Module::Build)
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
This module provides a convenient, object-oriented interface to Apache-style
.htpasswd files. It supports passwords encrypted via MD5, SHA1, and crypt, as
well as plain (cleartext) passwords. It requires Crypt::PasswdMD5 for MD5 and
Digest::SHA1 for SHA1. 

%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}



