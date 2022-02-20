Name:           nwg-launchers
Version:        0.6.3
Release:        1
Summary:        GTK launchers and menu for sway and i3
License:        GPL-3.0
Group:          System/X11/Utilities/NWG
URL:            https://github.com/nwg-piotr/nwg-launchers
Source:         https://github.com/nwg-piotr/nwg-launchers/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(nlohmann_json)

%description
GTK-based launchers: application grid, button bar, dmenu for sway and other window managers.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/nwgbar
%{_bindir}/nwgdmenu
%{_bindir}/nwggrid
%{_bindir}/nwggrid-server
%dir %{_datadir}/nwg-launchers
%{_datadir}/nwg-launchers/nwgbar
%{_datadir}/nwg-launchers/nwgdmenu
%{_datadir}/nwg-launchers/nwggrid
%{_datadir}/nwg-launchers/icon-missing.png
%{_datadir}/nwg-launchers/icon-missing.svg
