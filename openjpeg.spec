%define oname OpenJPEG
%define oversion %(echo %{version} | sed -e 's/\\./_/g')

%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}
%define lib_dev %mklibname %{name} -d

%define common_description The OpenJPEG library is an open-source JPEG 2000 codec written in C\
language. It has been developed in order to promote the use of JPEG\
2000, the new still-image compression standard from the Joint\
Photographic Experts Group (JPEG).

Name: openjpeg
Version: 1.5.0
Release: 2
Summary: An open-source JPEG 2000 codec 
Source0: http://openjpeg.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0: openjpeg-1.5.0-CVE-2009-5030.diff
Patch1: openjpeg-1.5.0-CVE-2012-3358.diff
License: BSD
Group: System/Libraries
Url: http://www.openjpeg.org/
BuildRequires: cmake

%description
%{common_description}

%package -n %{lib_name}
Summary: %{oname} library
Group: System/Libraries

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with the %{oname} library.

%{common_description}

%files -n %{lib_name}
%{_libdir}/*.so.*





#-----------------------------
%files
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%doc %{_datadir}/doc/%{name}-1.5/

#---------------------------------------------
%package -n %{lib_dev}
Summary: Development tools for programs using the %{oname} library
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n	%{lib_dev}
This package contains the header files and libraries needed for
developing programs using the %{oname} library.

%{common_description}

%files -n %{lib_dev}
%{_includedir}/%{name}-1.5/%{name}.h
%{_libdir}/*.so
%{_datadir}/%{name}-1.5/*.cmake
%{_datadir}/pkgconfig/libopenjpeg1.pc

#---------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .CVE-2009-5030
%patch1 -p1 -b .CVE-2012-3358

%build
%cmake -DOPENJPEG_INSTALL_LIB_DIR=%{_lib}
%make

%install
cd build/
%makeinstall_std
