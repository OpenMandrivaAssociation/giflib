%define major	6
%define	libname	%mklibname gif %{major}
%define	devname	%mklibname -d gif

Summary:	Library for reading and writing gif images
Name:		giflib
Version:	5.0.4
Release:	6
Group:		System/Libraries
License:	BSD like
Url:		http://giflib.sourceforge.net/
Source0:	http://switch.dl.sourceforge.net/project/giflib/giflib-5.x/giflib-%version.tar.bz2
Patch2:		giflib-4.2.1-automake-1.13.patch
BuildRequires:	xmlto
BuildRequires:	pkgconfig(x11)

%track
prog %name = {
	url = http://sourceforge.net/projects/giflib/
	regex = %name-(__VER__)\.tar\.bz2
	version = %version
}

%description
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

%package	progs
Summary:	Gif tools based on giflib
Group:		Graphics
%rename		libungif-progs

%description	progs
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

This package provides some gif tools based on giflib.

%package -n	%{libname}
Group:		System/Libraries
Summary:	Library for reading and writing gif images

%description -n	%{libname}
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

%package -n	%{devname}
Group:		Development/C
Summary:	Development files for giflib
Requires:	%{libname} = %{version}-%{release}
Provides:	giflib-devel = %{version}-%{release}
Provides:	ungif-devel = %{version}-%{release}
%rename		%{_lib}ungif4-devel

%description -n	%{devname}
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

This packages provides the developement files for giflib.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

# Let's try to keep -lungif working for really old code
ln -s libgif.so %{buildroot}%{_libdir}/libungif.so

%files progs
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libgif.so.%{major}*

%files -n %{devname}
%{_includedir}/gif_lib.h
%{_libdir}/*.so

