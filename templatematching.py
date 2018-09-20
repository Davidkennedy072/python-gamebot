# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 09:25:07 2018
@author: david

Template match function
Called in enemysearch.py
Returns coordinates (y,x) of template center and marked image
"""
import cv2
import numpy as np
import time

path = 'C:/Users/david/Desktop/Fun/pybot/testimages/'
testimage = cv2.imread(path+'rpgmotestimage1.PNG', cv2.IMREAD_COLOR)
testimage = cv2.cvtColor(testimage, cv2.COLOR_BGR2GRAY)

template = cv2.imread(path+'rpgmotestenemy1.PNG', cv2.IMREAD_COLOR)
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#testimage = cv2.imread(path+'testimage1.PNG', cv2.IMREAD_COLOR)
#template = cv2.imread('C:/Users/david/Desktop/Fun/pybot/testimages/testenemy1.PNG', cv2.IMREAD_COLOR)

def templatematch(testframe, template, threshold = 0.8):
    w = template.shape[0]
    h = template.shape[1]
    res = cv2.matchTemplate(testframe, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    
    coords = []
    for pt in zip(*loc[::-1]):
        coords.append((pt[1] + int(w/2), pt[0] + int(h/2))) # (y,x)
        cv2.rectangle(testframe, pt, (pt[0] + w, pt[1] + h), (0,0,255), thickness = 2)
#        testframe[pt[1] + int(w/2), pt[0] + int(h/2), :] = [0, 0, 255]
    return coords, testframe

if __name__ == '__main__':
    t0 = time.time()
    coords , resultimage = templatematch(testframe = testimage, template = template)
    cv2.imshow('result', resultimage)
    t1 = time.time()
    print(t1-t0)