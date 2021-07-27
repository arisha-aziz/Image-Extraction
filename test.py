from imutils.object_detection import non_max_suppression
import pytesseract
from PIL import Image, ImageEnhance
import cv2
import numpy as np

image = cv2.imread('3.png')
img = image.copy()
cv2.imshow('image',img)
cv2.waitKey()
print("Original Image: ")
print()
text = pytesseract.image_to_string(img) 
text = text.split('\n')
print(text)

print()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',img)
cv2.waitKey()
print("Gray Image: ")
print()
text = pytesseract.image_to_string(img) 
text = text.split('\n')
print(text)

print()
img = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('img',img)
cv2.waitKey()
print("Blur Image: ")
print()
text = pytesseract.image_to_string(img) 
text = text.split('\n')
print(text)
