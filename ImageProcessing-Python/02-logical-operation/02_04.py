# -*- coding:utf-8 -*-
import cv2
import numpy

#读取图片
img = cv2.imread("./images/Lena.png")
print(type(img))

#Numpy读取像素
print(img.item(78, 100, 0))
print(img.item(78, 100, 1))
print(img.item(78, 100, 2))

#Numpy修改像素
img.itemset((78, 100, 0), 100)
img.itemset((78, 100, 1), 100)
img.itemset((78, 100, 2), 100)
print(img.item(78, 100, 0))
print(img.item(78, 100, 1))
print(img.item(78, 100, 2))
