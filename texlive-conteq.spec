Name:		texlive-conteq
Version:	37868
Release:	2
Summary:	Typeset multiline continued equalities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/conteq
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an environment conteq, which will lay out
systems of continued equalities (or inequalities). Several
variant layouts of the equalities are provided, and the user
may define their own. The package is written use LaTeX 3
macros.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/conteq
%doc %{_texmfdistdir}/doc/latex/conteq
#- source
%doc %{_texmfdistdir}/source/latex/conteq

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
