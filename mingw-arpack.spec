%?mingw_package_header

Name:           mingw-arpack
Version:        3.5.0
Release:        1%{?dist}
Summary:        MinGW port of ARPACK-NG

License:        BSD
URL:            https://github.com/opencollab/arpack-ng
Source0:        https://github.com/opencollab/arpack-ng/archive/%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-gfortran
BuildRequires:  mingw32-openblas

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-gfortran
BuildRequires:  mingw64-openblas

BuildArch:      noarch

%description
MinGW Windows port of ARPACK-NG.

# Win32
%package -n mingw32-arpack
Summary:        32-bit version of ARPACK-NG for Windows

%description -n mingw32-arpack
%mingw32_description

# Win64
%package -n mingw64-arpack
Summary:        64-bit version of ARPACK-NG for Windows

%description -n mingw64-arpack
%mingw64_description

%?mingw_debug_package

%prep
%setup -qn arpack-ng-%{version}
./bootstrap

%build
%global blaslib -lopenblaso
%mingw_configure \
    --with-blas="%{blaslib}" \
    --with-lapack="%{blaslib}"
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}
find %{buildroot} -name "*.la" -delete

# Win32
%files -n mingw32-arpack
%{mingw32_bindir}/libarpack-2.dll
%{mingw32_libdir}/libarpack.dll.a
%{mingw32_libdir}/libarpack.a
%{mingw32_libdir}/pkgconfig/arpack.pc

# Win64
%files -n mingw64-arpack
%{mingw64_bindir}/libarpack-2.dll
%{mingw64_libdir}/libarpack.dll.a
%{mingw64_libdir}/libarpack.a
%{mingw64_libdir}/pkgconfig/arpack.pc

%changelog
* Fri Nov 10 2017 Jajauma's Packages <jajauma@yandex.ru> - 3.5.0-1
- Initial release
