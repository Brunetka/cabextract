Summary:	A program to extract Microsoft Cabinet files
Summary(pl):	Program do rozpakowywania plik�w MS Cabinet
Name:		cabextract
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Archiving
Source0:	http://www.kyz.uklinux.net/downloads/%{name}-%{version}.tar.gz
URL:		http://www.kyz.uklinux.net/cabextract.php3
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%description -l pl
Pliki Cabinet (.CAB) s� rodzajem archiwum, kt�ry Miscrosoft u�ywa do
dystrybucji swojego oprogramowania i rzeczy typu Windows Font Pack.
cabextract mo�e takie pliki rozpakowa�.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
