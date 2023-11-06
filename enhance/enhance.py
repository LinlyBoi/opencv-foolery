#!/usr/bin/env python3
import cv2
import matplotlib.pyplot as plt
import numpy as np

file_path = input('Enter Image file path: ')
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

#Threshold
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('image', img)
cv2.waitKey(0)
#norm
img = cv2.normalize(img, None, alpha=0.1, beta=1.2, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
cv2.imshow('image', img)
cv2.waitKey(0)
#Sharpening
kernel = np.array([
    [0, -1, 0,],
    [-1, 5, -1],
    [0, -1, 0]
])
img = cv2.filter2D(img, -1, kernel)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imwrite(file_path + '-enhanced.jpg', 255*img)
#sharp_file = 'sharp' + '-' + file_path + '.jpg'
#cv2.imwrite(sharp_file, img)
#cv2.imread(sharp_file, cv2.IMREAD_GRAYSCALE)

