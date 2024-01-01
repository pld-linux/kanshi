Summary:	Dynamic output configuration
Name:		kanshi
Version:	1.5.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://git.sr.ht/~emersion/kanshi/archive/v%{version}.tar.gz
# Source0-md5:	7252cec39bb008bedb9bf456a9108147
URL:		https://wayland.emersion.fr/kanshi/
BuildRequires:	gcc >= 6:4.6
BuildRequires:	libvarlink-devel
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc >= 1.9.2
BuildRequires:	wayland-devel >= 1.14.91
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kanshi allows you to define output profiles that are automatically
enabled and disabled on hotplug.

%prep
%setup -q -n %{name}-v%{version}

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kanshi
%attr(755,root,root) %{_bindir}/kanshictl
%{_mandir}/man1/kanshi.1*
%{_mandir}/man1/kanshictl.1*
%{_mandir}/man5/kanshi.5*
