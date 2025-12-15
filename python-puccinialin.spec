Name:           python-puccinialin
Version:        0.1.8
Release:        1
Summary:        Development/Python
License:        Apache-2.0 OR MIT
URL:            https://github.com/konstin/puccinialin
Source0:        https://files.pythonhosted.org/packages/source/p/puccinialin/puccinialin-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
# If we let the dependency generator do its job, we get a hard dependency
# on httpx -- resulting in a circular dependency loop while bootstrapping
# (httpx needs anyio, which needs cryptography, which needs maturin, which
# needs puccinialin).
# Since puccinialin basics work without httpx (it works as long as no http
# downloads are triggered -- sufficient to bootstrap maturin), let's
# downgrade that dependency to a soft dependency.
%define __requires_exclude .*httpx.*
Recommends:	python%{pyver}dist(httpx)

%description
Install rust into a cache dir for rust-based builds 

%files
%{_bindir}/puccinialize
%{python_sitelib}/puccinialin-%{version}.dist-info
%{python_sitelib}/puccinialin
