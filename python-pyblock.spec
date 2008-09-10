%define realname pyblock
Summary:	Python modules for dealing with block devices
Summary(pl.UTF-8):	Moduły Pythona do obsługi urządzeń blokowych
Name:		python-%{realname}
Version:	0.30
Release:	1
License:	GPL
Group:		Libraries/Python
# https://fedorahosted.org/releases/p/y/pyblock/ (not yet)
Source0:	%{realname}-%{version}.tar.bz2
# Source0-md5:	a245a890688e149341de28d151d09acc
Patch0:		%{name}-ULLLLLL.patch
Patch1:		%{name}-optflags.patch
Patch2:		%{name}-fix.patch
BuildRequires:	device-mapper-devel >= 1.02.05-0.3
BuildRequires:	dmraid-devel >= 1.0.0-0.rc10.1.6
BuildRequires:	libselinux-devel
BuildRequires:	python-devel
Requires:	device-mapper >= 1.02.02
ExcludeArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
The pyblock contains Python modules for dealing with block devices.

%description -l pl.UTF-8
Pakiet pyblock zawiera moduły Pythona do obsługi urządzeń blokowych.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SITELIB=%{py_sitedir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/block
%attr(755,root,root) %{py_sitedir}/block/dmmodule.so
%attr(755,root,root) %{py_sitedir}/block/dmraidmodule.so
%{py_sitedir}/block/*.py[co]
