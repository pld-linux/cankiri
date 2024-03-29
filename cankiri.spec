Summary:	A single file screen recorder for Linux
Summary(pl.UTF-8):	Jednoplikowa nagrywarka ekranu dla Linuksa
Name:		cankiri
Version:	0.2
Release:	3
License:	GPL v2
Group:		Applications
Source0:	http://www.tortall.net/~mu/releases/%{name}-%{version}.tar.gz
# Source0-md5:	fcdc903284cfad5c115cb3164b67cd8a
URL:		http://www.tortall.net/mu/wiki/Cankiri
%pyrequires_eq	python-libs
BuildRequires:	rpm-pythonprov
Requires:	gstreamer-theora
Requires:	gstreamer-ximagesrc
Requires:	python-gnome-extras-egg
Requires:	python-gstreamer >= 0.10
Requires:	python-pygtk-gtk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cankiri is a single file screen recorder for Linux and other systems
that run GStreamer 0.10 and PyGTK 2.8.

%description -l pl.UTF-8
Cankiri to składająca się z jednego pliku nagrywarka ekranu dla
Linuksa i innych systemów, na których działa GStreamer 0.10 i PyGTK
2.8.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p cankiri.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/%{name}
