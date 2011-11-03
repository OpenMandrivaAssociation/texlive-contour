# revision 18950
# category Package
# catalog-ctan /macros/latex/contrib/contour
# catalog-date 2006-12-09 15:50:57 +0100
# catalog-license lppl
# catalog-version 2.14
Name:		texlive-contour
Version:	2.14
Release:	1
Summary:	Print a coloured contour around text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/contour
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package generates a coloured contour around a given text
in order to enable printing text over a background without the
need of a coloured box around the text.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
