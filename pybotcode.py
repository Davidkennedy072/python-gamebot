# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 07:43:57 2018
@author: David
Grab screenshot and return
optical argument for bbox with default as full screen

Task:

    1) Allow users to define an enemy 
    2) Search for define enemy on screenshot to get enemy coordinates
    3) Excute attacks 

Extra bits:
    1) add click option on maplewindow function 
"""
from PIL import ImageGrab
import os
import time
import pyautogui
import numpy as np
import cv2

from quickGrab import screenGrab

screencoord = (500, 500, 1000, 1000)

#last_time = time.time()
while True:
    printscreen = np.array(screenGrab(bbox = screencoord)) # RGB
    cv2.imshow('window', cv2.cvtColor(printscreen, cv2.COLOR_RGB2BGR))
#    print('Loop took {} seconds'.format(time.time() - last_time))
#    last_time = time.time()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break