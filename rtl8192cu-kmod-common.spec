%global RepoName rtl8192cu-fixes

Name:		rtl8192cu-kmod-common
Version:	4.0.2
Release:	1%{?dist}
Summary:	Common package for rtl8192cu-kmod

Group:		System Environment/Kernel
License:	GPLv2
URL:		https://github.com/pvaret/%{RepoName}
Source0:	https://github.com/pvaret/%{RepoName}/archive/master.tar.gz

BuildArch:  noarch

%description
Common package for rtl8192cu-kmod

%prep
%setup -q -c -T
mkdir %{name}-%{version}-src
pushd %{name}-%{version}-src
tar xzf %{SOURCE0}
popd

%build

%install
pushd %{name}-%{version}-src/%{RepoName}-master
install -d 0755 $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d
install -m 0644 blacklist-native-rtl8192.conf $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/blacklist-native-rtl8192.conf
install -m 0644 8192cu-disable-power-management.conf $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/8192cu-disable-power-management.conf
popd

%files
%{_sysconfdir}/modprobe.d/*

%changelog
* Tue May 30 2017 Alexei Panov <me AT elemc DOT name> 4.3.14-2
-  Initial build

