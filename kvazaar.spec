# Todo: make main program dinamically linked

Name:           kvazaar
Version:        1.1.0
Release:        1%{?dist}
Summary:        An open-source HEVC encoder
License:        LGPLv2+
URL:            http://ultravideo.cs.tut.fi/#encoder

Source0:        https://github.com/ultravideo/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Fix GCC 7 build
Patch0:         https://github.com/ultravideo/kvazaar/commit/47a9f0de049e77e866ea5bdd4bc7c795ea6dd641.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

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
%autosetup -p1
autoreconf -vif
%configure --disable-static

%build
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -name '*.la' -delete

# Pick up docs in the files section
rm -fr %{buildroot}%{_docdir}

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README.md CREDITS
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
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
