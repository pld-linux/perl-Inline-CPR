%include	/usr/lib/rpm/macros.perl
%define	pdir	Inline
%define	pname	CPR
Summary:	Inline::CPR - C Perl Run
Summary(pl):	Inline::CPR - Uruchamianie perla z C
Name:		perl-Inline-CPR
Version:	0.12
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Inline >= 0.41
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::CPR - C Perl Run. Embed Perl in C, ala Inline.

%description -l pl
Inline::CPR - uruchamianie Perla z C. Pozwala na wbudowywanie
kodu Perla w C.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Inline/CPR.pm
%{_mandir}/man3/*
