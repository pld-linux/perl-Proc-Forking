#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Proc
%define	pnam	Forking
Summary:	Proc::Forking - fork and deamonize
#Summary(pl):	-
Name:		perl-%{pdir}-%{pnam}
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fc57356465c3eed871d9fb1c55f8cf5a
URL:		http://search.cpan.org/dist/Proc-Forking/
BuildRequires:	perl-Sys-Load
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Proc::Forking.pm module provides a set of tool to fork and
daemonize. The module fork a function code.

#%description -l pl

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Proc/Forking.pm
%{_mandir}/man3/*
