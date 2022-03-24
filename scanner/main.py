#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created by                               extra usages \
@author: ababil islam udoy
image decoder.
"""
import cv2
import sys
import numpy as np
from PIL import Image, ImageOps
import imageio
import glob
import os
import img_comp, data_extractor, binary_to_string
import time
import tracemalloc

start_time = time.time()
tracemalloc.start()
data=[]
"""image reading 

use image(4_stage_QR image) that need to read/scan.

specially use absulate file location/path to read image properly.
 
using relative path may not work with external file!"""

# img = Image.open(4_state_QR.jpeg)           #note: this relative path can be find.

path = "/home/ab/Documents/GitHub/4_states-QR-code-encoder/QR/4_state_QR.jpeg"

img = Image.open(path)
# converting color image to gray
img = ImageOps.grayscale(img)
# convert gray inage to numpy array
img_array_1 = np.array(img)
# finding shape
s = np.shape(img_array_1)
v = s[0]
# print(v)
# removing border white pixle
# top and bottom white border
da = np.delete(img_array_1, np.s_[:50:1], 0)
da = np.delete(da, np.s_[:-51:-1], 0)
# removing left and right birder pixel
da = np.delete(da, np.s_[:50:1], 1)
da = np.delete(da, np.s_[:-51:-1], 1)
# generating border less imagepip install opencv2-python
final_borderless_image = Image.fromarray(da)
# display border less image
# final_borderless_image.show()
# save bodderless image
imageio.imwrite('4_boder_less_qr.jpeg', final_borderless_image)

path = os.path.dirname((os.path.abspath(__file__)))
# path= os.path.join(path,)
# print(path)
# image patcher
img = cv2.imread(os.path.join(path,"4_boder_less_qr.jpeg"))
img_path = os.path.join(os.path.dirname(path),"raw")
# print(img_path)                            #img_path=/home/ab/Desktop/QRDecoder/raw
img_00 = cv2.imread(os.path.join(img_path,"img1.jpg"))      #dynamic path finding
img_01 = cv2.imread(os.path.join(img_path,"img2.jpg"))
img_10 = cv2.imread(os.path.join(img_path,"img3.png"))
img_11 = cv2.imread(os.path.join(img_path,"img4.png"))

# cv2.imshow("image00",img_00)
# cv2.imshow("image01",img_01)
# cv2.imshow("image10",img_10)
# cv2.imshow("image11",img_11)
# img = final_borderless_image
image_copy = img.copy()
# image height in int from image
imgheight = img.shape[0]
# image width in int from image
imgwidth = img.shape[1]

M = 50
N = 50
x1 = 0
y1 = 0
# i = 0
for y in range(0, imgheight, M):
    # j = 0
    ls=[]
    for x in range(0, imgwidth, N):
        y1 = y + M
        x1 = x + N
        # Crop into patches of size MxN
        tiles = image_copy[y:y + M, x:x + N]

        # Save each patch into file directory
        path = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
        path= os.path.join(path,"image/patch")
        
        cv2.imwrite(path + 'img' + str(x) + '_' + str(y) + '.jpg', tiles)

        
        # cv2.imwrite('/home/ab/Desktop/QRDecoder/image/patch/' + 'img' + str(x) + '_' + str(y) + '.jpg', tiles)
        # cv2.imshow("img"+ str(x) + '_' + str(y) + '.jpg', tiles)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        ab=img_comp.image_compare(path + 'img' + str(x) + '_' + str(y) + '.jpg')
        # print(ab)
        ls.append(ab)
        cv2.rectangle(img, (x, y), (x1, y1), (0, 255, 0), 1)
    data.append(ls)
# print(path)
# cv2.imshow("Patched Image",img)

cv2.imwrite("patched.jpg", img)

# cv2.waitKey()
#
# cv2.destroyAllWindows()
# matrix before any data extracted 
# print(data,sep=" ",end="\n")

# print(np.shape(data))

str_steam = data_extractor.extractor(data = data)
# print(str_steam)


def data_spliter(data):
    """this module split data in to 8 digit by 8 digit data block
    like : if i have a binary data of 16 digit that data going to split in to 8 group or list index.
    example: let assume binary_data= '0001001000010011'
    then this data i'm going to split in to 8 bit by 8 bit
    out put should be like this ="00010010","00010011"
    and finaly i returned this output of data that going to generate our final qr matrix value.
    """
    data = data
    # print(fr"data before splitting: {data}")
    n = 8
    splitted_data = [data[i:i + n] for i in range(0, len(data), n)]
    # print(len(splitted_data))
    # print(splitted_data)
    return splitted_data

try:
    splitted_Data = data_spliter(data=str_steam)
except Exception as exception:
    
    print("can\'t decode the image")
    print("probabily image is not valid. Try with a valid image")
    sys.exit()
# print(splitted_Data)
# print(type(splitted_Data))
data_list=[]
# poping out which type of encode is used
encode_type = splitted_Data.pop(0)
# poping out how may character is used in this qr code
data_length = splitted_Data.pop(0)

# int(encode_type, 2) is the binary to decimal conversion.
# print("Encode Mode is : ",int(encode_type, 2))
# print("Number of character in the QR Code is : ",int(data_length, 2))

# pushing string part in to datalist.
for i in splitted_Data:
    if i=="00000000":
        break
    else:
        data_list.append(i)
# print(data_list)

# converting binary to string stream
string_stream = binary_to_string.str_converter(data=data_list)
# print(" ")
print("Output data:")
print(string_stream)
# print("")
print("output data length :",len(string_stream))

"""time counter to count runtime of a program"""
execution_time = time.time() - start_time

"""comment out for future use."""
# t=time.strftime("%S",time.gmtime(execution_time))
# if int(t)>0:
#     print('Execution Time Taken:', time.strftime("%HHours:%MMinutes:%SSeconds",time.gmtime(execution_time)))
# else:
#     print("Execution Time {:.2f} Milliseconds".format(execution_time*1000))
# comment below 2 line if upper section of code is used.
# print('Execution Time Taken:', time.strftime("%H Hours:%M Minutes:%S Seconds",time.gmtime(execution_time)))
print("Execution Time {:.2f} Milliseconds".format(execution_time*1000))
# print('Execution Time Taken:', time.strftime("%H H:%M M:%S S",time.gmtime(execution_time)))

""" memory cost """
current, Maximum = tracemalloc.get_traced_memory()
print(f"Maximum usage of memory is: {Maximum / 10**6} MB")
tracemalloc.stop()