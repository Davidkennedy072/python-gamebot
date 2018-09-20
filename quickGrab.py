# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 07:43:57 2018
@author: David
Grab screenshot and return
optical argument for bbox with default as full screen
"""
from PIL import ImageGrab
import os
import time
import pyautogui

maxx, maxy = pyautogui.size()

def screenGrab(bbox = (0, 0, maxx, maxy)): # bbox = (X1, Y1, X2, Y2)
    im = ImageGrab.grab(bbox)
    return im

if __name__ == '__main__':
    zi = screenGrab()
