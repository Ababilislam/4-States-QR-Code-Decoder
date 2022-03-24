#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 20:37:42 2022

@author: ab
"""
"""this function convert binary data to unicode character 
 in the list we pass data this data.  then we convert data into byte and 
 this byte convert using decode fucntion and return a stream of character
 and finaly we retun data_stream to the caller
"""
def str_converter(data):
    character_stream = bytes([int(x,2) for x in data]).decode('utf-8')
    return character_stream

