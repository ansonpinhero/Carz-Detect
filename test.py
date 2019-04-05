import requests
import os
url = 'https://project-carz-ansonpinhero.c9users.io:8080/'
path_img="test.jpg"
with open(path_img, 'rb') as img:
  name_img= os.path.basename(path_img)
  files= {'file': (name_img,img,'multipart/form-data',{'Expires': '0'}) }
  with requests.Session() as s:
    r = s.post(url,files=files)
    print(r.text)