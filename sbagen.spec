Summary:	A Sequenced Binaural Wave Generator
Summary(pl):	Program generuj�cy d�wi�k do synchronizacji p�kulowej
Name:		sbagen
Version:	1.0.9
Release:	1
License:	GPL v2
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/sbagen/%{name}-%{version}.tgz
# Source0-md5:	d9b10ad330736ffc2064b25659ff44e8
URL:		http://sourceforge.net/projects/sbagen/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sbagen may be used to generate sounds that entrain the brain's waves
to oscillate at selected frequencies to aid in relaxation, lucid
dreaming, meditation, clear thought, out-of-body experiences and more.

%description -l pl
Sbagen s�u�y do generowania d�wi�k�w (z przygotowanych ju� wcze�niej
skrypt�w), kt�re pomagaj� przy medytacji, �wiadomym �nieniu (LD),
relaksacji, czysto�ci my�li, do�wiadczeniom poza cia�em (OOBE) i innym
zjawiskom parapsychologicznym. S�ucha� nale�y tego na s�uchawkach
stereofonicznych, przy zamkni�tych oczach z g�ow� najlepiej odchylon�
lekko do ty�u, siedz�c lub le��c w wygodnej pozycji.

%prep
%setup -q

%build
sed -e 'sI//.*$II' -e 's/inline//' <sbagen.c >temp.c
%{__cc} %{rpmcflags} temp.c -o sbagen -lm

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
%doc ChangeLog README *.txt sbagen.lsm
%attr(755,root,root) %{_bindir}/*
