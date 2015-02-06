%define	name	cproto
%define	version	4.7g
%define release 2

Summary:	Generates function prototypes and variable declarations from C code
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		Development/C
Url:		http://sourceforge.net/projects/cproto/
Source0:	ftp://invisible-island.net/cproto/%{name}-%{version}.tgz
BuildRequires:	byacc flex
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Cproto generates function prototypes and variable declarations from
C source code.  Cproto can also convert function definitions between the
old style and the ANSI C style.  This conversion will overwrite the
original files, however, so be sure to make a backup copy of your original
files in case something goes wrong.  Since cproto uses a Yacc generated
parser, it shouldn't be confused by complex function definitions as much
as other prototype generators) because it uses a Yacc generated parser.  

Cproto will be useful for C programmers, so install cproto if you are going
to do any C programming.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall
mkdir $RPM_BUILD_ROOT%{_mandir}/man1
mv -f $RPM_BUILD_ROOT%{_mandir}/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README
%{_bindir}/cproto
%{_mandir}/*/cproto.1*


%changelog
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 4.7g-1mdv2011.0
+ Revision: 571836
- use configure2_5x

* Thu May 28 2009 Eugeni Dodonov <eugeni@mandriva.com> 4.7g-1mdv2010.0
+ Revision: 380560
- Updated to 4.7g.

* Mon Sep 01 2008 Olivier Blin <oblin@mandriva.com> 4.7f-1mdv2009.0
+ Revision: 278133
- 4.7f

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 4.7e-3mdv2009.0
+ Revision: 243704
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 4.7e-1mdv2008.1
+ Revision: 136345
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix summary-ended-with-dot

* Thu Apr 19 2007 Olivier Blin <oblin@mandriva.com> 4.7e-1mdv2008.0
+ Revision: 15011
- 4.7e
- Import cproto



* Thu Jul 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 4.7c-1mdk
- 4.7c
- drop patch that wasn't applied
- drop useless prefix
- cosmetics
- no .bz2 ending in %%files list for man pages

* Fri Dec 12 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 4.6-11mdk
- rebuild

* Fri Sep 20 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 4.6-10mdk
- meuh-rebuild

* Fri Sep 07 2001 Stefan van der Eijk <stefan@eijk.nu> 4.6-9mdk
- BuildRequires: byacc flex
- Copyright --> License

* Thu Dec 27 2000 Letoquart Gregory <gletoquart@mandrakesoft.com> 4.6-8mdk
- Rebuild after six month

* Thu Dec 27 2000 Letoquart Gregory <gletoquart@mandrakesoft.com> 4.6-7mdk
- New ftp & website

* Wed Aug 09 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.6-6mdk
- rebuild for macros Stefan: the patch didn't work ... :-(

* Fri Mar 17 2000 Enzo Maggi <enzo@mandrakesoft.com> 4.6-5mdk
- fixed a bug related to the C preprocessor used (CPP)

* Thu Nov 11 1999 Jeff Garzik <jgarzik@mandrakesoft.com>
- Correct spec filename to version 4.6
- Oxygen release

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 2)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- update to 4.6.1 (#1516).
- use %%configure

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
