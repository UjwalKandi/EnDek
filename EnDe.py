import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os 
from PIL import Image
from PIL.ExifTags import TAGS

import re

#section 1
def ImgMeta(img_file):
    '''to extract image metadata with Python'''
    # img_file = '../input/img-sample/4549539197_11275cd1a7_o.jpg'
    image = Image.open(img_file)
    # img.show()
    exif = {}

    for tag, value in image._getexif().items():
        if tag in TAGS:
            exif[TAGS[tag]] = value

    if 'GPSInfo' in exif:
        geo_coordinate = '{0} {1} {2:.2f} {3}, {4} {5} {6:.2f} {7}'.format(
            exif['GPSInfo'][2][0][0],
            exif['GPSInfo'][2][1][0],
            exif['GPSInfo'][2][2][0] / exif['GPSInfo'][2][2][1],
            exif['GPSInfo'][1],
            exif['GPSInfo'][4][0][0],
            exif['GPSInfo'][4][1][0],
            exif['GPSInfo'][4][2][0] / exif['GPSInfo'][4][2][1],
            exif['GPSInfo'][3],)
        return geo_coordinate

#     return exif
#     return(exif['FocalPlaneYResolution'])
    return exif['Model'],exif['DateTime']


img_file = input()
print(ImgMeta(img_file))



#section 2 
def KeyGenerator(plain_text, key):
	
	# returns plain text by repeatedly xoring it with key
	pt = plain_text
	len_key = len(key)
	encoded = []
	
	for i in range(0, len(pt)):
		encoded.append(pt[i] ^ key[i % len_key])
	return bytes(encoded)
	# Driver Code
def main():
# 	plain_text = b'Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal'
# 	key = b'ICE'
	plain_text = bytes(input('text:'), "utf8")
	key = bytes(input('key:'), "utf8")
    
	print("Plain text: ", plain_text)
	print("Encrypted as: ", KeyGenerator(plain_text, key).hex())

if __name__ == '__main__':
		main()

#section 3
def Encrypt(data, key):
	# try block to handle exception
	try:
		# take path of image as a input
		path = input(r'Enter path of Image : ')
		
		# taking encryption key as input
		key = int(input('Enter Key for encryption of Image : '))
		
		# print path of image file and encryption key that
		# we are using
		print('The path of file : ', path)
		print('Key for encryption : ', key)
		
		# open file for reading purpose
		fin = open(path, 'rb')
		
		# storing image data in variable "image"
		image = fin.read()
		fin.close()
		
		# converting image into byte array to
		# perform encryption easily on numeric data
		image = bytearray(image)

		# performing XOR operation on each value of bytearray
		for index, values in enumerate(image):
			image[index] = values ^ key

		# opening file for writting purpose
		fin = open(path, 'wb')
		
		# writing encrypted data in image
		fin.write(image)
		fin.close()
		print('Encryption Done...')
	except Exception:
		print('Error caught : ', Exception.__name__)

#section 4
def KeyExtractor(key1, key2):

#section 5
def Decrypt(data, key):
	# try block to handle the exception
	try:
		# take path of image as a input
		path = input(r'Enter path of Image : ')
		
		# taking decryption key as input
		key = int(input('Enter Key for encryption of Image : '))
		
		# print path of image file and decryption key that we are using
		print('The path of file : ', path)
		print('Note : Encryption key and Decryption key must be same.')
		print('Key for Decryption : ', key)
		
		# open file for reading purpose
		fin = open(path, 'rb')
		
		# storing image data in variable "image"
		image = fin.read()
		fin.close()
		
		# converting image into byte array to perform decryption easily on numeric data
		image = bytearray(image)

		# performing XOR operation on each value of bytearray
		for index, values in enumerate(image):
			image[index] = values ^ key

		# opening file for writting purpose
		fin = open(path, 'wb')
		
		# writing decryption data in image
		fin.write(image)
		fin.close()
		print('Decryption Done...')
	except Exception:
		print('Error caught : ', Exception.__name__)