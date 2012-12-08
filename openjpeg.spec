%define oname OpenJPEG
%define oversion %(echo %{version} | sed -e 's/\\./_/g')

%define lib_major 5
%define lib_name %mklibname %{name} %{lib_major}
%define lib_dev %mklibname %{name} -d

%define common_description The OpenJPEG library is an open-source JPEG 2000 codec written in C\
language. It has been developed in order to promote the use of JPEG\
2000, the new still-image compression standard from the Joint\
Photographic Experts Group (JPEG).

Name: openjpeg
Version: 1.5.1
Release: 3
Summary: An open-source JPEG 2000 codec 
Source0: http://openjpeg.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0: openjpeg-1.3-Makefile.patch
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
%{_libdir}/*.so.%{lib_major}
%{_libdir}/*.so.%{version}





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
Requires: %{name} = %{version}
Provides: %{name}-devel = %{version}-%{release}

%description -n	%{lib_dev}
This package contains the header files and libraries needed for
developing programs using the %{oname} library.

%{common_description}

%files -n %{lib_dev}
%{_includedir}/%{name}-1.5/%{name}.h
%{_libdir}/*.so
%{_libdir}/%{name}-1.5/*.cmake
%{_libdir}/pkgconfig/libopenjpeg1.pc

#---------------------------------------------

%prep
%setup -q

%build
%cmake -DOPENJPEG_INSTALL_LIB_DIR=%{_lib}
%make

%install
cd build/
%makeinstall_std


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.5.0-1
+ Revision: 786938
- BR:cmake
- version update 1.5.0

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3-8
+ Revision: 666953
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3-7mdv2011.0
+ Revision: 607018
- rebuild

* Mon Dec 21 2009 Funda Wang <fwang@mandriva.org> 1.3-6mdv2010.1
+ Revision: 480780
- add gentoo patch (bug#50606)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.3-5mdv2010.0
+ Revision: 426345
- rebuild

* Sun Aug 03 2008 Helio Chissini de Castro <helio@mandriva.com> 1.3-4mdv2009.0
+ Revision: 262256
- Push new openjpeg build. Needed for kde4 okular

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.3-3mdv2009.0
+ Revision: 254780
- rebuild

* Sun Mar 02 2008 Olivier Blin <blino@mandriva.org> 1.3-1mdv2008.1
+ Revision: 177766
- fix lib install on x86_64
- 1.3
- rediff inst patch
- use makeinstall_std

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 1.1.1-1mdv2008.1
+ Revision: 141036
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

