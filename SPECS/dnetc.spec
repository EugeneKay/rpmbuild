Name: dnetc
Version: 2.9112.521
Release: 1%{?dist}
Summary: distributed.net project client
BuildArch: x86_64
License: Distributed.net License
URL: http://distributed.net
Source0: %{name}-%{version}.tar.gz
BuildRequires: systemd
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel


%description

distributed.net project client

%pre
/usr/bin/getent passwd dnetc >/dev/null || /usr/sbin/useradd -r -d /var/lib/dnetc -s /sbin/nologin dnetc

%install
tar xzf %{SOURCE0}
cd %{name}-%{version}
mkdir -p  %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sharedstatedir}
install -m 0755 dnetc %{buildroot}%{_bindir}/dnetc
install -m 0755 dnetc.service %{buildroot}%{_unitdir}/dnetc.service
install -m 0644 dnetc.ini %{buildroot}%{_sysconfdir}/dnetc.ini
install -m 0755 dnetc.1 %{buildroot}%{_mandir}/man1/dnetc.1.gz
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/dnetc.log
mkdir -p %{buildroot}%{_sharedstatedir}/dnetc

%post
systemctl daemon-reload

%preun
systemctl stop dnetc

%postun
if [ "$1" == "0" ]
then
	/usr/sbin/userdel dnetc
	rm %{_sharedstatedir}/dnetc -rf
	systemctl daemon-reload
fi

%files
%defattr(444, root, root, 555)
%attr(0755, root, root) %{_bindir}/dnetc
%{_unitdir}/dnetc.service
%config(noreplace) %{_sysconfdir}/dnetc.ini
%{_mandir}/man1/dnetc.1.gz
%attr(0644, dnetc, dnetc) %{_localstatedir}/log/dnetc.log
%dir %attr(0755, dnetc, dnetc) /var/lib/dnetc


%changelog
* Wed Jan 25 2017 Eugene E. Kashpureff Jr <eugene@kashpureff.org>
- Update to new dnetc version
- Modernize packaging

* Fri Nov 14 2014 Eugene E. Kashpureff Jr <eugene@kashpureff.org>
- First RPM package for EL7
