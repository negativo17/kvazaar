# Todo: make main program dinamically linked

Name:           kvazaar
Version:        2.0.0
Release:        1%{?dist}
Summary:        An open-source HEVC encoder
License:        LGPLv2+
URL:            http://ultravideo.cs.tut.fi/#encoder

Source0:        https://github.com/ultravideo/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  yasm

%description
Kvazaar is the leading academic open-source HEVC encoder developed from scratch
in C. This package contains the application for encoding videos.

%package        libs
Summary:        HEVC encoder %{name} libraries

%description    libs
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}. This package contains the shared libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup
autoreconf -vif
%configure --enable-static=no

%build
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

# Pick up docs in the files section
rm -fr %{buildroot}%{_docdir}

%ldconfig_scriptlets

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

%files libs
%license COPYING
%doc README.md CREDITS
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat May 23 2020 Simone Caronni <negativo17@gmail.com> - 2.0.0-1
- Update to 2.0.0.
- Update SPEC file.

* Sat Jan 11 2020 Simone Caronni <negativo17@gmail.com> - 1.3.0-1
- Update to 1.3.0.

* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-2
- Add GCC build requirement.

* Tue Jan 09 2018 Simone Caronni <negativo17@gmail.com> - 1.2.0-1
- Update to 1.2.0.

* Mon Jul 17 2017 Simone Caronni <negativo17@gmail.com> - 1.1.0-1
- Update to 1.1.0.

* Wed Nov 09 2016 Simone Caronni <negativo17@gmail.com> - 1.0.0-1
- Update to 1.0.0.

* Thu Jul 14 2016 Simone Caronni <negativo17@gmail.com> - 0.8.3-1
- Update to 0.8.3.

* Fri Mar 04 2016 Simone Caronni <negativo17@gmail.com> - 0.8.2-1
- Update to 0.8.2, remove old build/install procedure.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 0.7.2-1
- First build.
