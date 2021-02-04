#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbclient
Version  : 0.5.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/21/bf/8bc77713fe0e5c9255233f112cd5819d692a4eded7922e40d82970ce5616/nbclient-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/21/bf/8bc77713fe0e5c9255233f112cd5819d692a4eded7922e40d82970ce5616/nbclient-0.5.1.tar.gz
Summary  : A client library for executing notebooks. Formerly nbconvert's ExecutePreprocessor.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: nbclient-license = %{version}-%{release}
Requires: nbclient-python = %{version}-%{release}
Requires: nbclient-python3 = %{version}-%{release}
Requires: jupyter_client
Requires: nbformat
Requires: traitlets
BuildRequires : buildreq-distutils3
BuildRequires : nbformat
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : traitlets
BuildRequires : virtualenv

%description
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jupyter/nbclient/master?filepath=binder%2Frun_nbclient.ipynb)
[![Travis Build Status](https://travis-ci.org/jupyter/nbclient.svg?branch=master)](https://travis-ci.org/jupyter/nbclient)
[![Build Status](https://github.com/jupyter/nbclient/workflows/CI/badge.svg)](https://github.com/jupyter/nbclient/actions)
[![Documentation Status](https://readthedocs.org/projects/nbclient/badge/?version=latest)](https://nbclient.readthedocs.io/en/latest/?badge=latest)
[![image](https://codecov.io/github/jupyter/nbclient/coverage.svg?branch=master)](https://codecov.io/github/jupyter/nbclient?branch=master)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package license
Summary: license components for the nbclient package.
Group: Default

%description license
license components for the nbclient package.


%package python
Summary: python components for the nbclient package.
Group: Default
Requires: nbclient-python3 = %{version}-%{release}

%description python
python components for the nbclient package.


%package python3
Summary: python3 components for the nbclient package.
Group: Default
Requires: python3-core
Provides: pypi(nbclient)
Requires: pypi(async_generator)
Requires: pypi(jupyter_client)
Requires: pypi(nbformat)
Requires: pypi(nest_asyncio)
Requires: pypi(traitlets)

%description python3
python3 components for the nbclient package.


%prep
%setup -q -n nbclient-0.5.1
cd %{_builddir}/nbclient-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612454478
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nbclient
cp %{_builddir}/nbclient-0.5.1/LICENSE %{buildroot}/usr/share/package-licenses/nbclient/8a1fbf91e5334237f0176576f8ad1a679b8135a8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbclient/8a1fbf91e5334237f0176576f8ad1a679b8135a8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*