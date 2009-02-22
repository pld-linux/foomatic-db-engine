%include	/usr/lib/rpm/macros.perl
%define		snap	20080317
Summary:	System for using free software printer drivers
Summary(pl.UTF-8):	System umożliwiający używanie darmowych sterowników drukarek
Name:		foomatic-db-engine
Version:	3.0.%{snap}
Release:	4
License:	GPL
Group:		Applications/System
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-3.0-%{snap}.tar.gz
# Source0-md5:	d6ac64aeaa1f6ecdf386df6b6ad380a7
Patch0:		%{name}-destdir.patch
Patch1:		%{name}-cups.patch
URL:		http://www.linuxprinting.org/foomatic.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	foomatic-filters >= 3.0.20080317
BuildRequires:	libxml2-devel
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
Provides:	perl(Foomatic::GrovePath)
Obsoletes:	foomatic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_ulibdir	%{_prefix}/lib

%description
Foomatic is a system for using free software printer drivers with
common spoolers on Unix. It supports LPD, PDQ, CUPS, the VA Linux LPD,
LPRng, PPR, and direct spooler-less printing and any free software
driver for which execution data has been entered in the database.

%description -l pl.UTF-8
Foomatic to system pozwalający na używanie wolnodostępnych sterowników
drukarek z popularnymi uniksowymi serwerami wydruków. Obsługuje LPD,
PDQ, CUPS, VA Linux LPD, LPRng, PPR i bezpośrednie drukowanie bez
kolejkowania oraz dowolny wolnodostępny sterownik, dla którego
parametry zostały wprowadzone do bazy danych.

%prep
%setup -q -n %{name}-3.0-%{snap}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I .
%{__autoconf}
%configure
%{__make} \
	PERL_INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT

chmod +x mkinstalldirs

%{__sed} -i 's,PREFIX =.*,PREFIX = %{_prefix},g' lib/Makefile
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/{driver,opt,printer}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/foomatic
%attr(755,root,root) %{_bindir}/foomatic-*
%attr(755,root,root) %{_sbindir}/foomatic-*
%attr(755,root,root) %{_ulibdir}/cups/driver/foomatic
%{perl_vendorlib}/Foomatic
%{_datadir}/foomatic
%{_mandir}/man1/*
%{_mandir}/man8/*
