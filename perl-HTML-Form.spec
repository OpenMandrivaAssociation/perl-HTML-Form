%define upstream_name    HTML-Form
%define upstream_version 6.00

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Class that represents an HTML form element
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Encode)
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
Objects of the 'HTML::Form' class represents a single HTML '<form> ...
</form>' instance. A form consists of a sequence of inputs that usually
have names, and which can take on various values. The state of a form can
be tweaked and it can then be asked to provide 'HTTP::Request' objects that
can be passed to the request() method of 'LWP::UserAgent'.

The following methods are available:

* @forms = HTML::Form->parse( $html_document, $base_uri )

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*