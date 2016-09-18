#!/bin/bash 
clear
echo "Installing VIP - Autonomous Aerial Vehicle required packages"

echo
echo "Installing required python packages"
sudo pip install -r requirements.txt
echo
echo
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
echo
echo

echo "Cloning opencv repository"
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git

cd /opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j7 # runs7 jobs in parallel
sudo make install
echo "Installation finished"
cd ..
cd ..

