Summary:	hpiview - GTK+ Front end client for OpenHPI (HPI)
Summary(pl.UTF-8):   hpiview - interfejs kliencki GTK+ dla OpenHPI
Name:		hpiview
Version:	2.0
Release:	1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/openhpi/%{name}-%{version}.tar.gz
# Source0-md5:	32c06f96e4f22d22754de7c2f912f76a
URL:		http://openhpi.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	openhpi-devel >= 2.0.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a GTK+ based GUI developed as part of OpenHPI.

%description -l pl.UTF-8
Ten pakiet zawiera graficzny interfejs GTK+ tworzony jako część
OpenHPI.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/hpiview
%{_datadir}/hpiview
