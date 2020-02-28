#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : check-manifest
Version  : 0.41
Release  : 15
URL      : https://files.pythonhosted.org/packages/d5/05/c055664f50026fcc256b554f35c07ccbd9447f4b13410a40b0440e555449/check-manifest-0.41.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/05/c055664f50026fcc256b554f35c07ccbd9447f4b13410a40b0440e555449/check-manifest-0.41.tar.gz
Summary  : Check MANIFEST.in in a Python package for completeness
Group    : Development/Tools
License  : MIT
Requires: check-manifest-bin = %{version}-%{release}
Requires: check-manifest-license = %{version}-%{release}
Requires: check-manifest-python = %{version}-%{release}
Requires: check-manifest-python3 = %{version}-%{release}
Requires: pep517
Requires: toml
BuildRequires : buildreq-distutils3
BuildRequires : pep517
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : toml
BuildRequires : tox
BuildRequires : virtualenv

%description
check-manifest
==============

|buildstatus|_ |appveyor|_ |coverage|_

Are you a Python developer?  Have you uploaded packages to the Python Package
Index?  Have you accidentally uploaded *broken* packages with some files
missing?  If so, check-manifest is for you.

Quick start
-----------

::

    $ pip install check-manifest

    $ cd ~/src/mygreatpackage
    $ check-manifest

You can ask the script to help you update your MANIFEST.in::

    $ check-manifest -u -v
    listing source files under version control: 6 files and directories
    building an sdist: check-manifest-0.7.tar.gz: 4 files and directories
    lists of files in version control and sdist do not match!
    missing from sdist:
      tests.py
      tox.ini
    suggested MANIFEST.in rules:
      include *.py
      include tox.ini
    updating MANIFEST.in

    $ cat MANIFEST.in
    include *.rst

    # added by check_manifest.py
    include *.py
    include tox.ini


Command-line reference
----------------------

::

    $ check-manifest --help
    usage: check-manifest [-h] [--version] [-v] [-c] [-u] [-p PYTHON]
                          [--ignore patterns]
                          [source_tree]

    Check a Python MANIFEST.in file for completeness

    positional arguments:
      source_tree           location for the source tree (default: .)

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      -v, --verbose         more verbose output (default: False)
      -c, --create          create a MANIFEST.in if missing (default: False)
      -u, --update          append suggestions to MANIFEST.in (implies --create)
                            (default: False)
      -p PYTHON, --python PYTHON
                            use this Python interpreter for running setup.py sdist
                            (default: /home/mg/.venv/bin/python)
      --ignore patterns     ignore files/directories matching these comma-
                            separated patterns (default: None)
      --ignore-bad-ideas patterns
                            ignore bad idea files/directories matching these
                            comma-separated patterns (default: [])


Configuration
-------------

You can configure check-manifest to ignore certain file patterns using
a ``[tool.check-manifest]`` section in your ``pyproject.toml`` file or
a ``[check-manifest]`` section in either ``setup.cfg`` or
``tox.ini``. Examples::

    # pyproject.toml
    [tool.check-manifest]
    ignore = [".travis.yml"]

    # setup.cfg or tox.ini
    [check-manifest]
    ignore =
        .travis.yml

Note that lists are newline separated in the ``setup.cfg`` and
``tox.ini`` files.

The following options are recognized:

ignore
    A list of filename patterns that will be ignored by check-manifest.
    Use this if you want to keep files in your version control system
    that shouldn't be included in your source distributions.  The
    default ignore list is ::

        PKG-INFO
        *.egg-info
        *.egg-info/*
        setup.cfg
        .hgtags
        .hgsigs
        .hgignore
        .gitignore
        .bzrignore
        .gitattributes
        .github/*
        .travis.yml
        Jenkinsfile
        *.mo

ignore-default-rules
    If set to ``true``, your ``ignore`` patterns will replace the default
    ignore list instead of adding to it.

ignore-bad-ideas
    A list of filename patterns that will be ignored by
    check-manifest's generated files check.  Use this if you want to
    keep generated files in your version control system, even though
    it is generally a bad idea.


Version control integration
---------------------------

With `pre-commit <https://pre-commit.com>`_, check-manifest can be part of your
git-workflow. Add the following to your ``.pre-commit-config.yaml``.

.. code-block:: yaml

    repos:
    -   repo: https://github.com/mgedmin/check-manifest
        rev: "0.39"
        hooks:
        -   id: check-manifest


.. |buildstatus| image:: https://api.travis-ci.org/mgedmin/check-manifest.svg?branch=master
.. _buildstatus: https://travis-ci.org/mgedmin/check-manifest

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/mgedmin/check-manifest?branch=master&svg=true
.. _appveyor: https://ci.appveyor.com/project/mgedmin/check-manifest

.. |coverage| image:: https://coveralls.io/repos/mgedmin/check-manifest/badge.svg?branch=master
.. _coverage: https://coveralls.io/r/mgedmin/check-manifest


Changelog
=========


0.41 (2020-02-25)
-----------------

- Support `PEP 517`_, i.e. packages using pyproject.toml instead of a setup.py
  (`#105 <https://github.com/mgedmin/check-manifest/issues/105>`_).

.. _PEP 517: https://www.python.org/dev/peps/pep-0517/

- Ignore subcommand stderr unless the subcommand fails.  This avoids treating
  warning messages as filenames.  (`#110
  <https://github.com/mgedmin/check-manifest/issues/110>`_.)


0.40 (2019-10-15)
-----------------

- Add Python 3.8 support.


0.39 (2019-06-06)
-----------------

- You can now use check-manifest as a `pre-commit <https://pre-commit.com>`_
  hook (`#100 <https://github.com/mgedmin/check-manifest/issues/100>`__).


0.38 (2019-04-23)
-----------------

- Add Python 3.7 support.

- Drop Python 3.4 support.

- Added GitHub templates to default ignore patterns.

- Added reading check-manifest config out of ``tox.ini`` or ``pyproject.toml``.


0.37 (2018-04-12)
-----------------

- Drop Python 3.3 support.

- Support packages using ``setuptools_scm``
  (`#68 <https://github.com/mgedmin/check-manifest/issues/68>`__).

  Note that ``setuptools_scm`` usually makes MANIFEST.in files obsolete.
  Having one is helpful only if you intend to build an sdist and then use that
  sdist to perform further builds, instead of building from a source checkout.


0.36 (2017-11-21)
-----------------

- Handle empty VCS repositories more gracefully
  (`#84 <https://github.com/mgedmin/check-manifest/issues/84>`__).


0.35 (2017-01-30)
-----------------

- Python 3.6 support.


0.34 (2016-09-14)
-----------------

- Fix WindowsError due to presence of read-only files
  (`#74 <https://github.com/mgedmin/check-manifest/issues/74>`__).


0.33 (2016-08-29)
-----------------

- Fix WindowsError due to git submodules in subdirectories
  (`#73 <https://github.com/mgedmin/check-manifest/pull/73>`__).
  Contributed by Loren Gordon.


0.32 (2016-08-16)
-----------------

* New config/command line option to ignore bad ideas (ignore-bad-ideas)
  (`issue #67 <https://github.com/mgedmin/check-manifest/issues/67>`__).
  Contributed by Brecht Machiels.

* Files named ``.hgsigs`` are ignored by default.  Contributed by Jakub Wilk.


0.31 (2016-01-28)
-----------------

- Drop Python 3.2 support.

- Ignore commented-out lines in MANIFEST.in
  (`issue #66 <https://github.com/mgedmin/check-manifest/issues/66>`__).


0.30 (2015-12-10)
-----------------

* Support git submodules
  (`issue #61 <https://github.com/mgedmin/check-manifest/issues/61>`__).

* Revert the zc.buildout support hack from 0.26 because it causes breakage
  (`issue #56 <https://github.com/mgedmin/check-manifest/issues/56>`__).

* Improve non-ASCII filename handling with Bazaar on Windows.


0.29 (2015-11-21)
-----------------

* Fix --python with just a command name, to be found in path (`issue #57
  <https://github.com/mgedmin/check-manifest/issues/57>`__).


0.28 (2015-11-11)
-----------------

* Fix detection of git repositories when .git is a file and not a directory (`#53
  <https://github.com/mgedmin/check-manifest/pull/53>`__).  One situation
  where this occurs is when the project is checked out as a git submodule.

* Apply ignore patterns in subdirectories too (`#54
  <https://github.com/mgedmin/check-manifest/issues/54>`__).


0.27 (2015-11-02)
-----------------

* Fix utter breakage on Windows, introduced in 0.26 (`issue #52
  <https://github.com/mgedmin/check-manifest/issues/52>`__).
  (The bug -- clearing the environment unnecessarily -- could probably
  also cause locale-related problems on other OSes.)


0.26 (2015-10-30)
-----------------

* Do not complain about missing ``.gitattributes`` file (`PR #50
  <https://github.com/mgedmin/check-manifest/pull/50>`__).

* Normalize unicode representation and case of filenames. (`issue #47
  <https://github.com/mgedmin/check-manifest/issues/47>`__).

* Support installation via zc.buildout better (`issue #35
  <https://github.com/mgedmin/check-manifest/issues/35>`__).

* Drop Python 2.6 support because one of our test dependencies (mock) dropped
  it.  This also means we no longer use environment markers.


0.25 (2015-05-27)
-----------------

* Stop dynamic computation of install_requires in setup.py: this doesn't work
  well in the presence of the pip 7 wheel cache.  Use PEP-426 environment
  markers instead (this means we now require setuptools >= 0.7, and pip >= 6.0,
  and wheel >= 0.24).


0.24 (2015-03-26)
-----------------

* Make sure ``setup.py`` not being added to the VCS doesn't cause
  hard-to-understand errors (`issue #46
  <https://github.com/mgedmin/check-manifest/issues/46>`__).


0.23 (2015-02-12)
-----------------

* More reliable svn status parsing; now handles svn externals (`issue #45
  <https://github.com/mgedmin/check-manifest/issues/45>`__).

* The test suite now skips tests for version control systems that aren't
  installed (`issue #42
  <https://github.com/mgedmin/check-manifest/issues/42>`__).


0.22 (2014-12-23)
-----------------

* More terse output by default; use the new ``-v`` (``--verbose``) flag
  to see all the details.

* Warn the user if MANIFEST.in is missing  (`issue #31
  <https://github.com/mgedmin/check-manifest/issues/31>`__).

* Fix IOError when files listed under version control are missing (`issue #32
  <https://github.com/mgedmin/check-manifest/issues/32>`__).

* Improved wording of the match/do not match messages (`issue #34
  <https://github.com/mgedmin/check-manifest/issues/34>`__).

* Handle a relative --python path (`issue #36
  <https://github.com/mgedmin/check-manifest/issues/36>`__).

* Warn about leading and trailing slashes in MANIFEST.in (`issue #37
  <https://github.com/mgedmin/check-manifest/issues/37>`__).

* Ignore .travis.yml by default (`issue #39
  <https://github.com/mgedmin/check-manifest/issues/39>`__).

* Suggest a rule for Makefile found deeper in the source tree.


0.21 (2014-06-13)
-----------------

* Don't drop setup.cfg when copying version-controlled files into a clean
  temporary directory (`issue #29
  <https://github.com/mgedmin/check-manifest/issues/29>`__).


0.20 (2014-05-14)
-----------------

* Restore warning about files included in the sdist but not added to the
  version control system (`issue #27
  <https://github.com/mgedmin/check-manifest/issues/27>`__).

* Fix ``check-manifest relative/pathname`` (`issue #28
  <https://github.com/mgedmin/check-manifest/issues/28>`__).


0.19 (2014-02-09)
-----------------

* More correct MANIFEST.in parsing for exclusion rules.
* Some effort was expended towards Windows compatibility.
* Handles non-ASCII filenames, as long as they're valid in your locale
  (`issue #23 <https://github.com/mgedmin/check-manifest/issues/23>`__,
  `#25 <https://github.com/mgedmin/check-manifest/issues/23>`__).


0.18 (2014-01-30)
-----------------

* Friendlier error message when an external command cannot be found
  (`issue #21 <https://github.com/mgedmin/check-manifest/issues/21>`__).
* Add suggestion pattern for `.coveragerc`.
* Python 2.6 support
  (`issue #22 <https://github.com/mgedmin/check-manifest/issues/22>`__).


0.17 (2013-10-10)
-----------------

* Read the existing MANIFEST.in file for files to ignore
  (`issue #19 <https://github.com/mgedmin/check-manifest/issues/19>`__).


0.16 (2013-10-01)
-----------------

* Fix Subversion status parsing in the presence of svn usernames longer than 12
  characters (`issue #18 <https://github.com/mgedmin/check-manifest/issues/18>`__).


0.15 (2013-09-20)
-----------------

* Normalize the paths of all files, avoiding some duplicate misses of
  directories.  (`issue #16 <https://github.com/mgedmin/check-manifest/issues/16>`__).
  [maurits]


0.14 (2013-08-28)
-----------------

* Supports packages that do not live in the root of a version control
  repository (`issue #15 <https://github.com/mgedmin/check-manifest/issues/15>`__).

* More reliable svn support: detect files that have been added but not
  committed (or committed but not updated).

* Licence changed from GPL (v2 or later) to MIT
  (`issue #12 <https://github.com/mgedmin/check-manifest/issues/12>`__).


0.13 (2013-07-31)
-----------------

* New command line option: --ignore
  (`issue #11 <https://github.com/mgedmin/check-manifest/issues/11>`__).
  Contributed by Steven Myint.

* New command line option: -p, --python.  Defaults to the Python you used to
  run check-manifest.  Fixes issues with packages that require Python 3 to run
  setup.py (`issue #13 <https://github.com/mgedmin/check-manifest/issues/13>`__).


0.12 (2013-05-15)
-----------------

* Add suggestion pattern for `Makefile`.

* More generic suggestion patterns, should cover almost anything.

* zest.releaser_ integration: skip check-release for non-Python packages
  (`issue #9 <https://github.com/mgedmin/check-manifest/issues/9>`__).


0.11 (2013-03-20)
-----------------

* Make sure ``MANIFEST.in`` is not ignored even if it hasn't been added to the
  VCS yet (`issue #7 <https://github.com/mgedmin/check-manifest/issues/7>`__).


0.10 (2013-03-17)
-----------------

* ``check-manifest --version`` now prints the version number.

* Don't apologize for not adding rules for directories (especially after adding
  rules that include files inside that directory).

* Python 3 support contributed by Steven Myint.

* Default ignore patterns can be configured in ``setup.cfg``
  (`issue #3 <https://github.com/mgedmin/check-manifest/issues/3>`_).


0.9 (2013-03-06)
----------------

* Add suggestion pattern for `.travis.yml`.

* When check-manifest -u (or -c) doesn't know how to write a rule matching a
  particular file, it now apologizes explicitly.

* Copy the source tree to a temporary directory before running python setup.py
  sdist to avoid side effects from setuptools plugins or stale
  \*.egg-info/SOURCES.txt files
  (`issue #1 <https://github.com/mgedmin/check-manifest/issues/1>`_).

* Warn if `*.egg-info` or `*.mo` is actually checked into the VCS.

* Don't complain if `*.mo` files are present in the sdist but not in the VCS
  (`issue #2 <https://github.com/mgedmin/check-manifest/issues/2>`_).


0.8 (2013-03-06)
----------------

* Entry point for zest.releaser_.  If you install both zest.releaser and
  check-manifest, you will be asked if you want to check your manifest during
  ``fullrelease``.

.. _zest.releaser: https://pypi.python.org/pypi/zest.releaser


0.7 (2013-03-05)
----------------

* First release available from the Python Package Index.

* Moved from https://gist.github.com/4277075
  to https://github.com/mgedmin/check-manifest

* Added README.rst, CHANGES.rst, setup.py, tox.ini (but no real tests yet),
  MANIFEST.in, and a Makefile.

* Fixed a bug in error reporting (when setup.py failed, the user would get
  `TypeError: descriptor '__init__' requires an 'exceptions.Exception' object
  but received a 'str'`).

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
Provides: pypi(check-manifest)

%description python3
python3 components for the check-manifest package.


%prep
%setup -q -n check-manifest-0.41
cd %{_builddir}/check-manifest-0.41

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582906937
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/check-manifest
cp %{_builddir}/check-manifest-0.41/LICENSE.rst %{buildroot}/usr/share/package-licenses/check-manifest/b82514746d0268c7a2fca13e10d9d6daafa544c9
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
