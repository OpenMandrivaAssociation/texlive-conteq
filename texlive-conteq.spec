%global tl_name conteq
%global tl_revision 37868

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.1
Release:	%{tl_revision}.1
Summary:	Typeset multiline continued equalities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/conteq
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an environment conteq, which will lay out systems
of continued equalities (or inequalities). Several variant layouts of
the equalities are provided, and the user may define their own. The
package is written using LaTeX 3 macros.

