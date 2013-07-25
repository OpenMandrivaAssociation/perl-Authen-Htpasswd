%define upstream_name    Authen-Htpasswd
%define upstream_version 0.171

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.171
Release:	1

Summary:	Interface to read and modify Apache .htpasswd files
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Authen/Authen-Htpasswd-0.171.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Digest)
BuildRequires:	perl(IO::LockedFile)
BuildRequires:	perl(Crypt::PasswdMD5)
BuildArch:	noarch

%description
This module provides a convenient, object-oriented interface to Apache-style
.htpasswd files. It supports passwords encrypted via MD5, SHA1, and crypt, as
well as plain (cleartext) passwords. It requires Crypt::PasswdMD5 for MD5 and
Digest::SHA1 for SHA1. 

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
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Authen


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.161.0-2mdv2011.0
+ Revision: 680484
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.161.0-1mdv2011.0
+ Revision: 406255
- rebuild using %%perl_convert_version

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.16.1-1mdv2009.1
+ Revision: 294783
- new version
- drop patches (merged)

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 0.16-4mdv2009.0
+ Revision: 290358
- fix two upstream bugs
- fix deps

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.0
+ Revision: 64000
- new version

* Sun Apr 29 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.15-1mdv2008.0
+ Revision: 19248
-New version


* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 01:27:16 (54275)
- Rebuild, spec file cleanup

* Tue Aug 08 2006 Scott Karns <scottk@mandriva.org>
+ 2006-08-08 01:20:16 (54273)
- import perl-Authen-Htpasswd-0.14-4mdk

* Wed May 03 2006 Scott Karns <socttk@mandriva.org> 0.14-4mdk
- Updated BuildRequires

* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.14-3mdk
- Fix SPEC Using perl Policies

* Sat Mar 25 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.14-2mdk
- Add BuildRequires

* Fri Mar 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.14-1mdk
- First Mandriva release


