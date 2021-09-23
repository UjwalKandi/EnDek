import numpy as np
import pandas as pd

import os 
from PIL import Image
from PIL.ExifTags import TAGS

import re

def ImgMeta(img_file, localStorage):
    '''to extract image metadata with Python'''
    image = Image.open(img_file)
    exif = {}

    for tag, value in image._getexif().items():
        if tag in TAGS:
            exif[TAGS[tag]] = value
    
    print(exif)

    date_time = exif['DateTime']                # extracting DateTime from Metadata
    line = re.sub('[!@#$:]', '', date_time)     # removing : from DateTime
    plain_text = bytes(line, "utf8")            # public key
    key = bytes(input('key: '), "utf8")         # private key


localStorage = {'4549539197_11275cd1a7_o.jpg': 151}    
img_file = input('file path: ')
ImgMeta(img_file, localStorage)
