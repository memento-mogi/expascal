#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import subprocess
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import requests
import sys
import time

#GDrive
#gauth = GoogleAuth()
#gauth.LocalWebserverAuth()
#drive = GoogleDrive(gauth)

# LINE
TOKEN = "8wy1MX181uqvNa0W6vR7koRKFFRWgRU2TbiHU5ROMzG"
URL = "https://notify-api.line.me/api/notify"
HEADERS = {"Authorization" : "Bearer " + TOKEN}

MESSAGE =  "開始"
PAYLOAD = {"message" :  MESSAGE}
    
send = requests.post(URL, headers = HEADERS, params=PAYLOAD)
# log
start = time.time()
# time_l = [start]

DPI = 1000
size = 51
#divide = int(sys.argv[1])
divide = 4

tri_l = []
tri_axis = np.empty(size, dtype=np.int64)

# 軸の数列生成
np.put(tri_axis, [1,1], 1)
for column_axis in range (2, size):
    thenum = (tri_axis[column_axis-1]+tri_axis[column_axis-2]) % divide
    np.put(tri_axis, column_axis, thenum)

print(tri_axis)

tri_axis_l = tri_axis.tolist()
tri_l.append(tri_axis_l)

prevrow = tri_axis

# 中身生成
for row in range(1, size):
    tri_row = np.empty(size, dtype=np.int64)
    np.put(tri_row, 0, tri_axis[row])
     
    for column in range(1, size):
        thenum = (prevrow[column] + tri_row[column-1]) % divide
        np.put(tri_row, column, thenum)
 
    prevrow = tri_row

    tri_row_l = tri_row.tolist()
    tri_l.append(tri_row_l)
    

tri_show = np.array(tri_l)
tri_show = np.array(np.where(tri_show==0, 0, 255))

tri_show_up, tri_show_middle, tri_show_down = np.split(tri_show, 3)

tri_show_1, tri_show_2, tri_show_3 = np.split(tri_show_up, 3, 1)
tri_show_4, tri_show_5, tri_show_6 = np.split(tri_show_middle, 3, 1)
tri_show_7, tri_show_8, tri_show_9 = np.split(tri_show_down, 3, 1)

img_list = [tri_show_1, tri_show_2, tri_show_3, tri_show_4, tri_show_5, tri_show_6, tri_show_7, tri_show_8, tri_show_9]

#　可視化 
fig = plt.figure(dpi=DPI)
ax = fig.add_subplot(1,1,1)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

i=0
for img in img_list:
    i=i+1
    filename = str(divide)+"img"+str(i)+".png"
    ax.imshow(img, cmap="Blues")
    fig.savefig(filename)

    f = drive.CreateFile({'title': filename, 'mimeType': 'image/png'})
    f.SetContentFile('/home/maetaka-2020248/'+filename)
    f.Upload()

    subprocess.run("rm /home/maetaka-2020248/"+filename, shell=True)

end = time.time()
 
MESSAGE =  "Mod"+str(divide)+"の画像生成を"+str(int(end-start))+"秒で完了"
PAYLOAD = {"message" : MESSAGE}
 
send = requests.post(URL, headers = HEADERS, params=PAYLOAD)

