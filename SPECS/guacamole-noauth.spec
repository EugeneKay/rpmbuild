Name: guacamole-noauth
Version:  0.8.0
Release: 1%{?dist}
Summary: EugeneKay repository configuration
Group: System Environment/Base
License: MIT
URL: https://eugenekay.com
Source0: %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Guacamole noauth plugin

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/guacamole/extensions/
install -m 644 guacamole-noauth.jar $RPM_BUILD_ROOT/etc/guacamole/extensions/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/guacamole/extensions/guacamole-noauth.jar

%changelog
* Sat Mar 12 2016 Eugene E. Kashpureff Jr <eugene@kashpureff.org> - 1.0-1
- Initial package
