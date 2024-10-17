Name:		texlive-kinematikz
Version:	61392
Release:	2
Summary:	Design kinematic chains and mechanisms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kinematikz
License:	lppl1.3 gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kinematikz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kinematikz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides functionalities to draw kinematic
diagrams for mechanisms using dedicate symbols (some from the
ISO standard and others). The intention is not to represent CAD
mechanical drawings of mechanisms and robots, but only to
represent 2D and 3D kinematic chains. The package provides
links, joints and other symbols, mostly in the form of TikZ pic
objects. These pics can be placed in the canvas either by a
central point for joints, and start and end points for some
links.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/kinematikz
%doc %{_texmfdistdir}/doc/latex/kinematikz

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
