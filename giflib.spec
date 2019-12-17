%define major 7
%define libname %mklibname gif %{major}
%define devname %mklibname -d gif

%global optflags %{optflags} -O3

# (tpg) enable PGO build
# (tpg) 2019-12-17 BUILDSTDERR: ld: error: undefined symbol: GifErrorString
%bcond_with pgo

Summary:	Library for reading and writing gif images
Name:		giflib
Version:	5.2.1
Release:	3
Group:		System/Libraries
License:	BSD like
Url:		http://giflib.sourceforge.net/
Source0:	https://netcologne.dl.sourceforge.net/project/giflib/giflib-%{version}.tar.gz
Patch0:		https://src.fedoraproject.org/rpms/giflib/raw/master/f/giflib_quantize.patch
Patch1:		https://git.archlinux.org/svntogit/packages.git/plain/trunk/giflib-5.1.9-make-flags.patch
#BuildRequires:	xmlto
BuildRequires:	pkgconfig(x11)

%description
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

%package progs
Summary:	Gif tools based on giflib
Group:		Graphics
%rename		libungif-progs

%description progs
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

This package provides some gif tools based on giflib.

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for reading and writing gif images

%description -n %{libname}
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

%package -n %{devname}
Group:		Development/C
Summary:	Development files for giflib
Requires:	%{libname} = %{version}-%{release}
Provides:	giflib-devel = %{version}-%{release}
Provides:	ungif-devel = %{version}-%{release}
%rename		%{_lib}ungif4-devel

%description -n %{devname}
giflib is a library for reading and writing gif images. It is API and
ABI compatible with libungif which was in wide use while the LZW
compression algorithm was patented.

This packages provides the developement files for giflib.

%prep
%autosetup -p1

%build
%set_build_flags
# remove weird docs
#sed -i 's!$(MAKE) -C doc!!g' Makefile
%if %{with pgo}
export LLVM_PROFILE_FILE=%{name}-%p.profile.d
export LD_LIBRARY_PATH="$(pwd)"
CFLAGS="%{optflags} -fprofile-instr-generate" \
CXXFLAGS="%{optflags} -fprofile-instr-generate" \
FFLAGS="$CFLAGS" \
FCFLAGS="$CFLAGS" \
LDFLAGS="%{ldflags} -fprofile-instr-generate" \
%make_build CFLAGS="%{optflags}" PREFIX="%{_prefix}" LIBDIR="%{_libdir}" MANDIR="%{_mandir}/man1" CC="%{__cc}" all

make check

unset LD_LIBRARY_PATH
unset LLVM_PROFILE_FILE
llvm-profdata merge --output=%{name}.profile *.profile.d

make clean

CFLAGS="%{optflags} -fprofile-instr-use=$(realpath %{name}.profile)" \
CXXFLAGS="%{optflags} -fprofile-instr-use=$(realpath %{name}.profile)" \
LDFLAGS="%{ldflags} -fprofile-instr-use=$(realpath %{name}.profile)" \
%endif
%make_build CFLAGS="%{optflags}" PREFIX="%{_prefix}" LIBDIR="%{_libdir}" MANDIR="%{_mandir}/man1" CC="%{__cc}" all

%install
%make_install CFLAGS="%{optflags}" PREFIX="%{_prefix}" LIBDIR="%{_libdir}" MANDIR="%{_mandir}/man1" CC="%{__cc}"

# Let's try to keep -lungif working for really old code
ln -s libgif.so %{buildroot}%{_libdir}/libungif.so
rm %{buildroot}%{_libdir}/*.a

%files progs
%doc COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libgif.so.%{major}*

%files -n %{devname}
%{_includedir}/gif_lib.h
%{_libdir}/*.so
