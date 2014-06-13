# revision 30746
# category Package
# catalog-ctan /macros/latex/contrib/conteq
# catalog-date 2013-05-26 18:29:07 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-conteq
Version:	0.1
Release:	6
Summary:	Typeset multiline continued equalities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/conteq
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/conteq.source.tar.xz
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
%{_texmfdistdir}/tex/latex/conteq/conteq.sty
%doc %{_texmfdistdir}/doc/latex/conteq/README
%doc %{_texmfdistdir}/doc/latex/conteq/README.txt
%doc %{_texmfdistdir}/doc/latex/conteq/conteq.hd
%doc %{_texmfdistdir}/doc/latex/conteq/conteq.pdf
#- source
%doc %{_texmfdistdir}/source/latex/conteq/conteq.dtx
%doc %{_texmfdistdir}/source/latex/conteq/conteq.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
