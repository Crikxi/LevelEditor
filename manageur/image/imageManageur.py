# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 10:27:41 2018

@author: Bastien
"""
import tkinter
import tkinter.filedialog
import tkinter.messagebox

from manageur.image import imageEvent
from manageur.rect import rectManageur
from manageur.image.gui import imageInfoGui

from functools import partial

canEditImage = True


def toggleEditImage(gvars):
    gvars.canEditImage = not gvars.canEditImage
    """
    if(canEditImage == True):
        index.menuEditerImage.entryconfig(1, label = "Désactiver la modification des images")
    else:
        index.menuEditerImage.entryconfig(1, label = "Activer la modification des images")
        """
    

        

def createImageFromImage(gvars, imageId, indexZ):
    if(not 0 <= indexZ < len(gvars.imagesListe)):
        tkinter.messagebox.showerror("Erreur", "L'index n'existe pas.")
        return
    gvars.imagesListe[indexZ].append({'type': 'image', 'imageId': imageId, 'coords':[0,0], 'tkId': None})
    displayImages(gvars)
    
def createImageFromTile(gvars, imageId, indexZ, tileId=0):
    if(not 0 <= indexZ < len(gvars.imagesListe)):
        tkinter.messagebox.showerror("Erreur", "L'index n'existe pas.")
        return
    gvars.imagesListe[indexZ].append({'type': 'tile', 'imageId': str(imageId) + '-' + str(tileId), 'coords':[0,0], 'tkId': None})
    displayImages(gvars)

def creerRectFromImage(gvars, image, rectType):
    coords = image["coords"]
    texture = gvars.texturesListe[image["imageId"]]
    rectManageur.creerPlateforme(gvars, rectType, [[coords[0], coords[1]], [coords[0] + texture["dimension"][0], coords[1] + texture["dimension"][1]]])
    
def removeImage(gvars, image, zindex):
    gvars.imagesListe[zindex].remove(image)
    displayImages(gvars)
    
def moveImage(gvars, image, zindex, dx, dy):
    image["coords"][0] += dx
    image["coords"][1] += dy
    displayImages(gvars)
    imageEvent.onButton3Press(gvars, image, zindex, None)
    
def setCoordsImage(gvars, image, zindex, x, y):
    if(x != None):
        image["coords"][0] = x
    if(y != None):
        image["coords"][1] = y
    displayImages(gvars)
    imageInfoGui.load(gvars, image, zindex)
    
def changeImageIndex(gvars, image, zindex, dIndex):
    if(zindex + dIndex < 0):
        return
        
    while(zindex + dIndex >= len(gvars.imagesListe)):
        gvars.imagesListe.append([])
    gvars.imagesListe[zindex + dIndex].append(image)
    gvars.imagesListe[zindex].remove(image)
    displayImages(gvars)
    imageInfoGui.load(gvars, image, zindex + dIndex)
  
  
def displayImages(gvars): #rectType = platforme / piege
    hideImages(gvars)
    for imageByIndex in gvars.imagesListe:
        for image in imageByIndex:
            if(image["type"] == "image"):
                image["tkId"] = gvars.canvas.create_image(image['coords'][0], image['coords'][1], image=gvars.texturesListe[image['imageId']]["tkImage"], anchor=tkinter.NW, tags="image")
            elif(image["type"] == "tile"):
                splitImageId = image['imageId'].split("-")
                image["tkId"] = gvars.canvas.create_image(image['coords'][0], image['coords'][1], image=gvars.texturesListe[int(splitImageId[0])]["tkImage"][int(splitImageId[1])], anchor=tkinter.NW, tags="image")
            else:
                print("ERRR")
                return
            gvars.canvas.tag_bind(image["tkId"], "<Button-1>", partial(imageEvent.onButton1Press, image))
            gvars.canvas.tag_bind(image["tkId"], "<Button-3>", partial(imageEvent.onButton3Press, gvars, image, gvars.imagesListe.index(imageByIndex)))
           
    
    
def hideImages(gvars):
    gvars.canvas.delete("image")