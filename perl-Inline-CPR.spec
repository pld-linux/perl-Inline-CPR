#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# "make test" attemts to install files
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Inline
%define		pname	CPR
Summary:	Inline::CPR - C Perl Run
Summary(pl):	Inline::CPR - uruchamianie perla z C
Name:		perl-Inline-CPR
Version:	0.12
Release:	5
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pname}-%{version}.tar.gz
# Source0-md5:	7f2694934f58de24ece46864c641f176
Patch0:		%{name}-gcc3.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Inline >= 0.41
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inline::CPR - C Perl Run. Embed Perl in C, ala Inline.

%description -l pl
Inline::CPR - uruchamianie Perla z C. Pozwala na wbudowywanie
kodu Perla w C.

%prep
%setup -q -n %{pdir}-%{pname}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
%{perl_vendorlib}/Inline/CPR.pm
%{_mandir}/man3/*
