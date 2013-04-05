%define upstream_name    HTML-Form
%define upstream_version 6.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Class that represents an HTML form element
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(HTML::TokeParser)
BuildRequires:	perl(HTTP::Request)
BuildRequires:	perl(HTTP::Request::Common) >= 6.30.0
BuildRequires:	perl(LWP::MediaTypes)
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


%changelog
* Sat Mar 31 2012 Götz Waschk <waschk@mandriva.org> 6.30.0-1
+ Revision: 788475
- update build deps
- new version

* Wed Feb 22 2012 Götz Waschk <waschk@mandriva.org> 6.20.0-1
+ Revision: 779073
- update build deps
- update to new version 6.02

* Sun Feb 19 2012 Götz Waschk <waschk@mandriva.org> 6.10.0-1
+ Revision: 777364
- update to new version 6.01

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-4
+ Revision: 765302
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-3
+ Revision: 763843
- rebuilt for perl-5.14.x

* Fri Nov 11 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 6.0.0-2
+ Revision: 729995
- clean out old junk and apply some cosmetics

* Mon May 09 2011 Götz Waschk <waschk@mandriva.org> 6.0.0-1
+ Revision: 672831
- import perl-HTML-Form

