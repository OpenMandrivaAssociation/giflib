%define major 6
%define	libname	%mklibname gif %{major}
%define	devname	%mklibname -d gif

Summary:	Library for reading and writing gif images
Name:		giflib
Version:	5.0.4
Release:	1
Group:		System/Libraries
License:	BSD like
URL:		http://giflib.sourceforge.net/
Source0:	http://switch.dl.sourceforge.net/project/giflib/giflib-5.x/giflib-%version.tar.bz2
Patch2:		giflib-4.2.1-automake-1.13.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	xmlto

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
%patch2 -p1 -b .am13~
autoreconf -fi

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Let's try to keep -lungif working for really old code
ln -s libgif.so %buildroot%_libdir/libungif.so

%files progs
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%_bindir/*
%_mandir/man1/*

%files -n %{libname}
%{_libdir}/libgif.so.%{major}*

%files -n %{devname}
%{_includedir}/gif_lib.h
%{_libdir}/*.so


%changelog
* Wed Jan 04 2012 Matthew Dawkins <mattydaw@mandriva.org> 4.1.6-14
+ Revision: 752672
- rebuild for .la files
- split up libungif pkg
- disabled static build
- cleaned up spec (more could be done)

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1.6-11
+ Revision: 664831
- mass rebuild

* Mon Mar 21 2011 Funda Wang <fwang@mandriva.org> 4.1.6-10
+ Revision: 647240
- bump requires

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 4.1.6-9
+ Revision: 633913
- fix linkage

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.6-8mdv2011.0
+ Revision: 605455
- rebuild

* Tue Jan 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.6-7mdv2010.1
+ Revision: 486488
- Provide libungif-devel

* Tue Jan 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.6-6mdv2010.1
+ Revision: 486305
- Add forgotten provide

* Mon Jan 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.6-5mdv2010.1
+ Revision: 486194
- Fix provides/obsoletes

* Mon Jan 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.6-4mdv2010.1
+ Revision: 486179
- Handle of libungif compatibility

* Mon Jan 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 4.1.6-3mdv2010.1
+ Revision: 486154
- Add buildrequire: libx11-devel
- P0: Fix format strings errors
  Fix libtool errors by using %%configure2_5x

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Sep 11 2008 Nicolas Vigier <nvigier@mandriva.com> 4.1.6-1mdv2009.0
+ Revision: 283798
- import giflib


