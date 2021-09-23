import numpy as np
import pandas as pd

import os 
from PIL import Image
from PIL.ExifTags import TAGS

import re

def ImgMeta(img_file, localStorage):
    '''to extract image metadata with Python'''
    image = Image.open(img_file)
    # img.show()
    exif = {}

    for tag, value in image._getexif().items():
        if tag in TAGS:
            exif[TAGS[tag]] = value

    # print(exif)

    date_time = exif['DateTime']                # extracting DateTime from Metadata
    line = re.sub('[!@#$:]', '', date_time)     # removing : from DateTime
    plain_text = bytes(line, "utf8")            # public key
    key = bytes(input('key: '), "utf8")         # private key

    # returns plain text by repeatedly xoring it with key
    pt = plain_text
    len_key = len(key)
    encoded = []

    for i in range(0, len(pt)):
        encoded.append(pt[i] ^ key[i % len_key])
        en = bytes(encoded)
    # print(int(en.hex(), 16))                  
    hash_key = int(en.hex(),16)                    # hash key
    strr = str(hash_key)
    list_of_number = list(map(int, strr.strip()))
    compressed_key = sum(list_of_number)           # compressed version of hash key
    # print(compressed_key) 
    
# encryption section
    # open file for reading purpose
    fin = open(img_file, 'rb')

    # storing image data in variable "image"
    image1 = fin.read()
    fin.close()

    # converting image into byte array to
    # perform encryption easily on numeric data
    image1 = bytearray(image1)

    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image1):
        image1[index] = values ^ compressed_key

    # opening file for writting purpose
    fin = open(img_file, 'wb')

    # writing encrypted data in image
    fin.write(image1)
    fin.close()
    print('Encryption Done...')

    # extract file name to be used a key in the dictionary: localStorage
    file_name = img_file.split("\\")[-1]
    localStorage[file_name] = compressed_key


# decryption section
def Decrypt(img_file, localStorage):
    
    # extract file name to be used a key in the dictionary: localStorage
    file_name = img_file.split("\\")[-1]

    # comparing public keys and extracting the proper compressed key(private key)
    for key, value in localStorage.items():     
        if key == file_name:                     # search for a similar key to extract the value(compressed_key)
            compressed_key = value
        else:
            print('Key Not Found')
    
    # open file for reading purpose
    fin = open(img_file, 'rb')

    # storing image data in variable "image"
    image = fin.read()
    fin.close()

    # converting image into byte array to perform decryption easily on numeric data
    image = bytearray(image)

    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ compressed_key

    # opening file for writting purpose
    fin = open(img_file, 'wb')

    # writing decryption data in image 
    fin.write(image)
    fin.close()
    print('Decryption Done...')


localStorage = {'25807802118_c1251aab3a_o.jpg': 151}    
img_file = input('file path: ')
ImgMeta(img_file, localStorage)
Decrypt(img_file, localStorage)
# print(localStorage['4549539197_11275cd1a7_o.jpg'])
