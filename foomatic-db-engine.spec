Summary:	System for using free software printer drivers
Summary(pl.UTF-8):	System umożliwiający używanie darmowych sterowników drukarek
Name:		foomatic-db-engine
Version:	4.0.13
Release:	2
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	https://www.openprinting.org/download/foomatic/%{name}-%{version}.tar.gz
# Source0-md5:	f178947ca0437d85823a247f5725e6eb
Patch0:		%{name}-cups.patch
URL:		https://www.linuxprinting.org/foomatic.html
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libxml2-devel >= 2
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
Provides:	perl(Foomatic::GrovePath)
Suggests:	a2ps
Suggests:	foomatic-filters >= 4.0.7
Suggests:	ghostscript
Suggests:	wget
Obsoletes:	foomatic < 20020720
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
%setup -q
%patch -P0 -p1

%build
%{__aclocal} -I .
%{__autoconf}
%configure \
	A2PS=/usr/bin/a2ps \
	GS=/usr/bin/gs \
	WGET=/usr/bin/wget \
	--disable-gscheck

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
%doc ChangeLog README TODO USAGE
# XXX: dir shared with foomatic-filters
%dir %{_sysconfdir}/foomatic
%attr(755,root,root) %{_bindir}/foomatic-combo-xml
%attr(755,root,root) %{_bindir}/foomatic-compiledb
%attr(755,root,root) %{_bindir}/foomatic-configure
%attr(755,root,root) %{_bindir}/foomatic-datafile
%attr(755,root,root) %{_bindir}/foomatic-perl-data
%attr(755,root,root) %{_bindir}/foomatic-ppd-options
%attr(755,root,root) %{_bindir}/foomatic-ppd-to-xml
%attr(755,root,root) %{_bindir}/foomatic-ppdfile
%attr(755,root,root) %{_bindir}/foomatic-printjob
%attr(755,root,root) %{_bindir}/foomatic-searchprinter
%attr(755,root,root) %{_sbindir}/foomatic-addpjloptions
%attr(755,root,root) %{_sbindir}/foomatic-cleanupdrivers
%attr(755,root,root) %{_sbindir}/foomatic-extract-text
%attr(755,root,root) %{_sbindir}/foomatic-fix-xml
%attr(755,root,root) %{_sbindir}/foomatic-getpjloptions
%attr(755,root,root) %{_sbindir}/foomatic-kitload
%attr(755,root,root) %{_sbindir}/foomatic-nonumericalids
%attr(755,root,root) %{_sbindir}/foomatic-preferred-driver
%attr(755,root,root) %{_sbindir}/foomatic-printermap-to-gutenprint-xml
%attr(755,root,root) %{_sbindir}/foomatic-replaceoldprinterids
%attr(755,root,root) %{_ulibdir}/cups/driver/foomatic
%{perl_vendorlib}/Foomatic
%{_datadir}/foomatic
%{_mandir}/man1/foomatic-combo-xml.1*
%{_mandir}/man1/foomatic-compiledb.1*
%{_mandir}/man1/foomatic-configure.1*
%{_mandir}/man1/foomatic-perl-data.1*
%{_mandir}/man1/foomatic-ppd-options.1*
%{_mandir}/man1/foomatic-ppdfile.1*
%{_mandir}/man1/foomatic-printjob.1*
%{_mandir}/man8/foomatic-addpjloptions.8*
%{_mandir}/man8/foomatic-getpjloptions.8*
%{_mandir}/man8/foomatic-kitload.8*
%{_mandir}/man8/foomatic-preferred-driver.8*
