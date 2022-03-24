#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 22:52:29 2022

@author: ab
"""

import cv2

import qrcode
import time
import tracemalloc

start_time = time.time()
tracemalloc.start()
d = cv2.QRCodeDetector()
val,points,stqr=d.detectAndDecode(cv2.imread("2state.jpeg"))
print(val)
# For time CHeck
execution_time = time.time() - start_time
"""comment out for future use."""
t=time.strftime("%S",time.gmtime(execution_time))
if int(t)>0:
    print('Execution Time Taken:', time.strftime("%HHours:%MMinutes:%SSeconds",time.gmtime(execution_time)))
    pass
else:
    print("Execution Time {:.2f} Milliseconds".format(execution_time*1000))
    
print("Execution Time {:.2f} Milliseconds".format(execution_time*1000))
# For Memory CHeck
current, peak = tracemalloc.get_traced_memory()
print(f" Peak memory usage was {peak / 10**6}")
tracemalloc.stop()