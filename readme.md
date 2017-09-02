<embed width="420" height="315" src="https://www.youtube.com/watch?v=S2YmGoWgN1U&feature=youtu.be">

<b>Procedure:</b>

This repository is used to run videos and display images on a raspberry pi on fullscreen using OMXPLAYER and FBI image viewer
The software will display a single background image of your choosing and play the video every time the play switch is pressed.

<b>How do I get set up the Raspberry Pi?</b>

Wire up the connections as shown:
<img src="https://github.com/irtiq7/Raspberry-Pi-Kiosk/blob/master/RPi_kiosk_schem.jpg?raw=true">

<b>How do I get set up Raspbian OS?</b>

This code was prepared on Raspbian Pixel OS (latest from Raspberry Pi foundation)
First download and copy Raspbian Jessie Pixel on your SD card and power on the Raspberry Pi.

Upgrade to the latest OS library.

    sudo apt-get update
    sudo apt-get upgrade
  
You will need to download the following tools to run the code effectively,

    Install OMXPLAYER from the terminal.
    sudo apt-get install omxplayer
    Install FBI image viewer:
    sudo apt-get update
    sudo apt-get -y install fbi
  
Once the above two libraries are installed. Download and run the python file: kiosk_player.py
The file structure should be as follows:

    Kiosk folder:
    |-----kiosk_player.py
    |-----video.mp4
    |-----image.jpg

You should make a folder Kiosk and inside the folder you should have the image and video file of your choice.

Watch Video on : https://www.youtube.com/watch?v=S2YmGoWgN1U&feature=youtu.be
