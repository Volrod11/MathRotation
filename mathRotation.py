# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from turtle import *
from math import *


def multiplierMatrice(m1, m2):
    nvMatrice = m1
    
    for i in range(len(m1)):
        for j in range(len(m2)):
            nvMatrice[i][j] = m1[i][0]*m2[0][j] + m1[i][1]*m2[1][j] + m1[i][2]*m2[2][j]
            
    return nvMatrice
    
    

m1 = [[1,0,2],[0,1,3],[0,0,1]]
m2 = [[-1,0,0],[0,1,0],[0,0,1]]
print(multiplierMatrice(m1,m2))

def rotationCarre(rotation):
    carre = [[3,2,1],
             [3,3,1],
             [4,2,1],
             [4,3,1]]
    
    nvCarre = carre
    
    cos = cos(rotation)
    sin = sin(rotation)

    matriceRotation = [[cos, - sin, 0],
                       [sin, cos, 0],
                       [0, 0, 1]]
    
    
    
    for point in carre:
        nvcarre = multiplierMatrice()b 
    
    

    
