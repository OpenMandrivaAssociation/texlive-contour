Name:		texlive-contour
Version:	18950
Release:	2
Summary:	Print a coloured contour around text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/contour
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package generates a coloured contour around a given text
in order to enable printing text over a background without the
need of a coloured box around the text.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/contour/contour.cfg
%{_texmfdistdir}/tex/latex/contour/contour.sty
%{_texmfdistdir}/tex/latex/contour/dvips.cnt
%{_texmfdistdir}/tex/latex/contour/dvipsone.cnt
%{_texmfdistdir}/tex/latex/contour/pdftex.cnt
%{_texmfdistdir}/tex/latex/contour/vtex.cnt
%doc %{_texmfdistdir}/doc/latex/contour/ChangeLog
%doc %{_texmfdistdir}/doc/latex/contour/Makefile
%doc %{_texmfdistdir}/doc/latex/contour/README
%doc %{_texmfdistdir}/doc/latex/contour/contour.pdf
%doc %{_texmfdistdir}/doc/latex/contour/contourtest.tex
#- source
%doc %{_texmfdistdir}/source/latex/contour/contour.dtx
%doc %{_texmfdistdir}/source/latex/contour/contour.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
