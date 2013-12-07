# revision 18950
# category Package
# catalog-ctan /macros/latex/contrib/contour
# catalog-date 2006-12-09 15:50:57 +0100
# catalog-license lppl
# catalog-version 2.14
Name:		texlive-contour
Version:	2.14
Release:	4
Summary:	Print a coloured contour around text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/contour
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.14-2
+ Revision: 750544
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.14-1
+ Revision: 718147
- texlive-contour
- texlive-contour
- texlive-contour
- texlive-contour

