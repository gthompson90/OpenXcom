#
# spec file for package openxcom
#
# Copyright (c) 2012 Angelos Tzotsos <tzotsos@opensuse.org>
#
# This file and all modifications and additions to the openxcom
# package are licensed under the GPL license.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           openxcom
Version:        0.9.0
Release:        0
Group:          Amusements/Games/Strategy/Turn Based 
License:        GPL-2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            http://openxcom.org/
Source0:        %{name}-%{version}.tar.gz
Summary:        Open source remake of the original X-COM
BuildRequires:  cmake 
BuildRequires:  gcc-c++ 
BuildRequires:  gcc 
BuildRequires:  fdupes
BuildRequires:	pkg-config
BuildRequires:	timidity
Requires:	timidity
BuildRequires:	libSDL-devel
BuildRequires:	libSDL_mixer-devel
BuildRequires:	libSDL_image-devel
BuildRequires:	libSDL_gfx-devel >= 2.0.21
BuildRequires:	yaml-cpp-devel < 0.5.0

%description
OpenXcom is an open-source remake of the popular UFO: Enemy Unknown (X-COM: UFO Defense in USA) video game by Microprose, licensed under the GPL and written in C++ / SDL. OpenXcom requires game resources from the original game (DOS, Windows or Steam version)

%prep
%setup -q

%build
cd ..
mkdir temp
cd temp
cmake  -DBUILD_PACKAGE:BOOL=ON \
       -DDEV_BUILD:BOOL=OFF \
       -DCMAKE_INSTALL_PREFIX:PATH=/usr \
       -DCMAKE_BUILD_TYPE:STRING="Release" ../%{name}-%{version}/

make VERBOSE=1 %{?_smp_mflags}

%install
cd ../temp
make install DESTDIR=%{buildroot}

%fdupes %{buildroot}

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%dir /usr/share/openxcom
/usr/share/openxcom/*
/usr/bin/openxcom

%changelog
