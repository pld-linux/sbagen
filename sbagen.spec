Summary:	A Sequenced Binaural Wave Generator
Summary(pl.UTF-8):   Program generujący dźwięk do synchronizacji półkulowej
Name:		sbagen
Version:	1.4.1
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/sbagen/%{name}-%{version}.tgz
# Source0-md5:	7d672f2f2a8e33e664b06777459471fe
URL:		http://sourceforge.net/projects/sbagen/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sbagen may be used to generate sounds that entrain the brain's waves
to oscillate at selected frequencies to aid in relaxation, lucid
dreaming, meditation, clear thought, out-of-body experiences and more.

%description -l pl.UTF-8
Sbagen służy do generowania dźwięków (z przygotowanych już wcześniej
skryptów), które pomagają przy medytacji, świadomym śnieniu (LD),
relaksacji, czystości myśli, doświadczeniom poza ciałem (OOBE) i innym
zjawiskom parapsychologicznym. Słuchać należy tego na słuchawkach
stereofonicznych, przy zamkniętych oczach z głową najlepiej odchyloną
lekko do tyłu, siedząc lub leżąc w wygodnej pozycji.

%prep
%setup -q

%build
#sed -e 'sI//.*$II' -e 's/inline//' <sbagen.c >temp.c
./mk
#%{__cc} %{rpmcflags} temp.c -o sbagen -lm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install sbagen $RPM_BUILD_ROOT%{_bindir}
install t-* $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install prog* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
