%define realname pyblock
Summary:	Python modules for dealing with block devices
Name:		python-%{realname}
Version:	0.15
Release:	1
Source0:	%{realname}-%{version}.tar.bz2
# Source0-md5:	a201b09eb86a748b0d41bd5671e7ae8f
Patch0:		python-pyblock-ULLLLLL.patch
License:	GPL
Group:		Libraries
BuildRequires:	device-mapper >= 1.02.05-0.3
BuildRequires:	dmraid-static
BuildRequires:	gettext
BuildRequires:	libselinux-devel
BuildRequires:	libsepol-devel
BuildRequires:	python-devel
Requires:	device-mapper >= 1.02.02
Requires:	libselinux
ExcludeArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The pyblock contains Python modules for dealing with block devices.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	SITELIB=%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/block
%{py_sitescriptdir}/block/*
