%global tl_name contour
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.14
Release:	%{tl_revision}.1
Summary:	Print a coloured contour around text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/contour
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/contour.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package generates a coloured contour around a given text in order
to enable printing text over a background without the need of a coloured
box around the text.

