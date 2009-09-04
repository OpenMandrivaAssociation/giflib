%define major 4
%define libname %mklibname gif %major
%define develname %mklibname -d gif

Name:		giflib
Version:	4.1.6
Release:	%mkrel 2
URL:		http://giflib.sourceforge.net/
Summary:	Library for reading and writing gif images
License:	BSD like
Source:		%{name}-%{version}.tar.bz2
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%description
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

%package progs
Summary:	Gif tools based on giflib
Group:		Graphics

%description progs
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

This package provides some gif tools based on giflib.

%package -n %libname
Group:		System/Libraries
Summary:	Library for reading and writing gif images

%description -n %libname
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

%package -n %develname
Group:		Development/C
Summary:	Development files for giflib
Requires:	%libname
Provides:	giflib-devel = %{version}-%{release}

%description -n %develname
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

This packages provides the developement files for giflib.

%prep
%setup -q

%build
%configure
%make

%clean
%{__rm} -Rf %{buildroot}

%install
%{__rm} -Rf %{buildroot}
%makeinstall

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files progs
%doc AUTHORS BUGS COPYING ChangeLog NEWS ONEWS README TODO
%{_bindir}/gif2epsn
%{_bindir}/gif2ps
%{_bindir}/gif2rgb
%{_bindir}/gifasm
%{_bindir}/gifbg
%{_bindir}/gifburst
%{_bindir}/gifclip
%{_bindir}/gifclrmp
%{_bindir}/gifcolor
%{_bindir}/gifcomb
%{_bindir}/gifcompose
%{_bindir}/giffiltr
%{_bindir}/giffix
%{_bindir}/gifflip
%{_bindir}/gifhisto
%{_bindir}/gifinfo
%{_bindir}/gifinter
%{_bindir}/gifinto
%{_bindir}/gifovly
%{_bindir}/gifpos
%{_bindir}/gifrotat
%{_bindir}/gifrsize
%{_bindir}/gifspnge
%{_bindir}/giftext
%{_bindir}/gifwedge
%{_bindir}/icon2gif
%{_bindir}/raw2gif
%{_bindir}/rgb2gif
%{_bindir}/text2gif

%files -n %libname
%doc AUTHORS BUGS COPYING ChangeLog NEWS ONEWS README TODO
%{_libdir}/libgif.so.%{major}
%{_libdir}/libgif.so.%{major}.*

%files -n %develname
%{_includedir}/gif_lib.h
%{_libdir}/libgif.a
%{_libdir}/libgif.la
%{_libdir}/libgif.so
