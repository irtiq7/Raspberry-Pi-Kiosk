from time import sleep
import RPi.GPIO as GPIO
import time
import os
from subprocess import Popen

folder1 = "/media/pi/PRESENT/PRESENTATION/Button1/"
folder2 = "/media/pi/PRESENT/PRESENTATION/Button2/"
folder3 = "/media/pi/PRESENT/PRESENTATION/Button3/"
folder4 = "/media/pi/PRESENT/PRESENTATION/Button4/"
image_file = "/media/pi/PRESENT/PRESENTATION/image.jpg"
video_file = "video.mp4"

def read_folderfile4(folder):
	folder_files= os.listdir(folder)
	print folder_files
	for image_type in (folder_files):
		if image_type.endswith(".jpg"):
			print image_type
			os.system("sudo fbi -T 1 "+folder+"%s"%str(image_type))
			#~ time.sleep(2)
		elif image_type.endswith("loop.mp4"):
			Popen(['omxplayer', '-b', '--loop',folder+"%s"%str(image_type)])
		else:
			print image_type
			Popen(['omxplayer', '-b', folder+"%s"%str(image_type)])

def read_folderfile2(folder):
	folder_files= os.listdir(folder)
	print folder_files
	i=0
	while(i!=len(folder_files)):
		image_type = folder_files[i]
		os.system("sudo fbi -T 1 "+folder2+"%s"%str(image_type))
		while(not GPIO.input(26)):
			print "pass"
			pass
		i=i+1
		time.sleep(0.3)
	omxc = Popen(['killall', 'omxplayer.bin'])
	os.system("sudo fbi -T 1 "+image_file)

def read_folderfile1(folder):
	folder_files= os.listdir(folder)
	print folder_files
	for image_type in (folder_files):
		
		if image_type.endswith(".jpg"):
			print image_type
			#~ os.system("sudo fbi -T 1 /media/pi/44F3-214D/PRESENTATION/Button2/%s"%str(image_type))
			Popen(['fbi', '-T', "1",folder+"%s"%str(image_type)])
			time.sleep(5)
		elif image_type.endswith("loop.mp4"):
			Popen(['omxplayer', '-b', '--loop',folder+"%s"%str(image_type)])
		else:
			print image_type
			Popen(['omxplayer', '-b', folder+"%s"%str(image_type)])

def read_folderfile3(folder):
	folder_files= os.listdir(folder)
	print folder_files
	for image_type in (folder_files):
		if image_type.endswith(".jpg"):
			print image_type
			os.system("sudo fbi -T 1 "+folder+"%s"%str(image_type))
			#~ time.sleep(2)
		elif image_type.endswith("loop.mp4"):
			Popen(['omxplayer', '-b', '--loop',folder+"%s"%str(image_type)])
		else:
			print image_type
			Popen(['omxplayer', '-b', folder+"%s"%str(image_type)])

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

last_state1 = True
last_state2 = True
last_state3 = True
last_state4 = True
last_state5 = True

input_state1 = True
input_state2 = True
input_state3 = True
input_state4 = True
input_state5 = True
quit_video = True
player = False

os.system("sudo fbi -T 1 "+image_file)
while True:
	#Read states of inputs
	input_state1 = GPIO.input(17)
	input_state4 = GPIO.input(19)
	input_state2 = GPIO.input(24)
	input_state3 = GPIO.input(18)
	input_state5 = GPIO.input(26)

	#If GPIO(17) is shorted to ground
	if input_state1 != last_state1:
		if (player and not input_state1):
			os.system('killall omxplayer.bin')
			#~ omxc = os.system("sudo omxplayer -b video.mp4")
			#~ omxc = Popen(['omxplayer', '-b', video_file])
			omxc = read_folderfile1(folder1)
			player = True
		elif not input_state1:
			#~ os.system("sudo omxplayer -b video.mp4")
			omxc = read_folderfile1(folder1)
			player = True
		print "button 1"
	#If GPIO(24) is shorted to ground
	elif input_state2 != last_state2:
		if (player and not input_state2):
			#~ os.system('killall omxplayer.bin')
			omxc = Popen(['killall', 'omxplayer.bin'])
			os.system("sudo fbi -T 1 "+image_file)
			#~ omxc = read_folderfile(folder2)
			player = True
		elif not input_state2:
			omxc = Popen(['killall', 'omxplayer.bin'])
			os.system("sudo fbi -T 1 "+image_file)
			#~ omxc = read_folderfile(folder2)
			player = True
		print "button 2"
	#If GPIO(19) is shorted to ground
	elif input_state4 != last_state4:
		if (player and not input_state4):
			os.system('killall omxplayer.bin')
			#~ omxc = os.system("sudo omxplayer -b video.mp4")
			#~ omxc = Popen(['omxplayer', '-b', video_file])
			omxc = read_folderfile4(folder4)
			player = True
		elif not input_state4:
			#~ os.system("sudo omxplayer -b video.mp4")
			omxc = read_folderfile4(folder4)
			player = True
		print "button 4"
	#If GPIO(18) is shorted to ground
	elif input_state3 != last_state3:
		if (player and not input_state3):	
			os.system('killall omxplayer.bin')
			#~ omxc = os.system("sudo omxplayer -b video.mp4")
			#~ omxc = Popen(['omxplayer', '-b', video_file])
			omxc = read_folderfile3(folder3)
			player = True
		elif not input_state3:
			#~ os.system("sudo omxplayer -b video.mp4")
			omxc = read_folderfile3(folder3)
			player = True	
		print "button 3"
	elif input_state5 != last_state5:
		if (player and not input_state5):	
			os.system('killall omxplayer.bin')
			#~ omxc = os.system("sudo omxplayer -b video.mp4")
			#~ omxc = Popen(['omxplayer', '-b', video_file])
			omxc = read_folderfile2(folder2)
			player = True
		elif not input_state3:
			#~ os.system("sudo omxplayer -b video.mp4")
			omxc = read_folderfile2(folder2)
			player = True	
		print "button 5"
	#Set last_input states
	last_state1 = input_state1
	last_state2 = input_state2
	last_state3 = input_state3
	last_state4 = input_state4
	last_state5 = input_state5

