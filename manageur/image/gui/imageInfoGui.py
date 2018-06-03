# -*- coding: utf-8 -*-

import globalVars
import tkinter
from manageur.image import imageManageur
from manageur.image import textureManageur


selectionedImageIndexWithRightClick = 0
selectionedImageWithRightClick = None
editImageWindow = None
entryDeplacerImage = None
entryRedimensionnerTexture = None


def load(gvars, image, zindex):
    global selectionedImageRightClick,selectionedImageIndexWithRightClick, editImageWindow, entryDeplacerImage, entryRedimensionnerTexture
    selectionedImageRightClick = image
    selectionedImageIndexWithRightClick = zindex
    
    #Bof mais ça fonctionne
    
    try:        
        editImageWindow.focus_force()
        if(entryRedimensionnerTexture != None):
            redimensionnerTextureStringOld = entryRedimensionnerTexture.get()
        else:
            redimensionnerTextureStringOld = ""
        
        if(entryDeplacerImage != None):
            deplacerImageStringOld = entryDeplacerImage.get()
        else:
            deplacerImageStringOld = ""
            
        for widget in editImageWindow.pack_slaves():
            widget.destroy()
        
    except:
        editImageWindow = tkinter.Toplevel()
        deplacerImageStringOld = ""
        redimensionnerTextureStringOld = ""
        
    
        
    labelImage = tkinter.LabelFrame(editImageWindow, text="Option d'image")
    labelImage.pack()
    tkinter.Button(labelImage, text="Enlever Image", command=lambda: imageManageur.removeImage(gvars, image, zindex)).pack()
    tkinter.Button(labelImage, text="Creer plateforme", command=lambda: imageManageur.creerRectFromImage(gvars, image, "plateforme")).pack()
    tkinter.Button(labelImage, text="Creer piege", command=lambda: imageManageur.creerRectFromImage(gvars, image,"piege")).pack()
    tkinter.Button(labelImage, text="Creer platformes traversables", command=lambda: imageManageur.creerRectFromImage(gvars, image,"topPlateforme")).pack()
    
    labelDeplacerImage = tkinter.LabelFrame(labelImage, text="Bouger la texture")
    labelDeplacerImage.pack()
    
    tkinter.Label(labelDeplacerImage, text="X: " + str(image["coords"][0])).pack()
    tkinter.Label(labelDeplacerImage, text="Y: " + str(image["coords"][1])).pack()
    entryDeplacerImage = tkinter.Entry(labelDeplacerImage)
    entryDeplacerImage.insert(0, deplacerImageStringOld)
    entryDeplacerImage.pack()
    tkinter.Button(labelDeplacerImage, text="+X", command=lambda: imageManageur.moveImage(gvars, image, zindex, int(entryDeplacerImage.get()), 0)).pack()
    tkinter.Button(labelDeplacerImage, text="+Y", command=lambda: imageManageur.moveImage(gvars, image, zindex, 0, int(entryDeplacerImage.get()))).pack()
    tkinter.Button(labelDeplacerImage, text="Set X", command=lambda: imageManageur.setCoordsImage(gvars, image, zindex, int(entryDeplacerImage.get()), None)).pack()
    tkinter.Button(labelDeplacerImage, text="Set Y", command=lambda: imageManageur.setCoordsImage(gvars, image, zindex, None, int(entryDeplacerImage.get()))).pack()
    
    tkinter.Label(labelDeplacerImage, text="zIndex: " + str(zindex)).pack()
    tkinter.Button(labelDeplacerImage, text="index +1", command=lambda: imageManageur.changeImageIndex(gvars, image, zindex, 1)).pack()
    tkinter.Button(labelDeplacerImage, text="index -1", command=lambda: imageManageur.changeImageIndex(gvars, image, zindex, -1)).pack()
    
    
    labelTexture = tkinter.LabelFrame(editImageWindow, text="Option de texture")
    labelTexture.pack()
    
    if(image["type"] == "image"):
        texture = gvars.texturesListe[image["imageId"]]   
        tileId = None
        dimension = texture["dimension"]
    if(image["type"] == "tile"):
        splitId = image["imageId"].split("-")
        imageId = int(splitId[0])
        tileId = int(splitId[1])
        texture = gvars.texturesListe[imageId]
        dimension = texture["dimension"][tileId]
    tkinter.Label(labelTexture, text="Nom de la texture: " + texture["name"]).pack()
    
    if(image["type"] == "tile"):
        tkinter.Label(labelTexture, text="Id du tile: " + str(tileId)).pack()
    tkinter.Label(labelTexture, text="Width: " + str(dimension[0])).pack()
    tkinter.Label(labelTexture, text="Height: " + str(dimension[1])).pack()
    
    labelRedimensionnerTexture = tkinter.LabelFrame(labelTexture, text="Rediemnsionner la texture")
    labelRedimensionnerTexture.pack()
    
   
    entryRedimensionnerTexture = tkinter.Entry(labelRedimensionnerTexture)
    entryRedimensionnerTexture.insert(0, redimensionnerTextureStringOld)
    entryRedimensionnerTexture.pack()
    tkinter.Button(labelRedimensionnerTexture, text="+Width", command= lambda: textureManageur.resizeTexture(gvars, image, zindex, int(entryRedimensionnerTexture.get()), 0)).pack()
    tkinter.Button(labelRedimensionnerTexture, text="+Height", command= lambda: textureManageur.resizeTexture(gvars, image, zindex, 0, int(entryRedimensionnerTexture.get()))).pack()
    
    tkinter.Button(labelRedimensionnerTexture, text="Set Width", command= lambda: textureManageur.setTextureDim(gvars, image, zindex, int(entryRedimensionnerTexture.get()), None)).pack()
    tkinter.Button(labelRedimensionnerTexture, text="Set Height", command= lambda: textureManageur.setTextureDim(gvars, image, zindex, None, int(entryRedimensionnerTexture.get()))).pack()
    
    