%define	name	cproto
%define	version	4.7e
%{expand:%%define o_ver %(echo %{version}| sed "s#\.#_#g")}
%define release %mkrel 1

Summary:	Generates function prototypes and variable declarations from C code
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Public Domain
Group:		Development/C
Url:		http://sourceforge.net/projects/cproto/
Source0:	ftp://invisible-island.net/cproto/%{name}-%{o_ver}.tar.bz2
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
%setup -q -n %{name}-%{o_ver}

%build
%configure --exec-prefix=%{_prefix}
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
