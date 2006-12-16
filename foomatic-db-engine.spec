%include	/usr/lib/rpm/macros.perl
Summary:	System for using free software printer drivers
Summary(pl):	System umo¿liwiaj±cy u¿ywanie darmowych sterowników drukarek
Name:		foomatic-db-engine
Version:	3.0.2
Release:	3
License:	GPL
Group:		Applications/System
URL:		http://www.linuxprinting.org/foomatic.html
Source0:	http://www.linuxprinting.org/download/foomatic/%{name}-%{version}.tar.gz
# Source0-md5:	3061b8d3f7870467e6fbeae8d4399211
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	foomatic-filters >= 3.0.2
BuildRequires:	libxml2-devel
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
Provides:	perl(Foomatic::GrovePath)
Obsoletes:	foomatic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foomatic is a system for using free software printer drivers with
common spoolers on Unix. It supports LPD, PDQ, CUPS, the VA Linux LPD,
LPRng, PPR, and direct spooler-less printing and any free software
driver for which execution data has been entered in the database.

%description -l pl
Foomatic to system pozwalaj±cy na u¿ywanie wolnodostêpnych sterowników
drukarek z popularnymi uniksowymi serwerami wydruków. Obs³uguje LPD,
PDQ, CUPS, VA Linux LPD, LPRng, PPR i bezpo¶rednie drukowanie bez
kolejkowania oraz dowolny wolnodostêpny sterownik, dla którego
parametry zosta³y wprowadzone do bazy danych.

%prep
%setup -q

%build
%{__aclocal} -I .
%{__autoconf}
%configure
%{__make} \
	PERLPREFIX=/usr \
	PERL_INSTALLDIRS=vendor

%install
rm -rf $RPM_BUILD_ROOT

chmod +x mkinstalldirs

%{__make} install \
	PERLPREFIX=/usr \
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
%{perl_vendorlib}/Foomatic
%{_datadir}/foomatic
%{_mandir}/man1/*
%{_mandir}/man8/*
