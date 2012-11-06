Summary:	Graphical scanning frontend
Name:		xsane
Version:	0.998
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.xsane.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	936f1cc76b37caa8f285e1e15ac7e0aa
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-xdg-open.patch
Patch2:		%{name}-libpng.patch
Patch3:		%{name}-Makefile.patch
URL:		http://www.xsane.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gimp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	sane-backends-devel
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gimpplugindir	%(gimptool --gimpplugindir)/plug-ins

%description
XSane is a graphical scanning frontend.

%package -n gimp-plugin-xsane
Summary:	XSane plugin for GIMP
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gimp

%description -n gimp-plugin-xsane
XSane plugin for GIMP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/{sr,sr@Latn}.po
mv -f po/{zh,zh_TW}.po

%{__perl} -pi -e 's/ sr / sr\@Latn /;s/ zh/ zh_TW/' configure.in

%build
#%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{gimpplugindir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf %{_bindir}/xsane $RPM_BUILD_ROOT%{gimpplugindir}/xsane

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc xsane.{ACCELKEYS,AUTHOR,BUGS,CHANGES,LOGO,NEWS,PROBLEMS,TODO,BEGINNERS-INFO,ONLINEHELP}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/xsane
%{_mandir}/man1/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png

%files -n gimp-plugin-xsane
%defattr(644,root,root,755)
%attr(755,root,root) %{gimpplugindir}/*

