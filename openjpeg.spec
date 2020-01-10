%define oname OpenJPEG
%define major 5
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	An open-source JPEG 2000 codec 
Name:		openjpeg
Version:	1.5.2
Release:	7
License:	BSD
Group:		System/Libraries
Url:		http://www.openjpeg.org/
Source0:	http://openjpeg.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		openjpeg-1.5.1-fix-cmake-generated-pkgconfig.patch
Patch1:		openjpeg-fpic.patch
BuildRequires:	cmake
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(lcms2)

%description
The OpenJPEG library is an open-source JPEG 2000 codec written in C
language. It has been developed in order to promote the use of JPEG
2000, the new still-image compression standard from the Joint
Photographic Experts Group (JPEG).

%package -n %{libname}
Summary:	%{oname} library
Group:		System/Libraries
%rename		%{_lib}%{name}1

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with the %{oname} library.

%package -n	%{devname}
Summary:	Development tools for programs using the %{oname} library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package contains the header files and libraries needed for
developing programs using the %{oname} library.

%prep
%setup -q
%autopatch -p1

%build
%cmake	-DOPENJPEG_INSTALL_BIN_DIR:PATH=%{_bindir} \
	-DOPENJPEG_INSTALL_DATA_DIR:PATH=%{_datadir} \
	-DOPENJPEG_INSTALL_INCLUDE_DIR:PATH=%{_includedir} \
	-DOPENJPEG_INSTALL_LIB_DIR:PATH=%{_libdir}

%make

%install
%makeinstall_std -C build
rm -fr %{buildroot}%{_docdir}/%{name}-1.5

%files
%{_bindir}/*
%{_mandir}/man1/*
%doc doc/*

%files -n %{libname}
%{_libdir}/libopenjpeg.so.%{major}
%{_libdir}/libopenjpeg.so.%{version}

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/libopenjpeg.so
%{_libdir}/%{name}-1.5/*.cmake
%{_libdir}/pkgconfig/libopenjpeg1.pc
%{_mandir}/man3/*
