Summary:	Generates function prototypes and variable declarations from C code
Name:		cproto
Version:	4.7r
Release:	1
License:	Public Domain
Group:		Development/C
Url:		https://invisible-island.net/cproto/
Source0:	https://invisible-island.net/datafiles/release/%{name}.tar.gz
BuildRequires:	byacc
BuildRequires:	flex


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
%autosetup -p1

%build
%configure
%make_build

%install
%make_install


%files
%doc CHANGES README
%{_bindir}/cproto
%{_mandir}/*/cproto.1*
