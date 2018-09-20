# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 21:04:26 2018
@author: david
Task:
    1) Set up template matching/ image recognition of enemies
    
    2) Allow users to define an enemy (screenshot, save image, use as template)
    3) Identies enemies using different computer vision tech
    
    4) Color identification ( if enemy is unique color get color thresholding)
    5) template matching 
    6) Motion detection 
    
    6) build custom  high\low\band-pass filtering ( 2D fourier transform,
    remove frequency elements)
    7) image blurring and smoothing. add gray scale options.
Build functions than move them to seperate files

Additional notes:
Return enemy coordinates as distance from character if prixomityorder = True
add checkflipped option. FLips template
"""
import os
import cv2
import numpy as np
import time

from templatematching import templatematch

testimage = cv2.imread('C:/Users/david/Desktop/Fun/pybot/testimages/rpgmotestimage1.PNG', cv2.IMREAD_COLOR)
template1 = cv2.imread('C:/Users/david/Desktop/Fun/pybot/testimages/rpgmotestenemy1.PNG', cv2.IMREAD_COLOR)
template2 = cv2.imread('C:/Users/david/Desktop/Fun/pybot/testimages/rpgmotestenemy2.PNG',cv2.IMREAD_COLOR)

def enemysearch(screenshot, enemies, checkflip = False):
    '''
    enemies is a list with templates of different enemies as elements
    checkflip is an option to check flipped template of each enemy
    '''
    allcoords = []
    if checkflip == True:
        for enemy in enemies:
            enemyflip = np.fliplr(enemy)
            enemies.append(enemyflip)
    for enemy in enemies:
        coords, resultimage = templatematch(testframe = screenshot, template = enemy, threshold = 0.5)
        allcoords.append(coords)
    return allcoords, resultimage

if __name__ == '__main__':
    t0 = time.time()
    coords, resultimage = enemysearch(testimage, [template1, template2], checkflip = False)   
    cv2.imshow('result', resultimage)
    t1 = time.time()
    print(t1-t0)