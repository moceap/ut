Name:           unreal 
Version:        tournament
Release:        1%{?dist}
Summary:        Unreal Tournament GOTY Edition
License:        EULA
URL:            https://www.unrealtournament.com/
Source0:        setup_ut_goty.exe
Source1:        unreal.tournament_436-multilanguage.goty.run
Source2:        utcustom.sh
Source3:        ut99_logo.png
Requires:       pulseaudio-utils
BuildRequires:  innoextract
BuildRequires:  desktop-file-utils

%define __requires_exclude libglide.so.2

%description
Unreal Tournament GOTY Edition

%prep
# Way From https://youtu.be/gpu70RvNRyQ
innoextract %{SOURCE0} -d ut1
bash %{SOURCE1} --noexec --target ut2
cp -p %{SOURCE2} .
cp -p %{SOURCE3} .
cp -p ut2/ut.xpm ut1/app
cp -p ut2/bin/ut ut1/app
cp -p ut2/bin/Linux/x86/ucc ut1/app
tar -zxvf ut2/OpenGL.ini.tar.gz -C ut1/app/
tar -zxvf ut2/Credits.tar.gz -C ut1/app/
tar -zxvf ut2/data.tar.gz -C ut1/app/
tar -zxvf ut2/NetGamesUSA.com.tar.gz -C ut1/app/
tar -zxvf ut2/UT436-OpenGLDrv-Linux-090602.tar.gz -C ut1/app/
echo "padsp %{_datadir}/ut/ut" > ut
sed -i 's:GAME_BINARY="ut-bin":GAME_BINARY="../utcustom.sh":g' ut1/app/ut
echo '[Desktop Entry]
Type=Application
Categories=Game;
Exec=ut
Icon=ut
Terminal=false
Name=Unreal Tournament
GenericName=Unreal Tournament
Comment=Unreal Tournament GOTY Edition' > ut.desktop

%build
#nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/ut
mkdir -p %{buildroot}%{_bindir}
cp -pr ut1/app/* %{buildroot}%{_datadir}/ut
install -m 644 ut99_logo.png %{buildroot}%{_datadir}/pixmaps/ut.png
install -m 755 utcustom.sh %{buildroot}%{_datadir}/ut
install -m 755 ut %{buildroot}%{_bindir}
desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
    ut.desktop

%files
%license ut1/tmp/gog_EULA.txt ut1/app/innosetup_license.txt ut1/app/MD5_MIT_license.txt
%doc ut1/app/Manual/Manual.pdf ut1/app/Help ut2/README ut2/README.Loki
%{_datadir}/pixmaps/ut.png
%{_datadir}/applications/ut.desktop
%{_datadir}/ut
%{_bindir}/ut

%changelog
* Wed Jul 15 2015 Mosaab Alzoubi <moceap@hotmail.com> - tournament-1
- First build for Fedora
