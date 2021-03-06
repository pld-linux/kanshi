Summary:	Dynamic output configuration
Name:		kanshi
Version:	1.2.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://git.sr.ht/~emersion/kanshi/archive/v%{version}.tar.gz
# Source0-md5:	f59945af185d1a7b88065d91858560e5
URL:		https://wayland.emersion.fr/kanshi/
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc >= 1.9.2
BuildRequires:	wayland-devel
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
%{_mandir}/man1/kanshi.1*
%{_mandir}/man5/kanshi.5*
