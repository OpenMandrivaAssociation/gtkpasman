%define name	gtkpasman
%define version 0.10
%define release %mkrel 3

Name:		%{name} 
Summary:	GTK passwords manager for system and network administrators   
Version:	%{version} 
Release:	%{release} 
Source0:	http://downloads.sourceforge.net/project/gtkpasman/%{name}-sources/%{version}/%{name}-%{version}.tar.gz
URL:		http://gtkpasman.sourceforge.net/
# Patch correct an error in sample file who crash the application when you try to read it
# upstream have been notified of the problem 
Patch0:		gtkpasman-fix_default_store.patch

Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:	GPLv2+ 
Requires:	gnupg
BuildRequires:	gtk+2-devel


%description
It is a graphical interface to manage the usage of passwords related to servers
or services, grouped by customers (plateforms, etc.) The purpose is to provide
system and network administrators a convenient tool to manage a passwords
knowledge base related to customers, servers, services...

It can help to retrieve passwords, or even connect to servers (ssh, telnet, 
FTP...). Passwords will be kept in a gnupg crypted file. The structure of the 
file is predefined, but very easy to edit and maintain. The gtk application 
can switch between a discreet applet and a full list of containers. 

%prep 
%setup -q -a 0 
%patch0 -p0
%build 
./autogen.sh 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root) 
%doc README NEWS AUTHORS 
%{_bindir}/gtkpasman
