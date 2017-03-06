%define	dmrver	1.0.0-0.rc15
%define	dmver	1.02.54-3
%define	module	pyblock
Summary:	Python modules for dealing with block devices
Summary(pl.UTF-8):	Moduły Pythona do obsługi urządzeń blokowych
Name:		python-%{module}
Version:	0.53
Release:	5
License:	GPL v2 or GPL v3
Group:		Libraries/Python
Source0:	https://fedorahosted.org/releases/p/y/pyblock/pyblock-%{version}.tar.bz2
# Source0-md5:	f6d33a8362dee358517d0a9e2ebdd044
Patch0:		build.patch
URL:		http://fedoraproject.org/wiki/Anaconda
BuildRequires:	device-mapper-devel >= %{dmver}
BuildRequires:	dmraid-devel >= %{dmrver}
BuildRequires:	gettext
BuildRequires:	libselinux-devel
BuildRequires:	libsepol-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	device-mapper >= %{dmver}
Requires:	dmraid >= %{dmrver}
Requires:	python-parted
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fno-strict-aliasing

%description
The pyblock contains Python modules for dealing with block devices.

%description -l pl.UTF-8
Pakiet pyblock zawiera moduły Pythona do obsługi urządzeń blokowych.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__make} -j1 \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SITELIB=%{py_sitedir}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{module}-%{version}

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
