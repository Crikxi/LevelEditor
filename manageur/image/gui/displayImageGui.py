# -*- coding: utf-8 -*-

import tkinter
from manageur.image import imageManageur

def load(gvars):
    if(len(gvars.texturesListe)>0):
        window = tkinter.Toplevel()
        liste = []
        for textures in gvars.texturesListe:
            liste.append(textures["name"])
            
        
        tkinter.Label(window, text="Texture:").pack()
        textureChoisie = tkinter.StringVar(window)
        tkinter.OptionMenu(window, textureChoisie, *liste).pack()
        
        
        tkinter.Label(window, text="Si tile, tileInfo:").pack()
        tileInfo = tkinter.StringVar(window)
        tkinter.Entry(window, textvariable=tileInfo).pack()
        
        tkinter.Label(window, text="Index:").pack()
        indexZ = tkinter.StringVar(window)
        tkinter.Spinbox(window, textvariable=indexZ, from_=0, to=len(gvars.imagesListe)-1).pack()
        tkinter.Button(window, text="+1 index", command=lambda: gvars.imagesListe.append([])).pack()
        
        
        createButton = tkinter.Button(window, text="Valider", command=lambda: validate(gvars, liste, textureChoisie, indexZ, tileInfo))    
        createButton.pack()
    else:
        tkinter.messagebox.showerror("Erreur", "Aucune texture chargée.")



def validate(gvars, liste, textureChoisie, indexZ, tileInfo):
    if(textureChoisie.get() == ""):
        tkinter.messagebox.showerror("Erreur", "Aucune image selectionnée.")            
        return
    imgType = gvars.texturesListe[liste.index(textureChoisie.get())]['type']
    if(imgType == "image"):
        imageManageur.createImageFromImage(gvars, liste.index(textureChoisie.get()), int(indexZ.get()))
    if(imgType == "tile"):
        imageManageur.createImageFromTile(gvars, liste.index(textureChoisie.get()), int(indexZ.get()), tileInfo.get())