#
# Conditional build:
%bcond_without	tests	# smoke tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Console colouring for Python
Summary(pl.UTF-8):	Kolory na konsoli dla Pythona
Name:		python-termstyle
Version:	0.1.11
Release:	6
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/termstyle/
Source0:	https://files.pythonhosted.org/packages/source/t/termstyle/termstyle-%{version}.tar.gz
# Source0-md5:	b6ec81a1c7ebe06f139ce3c294bd3ff8
URL:		https://pypi.org/project/termstyle/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
termstyle is a simple Python library for adding coloured output to
terminal (console) programs. The definitions come from ECMA-048, the
"Control Functions for Coded Character Sets" standard.

%description -l pl.UTF-8
termstyle to prosta biblioteka Pythona, pozwalająca dodawać kolorowe
wyjście do programów terminalowych (konsolowych). Definicje pochodzą
ze standardu ECMA-048 ("Control Functions for Coded Character Sets").

%package -n python3-termstyle
Summary:	Console colouring for Python
Summary(pl.UTF-8):	Kolory na konsoli dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-termstyle
termstyle is a simple Python library for adding coloured output to
terminal (console) programs. The definitions come from ECMA-048, the
"Control Functions for Coded Character Sets" standard.

%description -n python3-termstyle -l pl.UTF-8
termstyle to prosta biblioteka Pythona, pozwalająca dodawać kolorowe
wyjście do programów terminalowych (konsolowych). Definicje pochodzą
ze standardu ECMA-048 ("Control Functions for Coded Character Sets").

%prep
%setup -q -n termstyle-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONIOENCODING=UTF-8 \
%{__python} test2.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} test3.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/termstyle.py[co]
%{py_sitescriptdir}/termstyle-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-termstyle
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/termstyle.py
%{py3_sitescriptdir}/__pycache__/termstyle.cpython-*.py[co]
%{py3_sitescriptdir}/termstyle-%{version}-py*.egg-info
%endif
