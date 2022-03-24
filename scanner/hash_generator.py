#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:30:35 2022

@author: ab
this is for sha-1 hash generator.
"""

import hashlib
 
# initialize a string
str = "ab"
 
# encode the string
encoded_str = str.encode()

# create a sha1 hash object initialized with the encoded string
hash_obj = hashlib.sha224(encoded_str)

 
# create a sha1 hash object initialized with the encoded string
# hash_obj = hashlib.sha256(encoded_str)
# create a sha1 hash object initialized with the encoded string
# hash_obj = hashlib.sha1(encoded_str)
 
# convert the hash object to a hexadecimal value
hexa_value = hash_obj.hexdigest()
 
# print
print("\n", hexa_value, "\n")