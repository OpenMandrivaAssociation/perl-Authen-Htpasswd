%define realname Authen-Htpasswd
%define name	perl-%{realname}
%define	modprefix Authen
%define version	0.16
%define release	%mkrel 4

Summary:	Interface to read and modify Apache .htpasswd files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{realname}-%{version}.tar.bz2
Patch0:		Authen-Htpasswd-0.16-bug27012.diff
Patch1:		Authen-Htpasswd-0.16-bug37785.diff
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Digest)
BuildRequires:	perl(IO::LockedFile)
BuildRequires:	perl(Crypt::PasswdMD5)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides a convenient, object-oriented interface to Apache-style
.htpasswd files. It supports passwords encrypted via MD5, SHA1, and crypt, as
well as plain (cleartext) passwords. It requires Crypt::PasswdMD5 for MD5 and
Digest::SHA1 for SHA1. 

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p0
%patch1 -p0

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



