#!/usr/bin/env python3
import cv2
import matplotlib.pyplot as plt

#reading image
img = cv2.imread('img3.jpg')
print("Original Image")
cv2.imshow('image',img)
cv2.waitKey(0)

#Defining boundaries
print(img.shape)
left = 350
top = 50
right = img.shape[1] - 100
bottom = img.shape[0] - 200

#cropping image
cropped = img[top:bottom, left:right]
print("Cropped image")
cv2.imshow('image',cropped)
cv2.waitKey(0)
