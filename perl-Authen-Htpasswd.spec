%define upstream_name    Authen-Htpasswd
%define upstream_version 0.161

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Interface to read and modify Apache .htpasswd files
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Digest)
BuildRequires:	perl(IO::LockedFile)
BuildRequires:	perl(Crypt::PasswdMD5)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a convenient, object-oriented interface to Apache-style
.htpasswd files. It supports passwords encrypted via MD5, SHA1, and crypt, as
well as plain (cleartext) passwords. It requires Crypt::PasswdMD5 for MD5 and
Digest::SHA1 for SHA1. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Authen
