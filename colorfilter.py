# -*- coding: utf-8 -*-
'''
Created on Sun Jul  1 12:10:08 2018
@author: david

color filtering for use in enemysearch.py
Converts color to from BGR to HSV
'''
import cv2
import numpy as np
import time
from enemysearch import enemysearch

#For testimage1: Color filter = blue
#after color filter template match 
path = 'C:/Users/david/Desktop/Fun/pybot/testimages/'
testimage = cv2.imread(path+'testimage1.PNG', cv2.IMREAD_COLOR)
template = cv2.imread('C:/Users/david/Desktop/Fun/pybot/testimages/testenemy1.PNG', cv2.IMREAD_COLOR)

'''
Color filtering
'''
hsv = cv2.cvtColor(testimage, cv2.COLOR_BGR2HSV)
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])
mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(testimage, testimage, mask = mask)
cv2.imshow('resultcolor', result)

if __name__ == '__main__':
    t0 = time.time()
    coords, resultimage = enemysearch(testimage, [template1, template2], checkflip = False)   
    cv2.imshow('result', resultimage)
    t1 = time.time()
    print(t1-t0)