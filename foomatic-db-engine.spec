%include	/usr/lib/rpm/macros.perl
Summary:	System for using free software printer drivers
Summary(pl):	System umo¿liwiaj±cy u¿ywanie darmowych sterowników drukarek
Name:		foomatic-db-engine
Version:	2.9.0
Release:	1
License:	GPL
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
Source0:	http://www.linuxprinting.org/download/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	perl-devel
BuildRequires:	libxml2-devel
Provides:	perl(Foomatic::GrovePath)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR="$RPM_BUILD_ROOT"
cp -fr $RPM_BUILD_ROOT$RPM_BUILD_ROOT%{_libdir} $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc ChangeLog TODO README USAGE
%{_mandir}/man1/*
%{_mandir}/man8/*

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/foomatic

%attr(755,root,root) %{_bindir}/foomatic-*
%attr(755,root,root) %{_sbindir}/foomatic-*

%{perl_sitelib}/Foomatic
%{perl_sitearch}/auto/Foomatic

%{_datadir}/foomatic
