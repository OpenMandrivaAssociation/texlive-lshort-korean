# revision 15878
# category Package
# catalog-ctan /info/lshort/korean
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license fdl
# catalog-version 4.17
Name:		texlive-lshort-korean
Version:	4.17
Release:	1
Summary:	Korean introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/korean
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-korean.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-korean.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A translation of Oetiker's original (not so) short
introduction.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-korean/README.ko
%doc %{_texmfdistdir}/doc/latex/lshort-korean/lshort-kr-src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-korean/lshort-kr.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
