Summary:	GTK passwords manager for system and network administrators
Name:		gtkpasman
Version:	0.12.1
Release:	2
License:	GPLv2+
Group:		File tools
Url:		http://gtkpasman.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/gtkpasman/%{name}-sources/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
Requires:	gnupg

%description
It is a graphical interface to manage the usage of passwords related to servers
or services, grouped by customers (plateforms, etc.) The purpose is to provide
system and network administrators a convenient tool to manage a passwords
knowledge base related to customers, servers, services...

It can help to retrieve passwords, or even connect to servers (ssh, telnet,
FTP...). Passwords will be kept in a gnupg crypted file. The structure of the
file is predefined, but very easy to edit and maintain. The gtk application
can switch between a discreet applet and a full list of containers.

%files -f %{name}.lang
%doc README NEWS AUTHORS
%{_bindir}/gtkpasman
%{_datadir}/applications/gtkpasman.desktop
%{_datadir}/glib-2.0/schemas/gtkpasman.gschema.xml

#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}
