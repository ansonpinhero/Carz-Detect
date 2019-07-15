import requests
import os
url = 'https://carz-x.herokuapp.com/'
path_img="test/car1.jpg"
def start(path_img):
  with open(path_img, 'rb') as img:
    name_img= os.path.basename(path_img)
    files= {'file': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
    with requests.Session() as s:
      r = s.post(url,files=files)
      print(r.text)
      if(r.text=="True"):
	  printf("Vehicle Found")
      else:
	  printf("No Vehicle Found")

start(path_img)





