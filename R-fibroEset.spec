%global packname  fibroEset
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.4.6
Release:          1
Summary:          exprSet for Karaman et al. (2003) fibroblasts data
Group:            Sciences/Mathematics
License:          LGPL
URL:              None
Source0:          http://bioconductor.org/packages/data/experiment/src/contrib/fibroEset_1.4.6.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-Biobase 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-Biobase

%description
exprSet for Karaman et al. (2003) human, bonobo and gorilla fibroblasts

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
