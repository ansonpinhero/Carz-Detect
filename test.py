import requests
import os
from firebase_admin import db
import firebase_admin
from firebase_admin import credentials
import image_slicer
import time 
import image_slicer
from PIL import Image
import picamera
cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://spas-8ee35.firebaseio.com/'
})

url = 'https://carz-x.herokuapp.com/'
images=['cars_01_01.png_01_01.png.jpg','cars_01_01.png_01_02.png.jpg','cars_01_02.png_01_01.png.jpg','cars_01_02.png_01_02.png.jpg']
path_img="test/car1.jpg"

def start(path_img,i):
  with open(path_img, 'rb') as img:
    name_img= os.path.basename(path_img)
    files= {'file': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
    with requests.Session() as s:
      r = s.post(url,files=files)
      print(r.text)
      if(r.text=="True"):
	  root = db.reference().update({'slot{}'.format(i) : "\"1\""})
      else:
	  root = db.reference().update({'slot{}'.format(i) : "\"0\""})

def split():
    tiles = image_slicer.slice('cars.jpg', 2, save=True)

    new_images=['cars_01_01.png','cars_01_02.png']

    print("hello")
    for ni in new_images:
        im=Image.open(ni)
        rgb_im=im.convert('RGB')
        rgb_im.save(ni+'.jpg')

    new_images=['cars_01_01.png.jpg','cars_01_02.png.jpg']
    i=1
    for ni in new_images:
        i=1
        print('heo')
        tiles = image_slicer.slice(ni, 2, save=True)
        k=[ni[0:14]+"_01_0{}.png".format(i),ni[0:14]+"_01_0{}.png".format(i+1)]
    
        for nil in k :
        
            im=Image.open(nil)
            rgb_im=im.convert('RGB')
            rgb_im.save(nil+".jpg")
        i=i+1
    test=os.listdir(os.getcwd())
    for i in new_images:
        os.remove(i)
    for item in test:
        if item.endswith(".png"):
            os.remove(item)

def capture():
  with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    
    time.sleep(2)
    camera.capture('cars.jpg')


while True:
  capture()
  i=1
  split()
  for image in images:
    start(image,i)
    i=i+1
  time.sleep(3)





