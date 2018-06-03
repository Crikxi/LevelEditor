# -*- coding: utf-8 -*-
import tkinter
from PIL import Image, ImageTk

class tileConfigureGui:
    def __init__(self, gvars, fileName, name, dimension):
        
        self.gvars = gvars
        if(fileName == None or fileName == ''):
            return
        #ImageTk.PhotoImage(self.image)
        self.fileName = fileName
        self.name = name
        
        image = Image.open(fileName)
        if(dimension == None):
            dimension = image.size
        
        self.dimension = dimension
        self.image = image.resize(dimension)

    
    
        self.window = tkinter.Toplevel()
        tkinter.Label(self.window, text="Nom: " + self.name).pack()     
        
        tkinter.Label(self.window, text="Nombre d'image par ligne/colonne").pack()
        self.ligne = tkinter.StringVar(self.window)
        self.ligne.trace("w", lambda name, index, mode: self.actualizeImagePerTile())
        tkinter.Entry(self.window, textvariable=self.ligne).pack()
        self.colonne = tkinter.StringVar(self.window)
        self.colonne.trace("w", lambda name, index, mode: self.actualizeImagePerTile())
        tkinter.Entry(self.window, textvariable=self.colonne).pack()
           
        saveButton = tkinter.Button(self.window, text="Sauvegarder", command=self.save)    
        saveButton.pack()
        
        self.canvas = tkinter.Canvas(self.window, width=1280,height=720, bg="black")
        self.imageTk = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0,0, image=self.imageTk, anchor=tkinter.NW)
        self.canvas.pack()
        

    def actualizeImagePerTile(self):
        self.canvas.delete("separationBar")
        try:
            ligne = int(self.ligne.get())
            colonne = int(self.colonne.get())
        except:
            return
        if(ligne <= 0 or colonne <= 0):
            return
        parLigne = self.dimension[1]/ligne
        
        for ligneI in range(ligne):
            y = parLigne*(ligneI+1)
            self.canvas.create_line(0, y, self.dimension[0], y, fill="red", tags="separationBar")

        
        parColonne = self.dimension[0]/colonne
        for colonneI in range(colonne):
            x = parColonne*(colonneI+1)
            self.canvas.create_line(x, 0, x, self.dimension[1], fill="red", tags="separationBar")

                
        

    def save(self):
        try:
            ligne = int(self.ligne.get())
            colonne = int(self.colonne.get())
        except:
            return
        if(ligne <= 0 or colonne <= 0):
            return
        
        parLigne = self.dimension[1]/ligne        
        parColonne = self.dimension[0]/colonne
        
        images = []
        dimensions = []
        defaultDimension = (int(self.dimension[0] / colonne), int(self.dimension[1] / ligne))
        for ligneI in range(ligne):
            for colonneI in range(colonne):
                dimensions.append(defaultDimension)
                images.append(ImageTk.PhotoImage(self.image.crop((parColonne*(colonneI), parLigne*(ligneI), parColonne*(colonneI+1), parLigne*(ligneI+1))).resize(defaultDimension)))
        self.gvars.texturesListe.append({'name': self.name, 'type': 'tile', 'chemin': self.fileName, 'tkImage': images, 'dimension': dimensions, 'tileInfo':{'lineNb': ligne, 'colonneNb': colonne}})
        self.window.destroy()