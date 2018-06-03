# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:24:15 2018

@author: Bastien
"""

import tkinter
import json
import tkinter.filedialog
import tkinter.messagebox
import traceback
from PIL import Image, ImageTk 

def newFile(gvars, resetTextures=True):
    rep = tkinter.messagebox.askokcancel(title="Etes vous sur ?", message="La sauvegarde actuelle sera supprimé.\nEtes-vous sur de vouloir créer\nun nouveau niveau")
    if(rep == True):
        gvars.canvas.delete("all")
        if(resetTextures):
            gvars.texturesListe = [] 
        gvars.imagesListe = [[], []]    
        gvars.plateformesListe = []
        gvars.piegesListe = []

    

def openFile(gvars):
    fileName = tkinter.filedialog.askopenfilename(defaultextension=".json", filetypes=[("Fichier level", "*.json")])
    if(fileName == None or fileName == ''):
        return
    setMainDir(gvars)
    try:        
        file = open(fileName, mode='r')
        loadSave(gvars, file.read())
        file.close()
    except: 
        print("ERROR")
        traceback.print_exc()
        tkinter.messagebox.showerror("Erreur", "Impossible de charger le niveau")
    

def saveFile(gvars):
    fileName = tkinter.filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("FIchier level", "*.json")])
    if(fileName == None or fileName == ''):
        return
    setMainDir(gvars)
    file = open(fileName, mode='w')
    file.write(createSave(gvars))
    file.close()
    

def createSave(gvars):#convert and create save
    piegesListe = []
    for piege in gvars.piegesListe:
        piegesListe.append(piege["coords"])
        
    plateformesListe = []
    for plateforme in gvars.plateformesListe:
        plateformesListe.append(plateforme["coords"])
        
    topPlateformesListe = []
    for plateforme in gvars.topPlateformesListe:
        topPlateformesListe.append(plateforme["coords"])
        
    texturesListe = []
    for texture in gvars.texturesListe:
        if(texture['chemin'].startswith(gvars.mainRessourceDir)):
            texture['chemin'] = "./" + texture['chemin'][len(gvars.mainRessourceDir):]
        if(texture['type'] == "image"):
            texturesListe.append({'name': texture['name'], 'type': 'image', 'chemin': texture['chemin'], 'dimension': texture['dimension']})
        elif(texture['type'] == "tile"):
            texturesListe.append({'name': texture['name'], 'type': 'tile', 'chemin': texture['chemin'], 'dimension': texture['dimension'], 'tileInfo': texture['tileInfo']})
        
    imagesListe = []
    for imageIndex in range(len(gvars.imagesListe)):
        imagesListe.append([])
        for image in gvars.imagesListe[imageIndex]:
            imagesListe[imageIndex].append({'type': image['type'], 'imageId': image['imageId'], 'coords': image['coords']})
    
    
    return json.dumps({'saveVersion': 2, 'plateformesListe': plateformesListe, 'topPlateformesListe': topPlateformesListe, 'piegesListe': piegesListe, 'texturesListe': texturesListe, 'imagesListe': imagesListe})

def loadSave(gvars, content):#crontary of createSave
    save = json.loads(content)
    
    gvars.plateformesListe = []
    for plateformeCoord in save["plateformesListe"]:
        gvars.plateformesListe.append({'tkId': None, 'coords': plateformeCoord})
    
    gvars.topPlateformesListe = []
    if("topPlateformesListe" in save):
        for plateformeCoord in save["topPlateformesListe"]:
            gvars.topPlateformesListe.append({'tkId': None, 'coords': plateformeCoord})
    
    gvars.piegesListe = []
    for piegeCoord in save["piegesListe"]:
        gvars.piegesListe.append({'tkId': None, 'coords': piegeCoord})
    
    gvars.texturesListe = []
    for texture in save["texturesListe"]:
        if(texture["chemin"].startswith("./")):
            texture["chemin"] = gvars.mainRessourceDir + texture["chemin"][2:]
        if(texture['type'] == "image"):
            texture["tkImage"] = ImageTk.PhotoImage(Image.open(texture["chemin"]).resize(texture["dimension"]))
        elif(texture['type'] == "tile"):
            image = Image.open(texture["chemin"])
            imgDimension = image.size
            ligne = texture['tileInfo']['lineNb']
            colonne = texture['tileInfo']['colonneNb']
            parLigne = imgDimension[1]/ligne        
            parColonne = imgDimension[0]/colonne
            
            images = []
            tileId = 0
            for ligneI in range(ligne):
                for colonneI in range(colonne):
                    images.append(ImageTk.PhotoImage(image.crop((parColonne*(colonneI), parLigne*(ligneI), parColonne*(colonneI+1), parLigne*(ligneI+1))).resize(texture["dimension"][tileId])))
                    tileId += 1
            texture["tkImage"] = images  
        gvars.texturesListe.append(texture)   
    
    gvars.imagesListe = save["imagesListe"]


def setMainDir(gvars, force=False):
    if(gvars.mainRessourceDir == "" or force == True):        
        gvars.mainRessourceDir = tkinter.filedialog.askdirectory(title="Dossier ressource")
        if(not gvars.mainRessourceDir.endswith("/")):
            gvars.mainRessourceDir += "/"