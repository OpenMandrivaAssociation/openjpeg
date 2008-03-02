%define name openjpeg
%define version 1.3
%define oname OpenJPEG
%define oversion %(echo %{version} | sed -e 's/\\./_/g')
%define release %mkrel 1

%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}

%define common_description The OpenJPEG library is an open-source JPEG 2000 codec written in C\
language. It has been developed in order to promote the use of JPEG\
2000, the new still-image compression standard from the Joint\
Photographic Experts Group (JPEG).

Summary: An open-source JPEG 2000 codec 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_v%{oversion}.tar.gz
Patch0: openjpeg-1.3-inst.patch
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

%package -n %{lib_name}-devel
Summary: Development tools for programs using the %{oname} library
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n	%{lib_name}-devel
This package contains the header files and libraries needed for
developing programs using the %{oname} library.

%{common_description}

%prep
%setup -q -n %{oname}_v%{oversion}
%patch0 -p1 -b .inst

%build
%make CFLAGS="$RPM_OPT_FLAGS -fPIC"

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}.h
%{_libdir}/*.a
%{_libdir}/*.so


