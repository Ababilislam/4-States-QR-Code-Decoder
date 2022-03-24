#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:42:07 2022

@author: ab
"""
import qrcode
import time
import tracemalloc

start_time = time.time()
tracemalloc.start()


img=qrcode.make("528cef87d0bfb947548ab94679d1e5765f19089a")
img.save("2state.jpeg")
# For time CHeck
execution_time = time.time() - start_time
"""comment out for future use."""
t=time.strftime("%S",time.gmtime(execution_time))
if int(t)>0:
    print('Execution Time Taken:', time.strftime("%HHours:%MMinutes:%SSeconds",time.gmtime(execution_time)))
else:
    print("Execution Time {:.2f} Milliseconds".format(execution_time*1000))
# For Memory CHeck
current, peak = tracemalloc.get_traced_memory()
print(f" Peak memory usage was {peak / 10**6}")
tracemalloc.stop()