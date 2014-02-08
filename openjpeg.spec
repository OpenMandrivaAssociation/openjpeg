%define	oname	OpenJPEG
%define	major	5
%define	libname	%mklibname %{name} %{major}
%define	libdev	%mklibname %{name} -d

%define common_description The OpenJPEG library is an open-source JPEG 2000 codec written in C\
language. It has been developed in order to promote the use of JPEG\
2000, the new still-image compression standard from the Joint\
Photographic Experts Group (JPEG).

Summary:	An open-source JPEG 2000 codec 
Name:		openjpeg
Version:	1.5.1
Release:	12
License:	BSD
Group:		System/Libraries
Url:		http://www.openjpeg.org/
Source0:	http://openjpeg.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		openjpeg-1.5.1-fix-cmake-generated-pkgconfig.patch
Patch1:		openjpeg-fpic.patch
BuildRequires:	cmake
BuildRequires:	png-devel
BuildRequires:	tiff-devel
BuildRequires:	lcms2-devel

%description
%{common_description}

%package -n	%{libname}
Summary:	%{oname} library
Group:		System/Libraries
%rename		%{_lib}%{name}1

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with the %{oname} library.

%{common_description}

%package -n	%{libdev}
Summary:	Development tools for programs using the %{oname} library
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{name} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{libdev}
This package contains the header files and libraries needed for
developing programs using the %{oname} library.

%{common_description}

%prep
%setup -q
%patch0 -p1 -b .pkgconfig~
%patch1 -p1 -b .fpic

%build
%cmake	-DOPENJPEG_INSTALL_BIN_DIR:PATH=%{_bindir} \
	-DOPENJPEG_INSTALL_DATA_DIR:PATH=%{_datadir} \
	-DOPENJPEG_INSTALL_INCLUDE_DIR:PATH=%{_includedir} \
	-DOPENJPEG_INSTALL_LIB_DIR:PATH=%{_libdir}

%make

%install
%makeinstall_std -C build

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%doc %{_datadir}/doc/%{name}-1.5/

%files -n %{libname}
%{_libdir}/libopenjpeg.so.%{major}
%{_libdir}/libopenjpeg.so.%{version}

%files -n %{libdev}
%{_includedir}/%{name}.h
%{_libdir}/libopenjpeg.so
%{_libdir}/%{name}-1.5/*.cmake
%{_libdir}/pkgconfig/libopenjpeg1.pc
