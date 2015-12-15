##Fotoautomat mit Raspberry Pi
#Make 1/15
#

import RPi.GPIO as IO
import time
import picamera
from os.path import basename, splitext
import sys
import getopt
import ftplib
import PIL.Image
import PIL.ImageEnhance
from PIL import Image
import pygame


fuser='pi2'
key='a'
secret='hier bitte eigene Dateneintragen'
list=['3_', '2_', '1_', '0_']


def shot():
   Zeit= time.ctime(time.time())
   Zeit= Zeit.replace(" ", "_")
   Zeit= Zeit.replace(":", "")
   Datei="./upload/stecker" + Zeit+ ".jpg"
   
   for i in list:

     nmbr = Image.open('./' + i + '.png')
     size = Image.new('RGB', (       ((nmbr.size[0] + 31) // 32) * 32,       ((nmbr.size[1] + 15) // 16) * 16, ) )
     size.paste(nmbr, (0, 0))
     c = PiCam.add_overlay(size.tostring(), size=nmbr.size)
     c.alpha = 100
     c.layer = 3
     time.sleep(1)
     PiCam.remove_overlay(c)
  
   print "Aufnahme"
   PiCam.capture(Datei)

   # Load the arbitrarily sized image
   img = Image.open(Datei)
   # Create an image padded to the required size with
   # mode 'RGB'
   pad = Image.new('RGB', (       ((img.size[0] + 31) // 32) * 32,       ((img.size[1] + 15) // 16) * 16, ) )
   # Paste the original image into the padded one
   pad.paste(img, (0, 0))
   # Add the overlay with the padded image as the source,
   # but the original image's dimensions
  
   PiCam.annotate_text=""

   o = PiCam.add_overlay(pad.tostring(), size=img.size)
   # By default, the overlay is in layer 0, beneath the
   # preview (which defaults to layer 2). Here we make
   # the new overlay semi-transparent, then move it above
   # the preview
   o.alpha = 255
   o.layer = 3


   bild = PIL.Image.open(Datei)
   logo = PIL.Image.open('./logo.png')
   logo = logo.resize((170, 60), Image.ANTIALIAS)
   brightness = 0.8
   logo = PIL.ImageEnhance.Brightness(logo).enhance(brightness)
   pos = (10,680)
   bild = bild.transpose(Image.FLIP_LEFT_RIGHT) 
   bild.paste(logo, pos, mask=logo) 
   #mask=logo for logo tranzperance
   #bild.alpha_composite(logo,bild)
   bild.save(Datei)
   t = splitext(basename(Datei))[0]   
   
   
   
#   PiCam.stop_preview()
#   PiCam.preview_fullscreen= True
#   PiCam.start_preview()
#   print "Auf Flicker hochladen..."
#   response=flickr.upload(filename=Datei, title=t, is_public=1, format='etree')
#   photoID = response.find('photoid').text
#   photoURL = 'http://www.flickr.com/photos/%s/%s/' % (fuser, photoID)
#   print "Fertig"
   time.sleep(8)
   PiCam.remove_overlay(o)	


#flickr = FlickrAPI(key, secret)
#(token, frob) = flickr.get_token_part_one(perms='write')

#if not token:
#    raw_input("Bitte Anwendung im Browser autorisieren und dann ENTER druecken")
#flickr.get_token_part_two((token, frob))
pygame.init()
PiCam = picamera.PiCamera()
PiCam.preview_fullscreen= True
PiCam.resolution=(1024, 768)
PiCam.hflip=True
PiCam.preview_window = (1, 1 , 800, 600)
PiCam.annotate_text_size=160
#PiCam.annotate_background=picamera.Color('red')
PiCam.start_preview()

PiCam.iso=0
PiCam.video_stabilization=True
#PiCam.exposure_mode="auto"
PiCam.exposure_compensation=5
#PiCam.awb_mode="flash"
#myftp=ftplib.FTP("")
#myftp.login("","");
#dir="/selfi"
#myftp.cwd(dir)
IO.setwarnings(False)
IO.setmode(IO.BCM)
Taster = 24
IO.setup(Taster, IO.IN, pull_up_down=IO.PUD_DOWN)
finished = False

while not finished:
   #if(IO.input(Taster)):
   #  print "Startffe Fullscreen-Vorschau"
   #  PiCam.stop_preview() 
   #  PiCam.preview_fullscreen= True
   #  PiCam.start_preview()
   #  time.sleep(1)
     
     while not IO.input(Taster):
        pygame.event.get()
	pass
     time.sleep(0.05)
     if IO.input(Taster):
        shot()
     print "Stecker-selfi: push the button!"

