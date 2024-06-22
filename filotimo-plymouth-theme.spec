Name:           filotimo-plymouth-theme
Version:        0.1
Release:        1%{?dist}
Summary:        Jimmac's spinner theme using the ACPI BGRT graphics as background - customised for Filotimo Linux

License:        GPL-2.0
URL:            https://github.com/filotimo-linux/plymouth-theme
Source0:        %{name}-%{version}.tar.gz

Requires:       rsms-inter-fonts
#Requires:       filotimo-branding-plymouth

%description
Jimmac's spinner theme using the ACPI BGRT graphics as background - customised for Filotimo Linux.
Uses the Breeze cog as a spinner. Requires filotimo-branding-plymouth for the watermark.

%prep
%setup -q

%build

%install
cd src
install -pm 0644 %{SOURCE0} LICENSE
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/filotimo
cp ./* %{buildroot}%{_datadir}/plymouth/themes/filotimo


%files
%license LICENSE
%dir %{_datadir}/plymouth/themes/filotimo
%{_datadir}/plymouth/themes/filotimo/*

%changelog
