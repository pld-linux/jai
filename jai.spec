# NOTE:
# there are (Java only, no native code) sources available on less-restrictive
# JDL license (from CVS only)
Summary:	Java Advanced Imaging (JAI) API
Summary(pl.UTF-8):	Java Advanced Imaging (JAI) - zaawansowane API do obrazów
Name:		jai
Version:	1.1.3
Release:	1
License:	Sun Binary Code License (restricted, non-distributable)
Group:		Libraries
# Download URL: https://jai.dev.java.net/binary-builds.html
Source0:	http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-i586.tar.gz
# NoSource0-md5:	a2cbc155ef3899bcde9c74a8035764b3
Source1:	http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib-linux-amd64.tar.gz
# NoSource1-md5:	4a906db35612f668aeef2c0606d7075b
Source2:	http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1_3-lib.zip
# NoSource2-md5:	ca8b26b359fcb2fa2c34b77add9af808
Source3:	http://download.java.net/media/jai/builds/release/1_1_3/jai-1_1-mr-doc.zip
# NoSource3-md5:	1e08a7b4b754dcb4576f165286212f5f
NoSource:	0
NoSource:	1
NoSource:	2
NoSource:	3
URL:		https://jai.dev.java.net/
BuildRequires:	jpackage-utils
BuildRequires:	rpmbuild(macros) >= 1.294
BuildRequires:	unzip
Requires:	jre
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Java Advanced Imaging API (JAI) provides a set of object-oriented
interfaces that supports a simple, high-level programming model which
allows images to be manipulated easily in Java applications and
applets. JAI goes beyond the functionality of traditional imaging APIs
to provide a high-performance, platform-independent, extensible image
processing framework.

%description -l pl.UTF-8
API Java Advanced Imaging (JAI) udostępnia zbiór zorientowanych
obiektowo interfejsów wspomagających prosty, wysokopoziomowy model
programowania, pozwalając na łatwą obróbkę obrazów w aplikacjach i
apletach Javy. JAI wychodzi poza funkcjonalność tradycyjnych API do
obrazów dostarczając wysoko wydajny, niezależny od platformy i
rozszerzalny szkielet do przetwarzania obrazów.

%package javadoc
Summary:	JAI documentation
Summary(pl.UTF-8):	Dokumentacja biblioteki JAI
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
JAI documentation.

%description javadoc -l pl.UTF-8
Dokumentacja biblioteki JAI.

%prep
%ifarch i586 i686 pentium3 pentium4 athlon
%setup -q -n jai-1_1_3
%else
%ifarch %{x8664}
%setup -q -n jai-1_1_3 -T -b1
%else
%setup -q -n jai-1_1_3 -T -b2
%endif
%endif
install -d docs
unzip -qq %{SOURCE3} -d docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install lib/*.jar $RPM_BUILD_ROOT%{_javadir}
%ifarch %{ix86}
install -D lib/libmlib_jai.so $RPM_BUILD_ROOT%{java_home}/jre/lib/i386/libmlib_jai.so
%endif
%ifarch %{x8664}
install -D lib/libmlib_jai.so $RPM_BUILD_ROOT%{java_home}/jre/lib/amd64/libmlib_jai.so
%endif

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
rm -f %{_javadocdir}/%{name}
ln -s %{name}-%{version} %{_javadocdir}/%{name}

%postun javadoc
if [ "$1" = "0" ]; then
	rm -f %{_javadocdir}/%{name}
fi

%files
%defattr(644,root,root,755)
%doc COPYRIGHT-jai.txt LICENSE-jai.txt THIRDPARTYLICENSEREADME-jai.txt DISTRIBUTIONREADME-jai.txt
%ifarch i586 i686 pentium3 pentium4 athlon
%attr(755,root,root) %{java_home}/jre/lib/i386/libmlib_jai.so
%{_javadir}/mlibwrapper_jai.jar
%endif
%ifarch %{x8664}
%attr(755,root,root) %{java_home}/jre/lib/amd64/libmlib_jai.so
%{_javadir}/mlibwrapper_jai.jar
%endif
%{_javadir}/jai_codec.jar
%{_javadir}/jai_core.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
