%include	/usr/lib/rpm/macros.perl

Summary:	System for using free software printer drivers
Summary(pl):	System umo¿liwiaj±cy u¿ywanie darmowych sterowników drukarek
Name:		foomatic-db-engine
Version:	3.0.1
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{version}.tar.gz
# Source0-md5:	89070d0acc245d350faeb0c49a5f3f7f
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
Foomatic to system pozwalaj±cy na u¿ywanie wolnodostêpnych
sterowników drukarek z popularnymi uniksowymi serwerami wydruków.
Obs³uguje LPD, PDQ, CUPS, VA Linux LPD, LPRng, PPR i bezpo¶rednie
drukowanie bez kolejkowania oraz dowolny wolnodostêpny sterownik,
dla którego parametry zosta³y wprowadzone do bazy danych.

%prep
%setup -q

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
