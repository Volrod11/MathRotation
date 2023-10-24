# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:22:00 2023

@author: garricastres
"""

# Une classe point. 
class Point : 
    'This is Coordonnees class'  
    
    # Une méthode utilisée pour créer l'objet (Contructor). 
    def __init__(self, x, y): 
         
        self.x = x 
        self.y = y 
        self.j = 1
     
    def getX(self):         
        return self.x 
     
    def getY(self):         
        return self.y 
         
    def setX(self,nouvX): 
        self.x = nouvX 
         
    def setY(self,nouvY): 
        self.y = nouvY 
         
    def afficherPoint(self): 
        print("[", self.x, ";", self.y, ";", self.j ,"]") 
         
