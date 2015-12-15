#!/bin/bash
echo "Egal bei welchem Wetter.....im Stecker!"
#if [[ "$(cat firstrun)" == "1" ]];then
#echo "0" >firstrun
#sudo reboot
#else 
#echo "1"> firstrun
#fi
sleep 10
sudo rm /home/pi/steckerfoto/upload/*
sudo sshfs raspi@10.26.180.11:/srv/www/fotos/html/selfi /home/pi/steckerfoto/upload -o IdentityFile=/home/pi/.ssh/id_rsa
cd /home/pi/steckerfoto && sudo python photobooth.py &
