%define module Authen-Htpasswd
%define name	perl-%{module}
%define	modprefix Authen
%define version	0.16.1
%define up_version  0.161
%define release	%mkrel 1

Summary:	Interface to read and modify Apache .htpasswd files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Authen/%{module}-%{up_version}.tar.gz
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Digest)
BuildRequires:	perl(IO::LockedFile)
BuildRequires:	perl(Crypt::PasswdMD5)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides a convenient, object-oriented interface to Apache-style
.htpasswd files. It supports passwords encrypted via MD5, SHA1, and crypt, as
well as plain (cleartext) passwords. It requires Crypt::PasswdMD5 for MD5 and
Digest::SHA1 for SHA1. 

%prep
%setup -q -n %{module}-%{up_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

%clean
rm -rf %{buildroot}



