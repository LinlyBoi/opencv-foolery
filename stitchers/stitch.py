#!/usr/bin/env python3
import cv2

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')
img4 = cv2.imread('4.jpg')

img_list = [img1, img2, img3, img4]
stitcher = cv2.Stitcher_create()
result, stitched_img = stitcher.stitch(img_list)

if result == cv2.STITCHER_OK:
    cv2.imshow('image', stitched_img)
    cv2.imwrite('stitched2.jpg', stitched_img)
    cv2.waitKey(0)
