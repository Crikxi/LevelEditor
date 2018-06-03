# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 23:15:29 2018

@author: Bastien
"""

from manageur.rect import rectEvent
from functools import partial

   
def setMiddleClicMode(gvars, mode):
    gvars.currentMode = mode

def getListFromType(gvars, rectType):
    if(rectType == "plateforme"):
        return gvars.plateformesListe    
    elif(rectType == "topPlateforme"):
        return gvars.topPlateformesListe
    elif(rectType == "piege"):
        return gvars.piegesListe
    
    else:
        return None
    
def getColorFromType(rectType):
    if(rectType == "plateforme"):
        return "green"    
    if(rectType == "topPlateforme"):
        return "blue"
    elif(rectType == "piege"):
        return "red"
    else:
        return "white"

def displayRect(gvars, rectType="plateforme", color=None): #rectType = platforme / piege
    hideRect(gvars, rectType)
    
    liste = getListFromType(gvars, rectType)
    if(liste == None): 
        return
    if(color == None):
        color = getColorFromType(rectType)
        
    for rect in liste:
        rect["tkId"] = gvars.canvas.create_rectangle(rect["coords"][0][0], rect["coords"][0][1], rect["coords"][1][0], rect["coords"][1][1], fill=color, tags=rectType)
        gvars.canvas.tag_bind(rect["tkId"], "<Button-1>", partial(rectEvent.onButton1Press, rect))
        gvars.canvas.tag_bind(rect["tkId"], "<Button-3>", partial(rectEvent.onButton3Press, gvars, rect, rectType))
    
def hideRect(gvars, rectType="plateforme"):
    gvars.canvas.delete(rectType)
    
    

def creerPlateforme(gvars, rectType, coords):
        liste = getListFromType(gvars, rectType)
        if(liste == None): 
            return
        liste.append({'tkId': None, 'coords': coords})
        displayRect(gvars, rectType)