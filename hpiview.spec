Summary:	hpiview - GTK+ Front end client for OpenHPI (HPI)
Summary(pl):	hpiview - interfejs kliencki GTK+ dla OpenHPI
Name:		hpiview
Version:	0.6
Release:	1
License:	BSD
Group:		Applications
Source0:	http://dl.sourceforge.net/openhpi/%{name}-%{version}.tar.gz
# Source0-md5:	1a9504c1db015833e87dc99e77567fde
# from CVS - missing in tarball
Source1:	%{name}-voh_types.h
URL:		http://openhpi.sourceforge.net/
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	openhpi-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a GTK+ based GUI developed as part of OpenHPI.

%description -l pl
Ten pakiet zawiera graficzny interfejs GTK+ tworzony jako czê¶æ
OpenHPI.

%prep
%setup -q
cp %{SOURCE1} hpiview/voh_types.h

%build
CPPFLAGS="-I/usr/include/openhpi"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/hpiview
%{_datadir}/hpiview

%clean
rm -rf $RPM_BUILD_ROOT
