%include	/usr/lib/rpm/macros.perl

%define		_rc	rc1

Summary:	System for using free software printer drivers
Summary(pl):	System umożliwiający używanie darmowych sterowników drukarek
Name:		foomatic-db-engine
Version:	3.0.1
Release:	0.%{_rc}.1
License:	GPL
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	8c117150f00f75cde9096dbe0cc1a30d
Patch0:		%{name}-perl-doubledestdir.patch
Patch1:		%{name}-symlinks.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	foomatic-filters >= 3.0.1
BuildRequires:	libxml2-devel
BuildRequires:	perl-devel
Provides:	perl(Foomatic::GrovePath)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	foomatic

%description
Foomatic is a system for using free software printer drivers with
common spoolers on Unix. It supports LPD, PDQ, CUPS, the VA Linux
LPD, LPRng, PPR, and direct spooler-less printing and any free
software driver for which execution data has been entered in the
database.

%description -l pl
Foomatic to system pozwalający na używanie wolnodostępnych
sterowników drukarek z popularnymi uniksowymi serwerami wydruków.
Obsługuje LPD, PDQ, CUPS, VA Linux LPD, LPRng, PPR i bezpośrednie
drukowanie bez kolejkowania oraz dowolny wolnodostępny sterownik,
dla którego parametry zostały wprowadzone do bazy danych.

%prep
%setup -q -n %{name}-%{version}%{_rc}
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make} \
	PERL_INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT

chmod +x mkinstalldirs

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install -d $RPM_BUILD_ROOT%{_datadir}/foomatic/db/source/{driver,opt,printer}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO README USAGE
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/foomatic
%attr(755,root,root) %{_bindir}/foomatic-*
%attr(755,root,root) %{_sbindir}/foomatic-*
%{perl_vendorlib}/Foomatic
%{_datadir}/foomatic
%{_mandir}/man1/*
%{_mandir}/man8/*
