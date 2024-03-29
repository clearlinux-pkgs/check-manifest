#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : check-manifest
Version  : 0.47
Release  : 31
URL      : https://files.pythonhosted.org/packages/06/bf/19135a8e930f6d7fd3049a34ae5316c7870b0badd14f07dd53ba58c2bf93/check-manifest-0.47.tar.gz
Source0  : https://files.pythonhosted.org/packages/06/bf/19135a8e930f6d7fd3049a34ae5316c7870b0badd14f07dd53ba58c2bf93/check-manifest-0.47.tar.gz
Summary  : Check MANIFEST.in in a Python source package for completeness
Group    : Development/Tools
License  : MIT
Requires: check-manifest-bin = %{version}-%{release}
Requires: check-manifest-license = %{version}-%{release}
Requires: check-manifest-python = %{version}-%{release}
Requires: check-manifest-python3 = %{version}-%{release}
Requires: build
Requires: setuptools
Requires: toml
BuildRequires : build
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : toml
BuildRequires : tox
BuildRequires : virtualenv

%description
==============
        
        |buildstatus|_ |appveyor|_ |coverage|_
        
        Are you a Python developer?  Have you uploaded packages to the Python Package
        Index?  Have you accidentally uploaded *broken* packages with some files
        missing?  If so, check-manifest is for you.
        
        Quick start
        -----------

%package bin
Summary: bin components for the check-manifest package.
Group: Binaries
Requires: check-manifest-license = %{version}-%{release}

%description bin
bin components for the check-manifest package.


%package license
Summary: license components for the check-manifest package.
Group: Default

%description license
license components for the check-manifest package.


%package python
Summary: python components for the check-manifest package.
Group: Default
Requires: check-manifest-python3 = %{version}-%{release}

%description python
python components for the check-manifest package.


%package python3
Summary: python3 components for the check-manifest package.
Group: Default
Requires: python3-core
Provides: pypi(check_manifest)
Requires: pypi(build)
Requires: pypi(setuptools)
Requires: pypi(toml)

%description python3
python3 components for the check-manifest package.


%prep
%setup -q -n check-manifest-0.47
cd %{_builddir}/check-manifest-0.47

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635710713
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/check-manifest
cp %{_builddir}/check-manifest-0.47/LICENSE.rst %{buildroot}/usr/share/package-licenses/check-manifest/b82514746d0268c7a2fca13e10d9d6daafa544c9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/check-manifest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/check-manifest/b82514746d0268c7a2fca13e10d9d6daafa544c9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
