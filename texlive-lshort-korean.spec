# revision 15878
# category Package
# catalog-ctan /info/lshort/korean
# catalog-date 2006-08-27 16:41:02 +0100
# catalog-license fdl
# catalog-version 4.17
Name:		texlive-lshort-korean
Version:	4.17
Release:	11
Summary:	Korean introduction to LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/lshort/korean
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-korean.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lshort-korean.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A translation of Oetiker's original (not so) short
introduction.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/lshort-korean/README.ko
%doc %{_texmfdistdir}/doc/latex/lshort-korean/lshort-kr-src.tar.gz
%doc %{_texmfdistdir}/doc/latex/lshort-korean/lshort-kr.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.17-2
+ Revision: 753474
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 4.17-1
+ Revision: 718894
- texlive-lshort-korean
- texlive-lshort-korean
- texlive-lshort-korean
- texlive-lshort-korean

