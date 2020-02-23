#!/bin/bash
if grep -qs "Ubuntu" /etc/os-release; then
sudo apt install python3 python3-pip -y
elif grep -qs "Debian GNU/Linux" /etc/os-release; then
sudo apt install python3 python3-pip -y
elif grep -qs "Arch Linux" /etc/os-release; then
sudo pacman -S python3 python-pip --noconfirm
elif grep -qs "CentOS" /etc/redhat-release; then
sudo yum -y install python3 python3-pip
else
exit
fi

pip3 install PyQt5

mkdir ~/.openvpn
mv main.py ~/.openvpn
mv openvpn.png ~/.openvpn
read -p 'Enter your openvpn config full path (.ovpn file) ' ovpn
mv $ovpn ~/.openvpn/vpn.ovpn

echo "[Unit]
Description=OpenVPN service

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=$HOME
ExecStart=openvpn $HOME/.openvpn/vpn.ovpn
Restart=on-failure

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/myovpn.service

echo "[Desktop Entry]
Name=OpenVPN GUI
Exec=python3 $HOME/.openvpn/main.py
Type=Application
Icon= $HOME/.openvpn/openvpn.png" | sudo tee /usr/share/applications/openvpngui.desktop
