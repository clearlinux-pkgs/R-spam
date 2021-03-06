#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-spam
Version  : 2.6.0
Release  : 42
URL      : https://cran.r-project.org/src/contrib/spam_2.6-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/spam_2.6-0.tar.gz
Summary  : SPArse Matrix
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 LGPL-2.0
Requires: R-spam-lib = %{version}-%{release}
Requires: R-dotCall64
Requires: R-fields
Requires: R-truncdist
BuildRequires : R-dotCall64
BuildRequires : R-fields
BuildRequires : R-truncdist
BuildRequires : buildreq-R

%description
Versions of `spam` prior to 1.00 included a LICENSE file that
described the license of some Fortran routines incompatible with the
general R philosophy.  The routines are in src/cholmodified.f.  For
the packages `SparseM` and `spam`, Esmond Ng and Barry Peyton have
very kindly given permission to use their routines under an open
source license (2012/03/09 and 2014/08/29).  They have requested that
their code be credited via the following two publications:

%package lib
Summary: lib components for the R-spam package.
Group: Libraries

%description lib
lib components for the R-spam package.


%prep
%setup -q -c -n spam
cd %{_builddir}/spam

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608162843

%install
export SOURCE_DATE_EPOCH=1608162843
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spam
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spam
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library spam
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc spam || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/spam/0LICENSE
/usr/lib64/R/library/spam/CITATION
/usr/lib64/R/library/spam/DESCRIPTION
/usr/lib64/R/library/spam/INDEX
/usr/lib64/R/library/spam/LICENSE
/usr/lib64/R/library/spam/Meta/Rd.rds
/usr/lib64/R/library/spam/Meta/data.rds
/usr/lib64/R/library/spam/Meta/demo.rds
/usr/lib64/R/library/spam/Meta/features.rds
/usr/lib64/R/library/spam/Meta/hsearch.rds
/usr/lib64/R/library/spam/Meta/links.rds
/usr/lib64/R/library/spam/Meta/nsInfo.rds
/usr/lib64/R/library/spam/Meta/package.rds
/usr/lib64/R/library/spam/Meta/vignette.rds
/usr/lib64/R/library/spam/NAMESPACE
/usr/lib64/R/library/spam/NEWS.md
/usr/lib64/R/library/spam/R/spam
/usr/lib64/R/library/spam/R/spam.rdb
/usr/lib64/R/library/spam/R/spam.rdx
/usr/lib64/R/library/spam/data/Rdata.rdb
/usr/lib64/R/library/spam/data/Rdata.rds
/usr/lib64/R/library/spam/data/Rdata.rdx
/usr/lib64/R/library/spam/demo/article-jss-example1.R
/usr/lib64/R/library/spam/demo/article-jss-example2.R
/usr/lib64/R/library/spam/demo/article-jss.R
/usr/lib64/R/library/spam/demo/cholesky.R
/usr/lib64/R/library/spam/demo/jss10-example1.R
/usr/lib64/R/library/spam/demo/jss10-example2.R
/usr/lib64/R/library/spam/demo/jss15-BYM.R
/usr/lib64/R/library/spam/demo/jss15-Leroux.R
/usr/lib64/R/library/spam/demo/spam.R
/usr/lib64/R/library/spam/demo/timing.R
/usr/lib64/R/library/spam/demodata/germany.adjacency
/usr/lib64/R/library/spam/doc/index.html
/usr/lib64/R/library/spam/doc/jss15.pdf
/usr/lib64/R/library/spam/doc/jss15.pdf.asis
/usr/lib64/R/library/spam/doc/spam.R
/usr/lib64/R/library/spam/doc/spam.Rmd
/usr/lib64/R/library/spam/doc/spam.pdf
/usr/lib64/R/library/spam/help/AnIndex
/usr/lib64/R/library/spam/help/aliases.rds
/usr/lib64/R/library/spam/help/figures/germanyadjacency.png
/usr/lib64/R/library/spam/help/paths.rds
/usr/lib64/R/library/spam/help/spam.rdb
/usr/lib64/R/library/spam/help/spam.rdx
/usr/lib64/R/library/spam/html/00Index.html
/usr/lib64/R/library/spam/html/R.css
/usr/lib64/R/library/spam/tests/demo_article-jss-example1.R
/usr/lib64/R/library/spam/tests/demo_article-jss-example1.Rout.save
/usr/lib64/R/library/spam/tests/demo_article-jss-example2.R
/usr/lib64/R/library/spam/tests/demo_article-jss-example2.Rout.save
/usr/lib64/R/library/spam/tests/demo_article-jss.R
/usr/lib64/R/library/spam/tests/demo_article-jss.Rout.save
/usr/lib64/R/library/spam/tests/demo_cholesky.R
/usr/lib64/R/library/spam/tests/demo_cholesky.Rout.save
/usr/lib64/R/library/spam/tests/demo_jss15-BYM.R
/usr/lib64/R/library/spam/tests/demo_jss15-BYM.Rout.save
/usr/lib64/R/library/spam/tests/demo_jss15-Leroux.R
/usr/lib64/R/library/spam/tests/demo_jss15-Leroux.Rout.save
/usr/lib64/R/library/spam/tests/demo_spam.R
/usr/lib64/R/library/spam/tests/demo_spam.Rout.save
/usr/lib64/R/library/spam/tests/demo_timing.R
/usr/lib64/R/library/spam/tests/demo_timing.Rout.save
/usr/lib64/R/library/spam/tests/jss_areal_counts.R
/usr/lib64/R/library/spam/tests/jss_areal_counts.Rout.save
/usr/lib64/R/library/spam/tests/testthat.R
/usr/lib64/R/library/spam/tests/testthat/helper.R
/usr/lib64/R/library/spam/tests/testthat/test-constructors.R
/usr/lib64/R/library/spam/tests/testthat/test-covmat.R
/usr/lib64/R/library/spam/tests/testthat/test-crossprod.R
/usr/lib64/R/library/spam/tests/testthat/test-diff.R
/usr/lib64/R/library/spam/tests/testthat/test-dim.R
/usr/lib64/R/library/spam/tests/testthat/test-dist.R
/usr/lib64/R/library/spam/tests/testthat/test-eigen.R
/usr/lib64/R/library/spam/tests/testthat/test-helper.R
/usr/lib64/R/library/spam/tests/testthat/test-kronecker.R
/usr/lib64/R/library/spam/tests/testthat/test-math.R
/usr/lib64/R/library/spam/tests/testthat/test-mle.R
/usr/lib64/R/library/spam/tests/testthat/test-ops.R
/usr/lib64/R/library/spam/tests/testthat/test-overall.R
/usr/lib64/R/library/spam/tests/testthat/test-permutation.R
/usr/lib64/R/library/spam/tests/testthat/test-profile.R
/usr/lib64/R/library/spam/tests/testthat/test-random.R
/usr/lib64/R/library/spam/tests/testthat/test-rep_len64.R
/usr/lib64/R/library/spam/tests/testthat/test-rowcolstats.R
/usr/lib64/R/library/spam/tests/testthat/test-solve.R
/usr/lib64/R/library/spam/tests/testthat/test-spamlist.R
/usr/lib64/R/library/spam/tests/testthat/test-subset.R
/usr/lib64/R/library/spam/tests/testthat/test-xybind.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/spam/libs/spam.so
/usr/lib64/R/library/spam/libs/spam.so.avx2
/usr/lib64/R/library/spam/libs/spam.so.avx512
