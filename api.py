import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json
import requests
import vlc
import time
import io
from mutagen.mp3 import MP3
from urllib.request import urlretrieve


listVoice = {
    "mienbac_nu" : "female",
    "mienbac_nam" : "male", 
    "mientrung" : "ngoclam", 
    "miennam" : "hatieumai"
}
try:
    with io.open("input.json", 'r', encoding = 'utf-8') as f:
        data = json.load(f)
except IOError as x:
    print(x)
    exit()
    

if (('msg' in data) == 0):
    print("Mo message!")
    exit()

if (len(data['msg']) < 1):
    print("No message!")
    exit()

if (('voice' in data) == 0) :
    print("No voice")
    exit()

if ((data['voice'] in listVoice) == 0):
    print("Unknown voice!")
    exit()

print(data)
    
url = 'http://api.openfpt.vn/text2speech/v4' 
head = {'api_key' : '206cbc8a3ca44faeb293e6696a232c1a', 'voice' : listVoice[data['voice']]} 
#dat = 'thứ 6 ngày 13'

r = requests.post(url, headers = head, data = data['msg'].encode('utf-8'))

if (r.status_code != 200) :
    print('ERROR: fall to connect')
    exit()
str = r.text
tmp = str.split("\"")
url = tmp[3] 
try:
    filename, headers = urlretrieve(url)
except IOError as e:
    print('ERROR:', e)
    exit()
except Exception as e:
    print('ERROR: ', e) 
    exit()

audio = MP3(filename)
t = audio.info.length
p = vlc.MediaPlayer(filename)
p.play()
if ('image' in data) :
    img=mpimg.imread('a.jpg')
    imgplot = plt.imshow(img)
    plt.show()
    plt.close()

time.sleep(t + 1.5)

exit()

