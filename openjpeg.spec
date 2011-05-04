%define oname OpenJPEG
%define oversion %(echo %{version} | sed -e 's/\\./_/g')

%define lib_major 2
%define lib_name %mklibname %{name} %{lib_major}
%define lib_dev %mklibname %{name} -d

%define common_description The OpenJPEG library is an open-source JPEG 2000 codec written in C\
language. It has been developed in order to promote the use of JPEG\
2000, the new still-image compression standard from the Joint\
Photographic Experts Group (JPEG).

Name: openjpeg
Version: 1.3
Release: %mkrel 8
Summary: An open-source JPEG 2000 codec 
Source0: %{name}_v%{oversion}.tar.gz
Patch0: openjpeg-1.3-Makefile.patch
License: BSD
Group: System/Libraries
Url: http://www.openjpeg.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%defattr(-,root,root)
%{_libdir}/*.so.*

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
%defattr(-,root,root)
%{_includedir}/%{name}.h
%{_libdir}/*.a
%{_libdir}/*.so

#---------------------------------------------

%prep
%setup -q -n %{oname}_v%{oversion}
%patch0 -p1 -b .inst

%build
%make CFLAGS="%{optflags} -fPIC" LDFLAGS="%{ldflags}"

%install
rm -rf %buildroot
%makeinstall_std INSTALL_LIBDIR=%{_libdir}

%clean
rm -rf %buildroot


