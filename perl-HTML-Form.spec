%define modname	HTML-Form
%define modver	6.03

Summary:	Class that represents an HTML form element
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Request::Common) >= 6.30.0
BuildRequires:	perl(LWP::MediaTypes)
BuildRequires:	perl(URI)

%description
Objects of the 'HTML::Form' class represents a single HTML '<form> ...
</form>' instance. A form consists of a sequence of inputs that usually
have names, and which can take on various values. The state of a form can
be tweaked and it can then be asked to provide 'HTTP::Request' objects that
can be passed to the request() method of 'LWP::UserAgent'.

The following methods are available:

* @forms = HTML::Form->parse( $html_document, $base_uri )

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{perl_vendorlib}/*
%{_mandir}/man3/*

