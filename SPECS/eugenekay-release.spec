Name: eugenekay-release
Version:  2.1
Release: 1%{?dist}
Summary: EugeneKay repository configuration
Group: System Environment/Base
License: WTFPL
URL: https://eugenekay.com
Source0: %{name}-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
EugeneKay's package repository configuration. Includes the EugeneKay and
SaltCloud repos.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 eugenekay.repo $RPM_BUILD_ROOT/etc/yum.repos.d/
install -m 644 saltstack.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/yum.repos.d/eugenekay.repo
/etc/yum.repos.d/saltstack.repo

%changelog
* Sun Apr 3 2016 Eugene E. Kashpureff Jr <eugene@kashpureff.org> - 2.0-1
- Add SaltStack repo

* Tue Dec 9 2014 Eugene E. Kashpureff Jr <eugene@kashpureff.org> - 1.0-1
- Initial package

