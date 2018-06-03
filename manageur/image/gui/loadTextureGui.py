# -*- coding: utf-8 -*-

import tkinter
from manageur.image import textureManageur
from manageur.image.gui import tileConfigureGui
from PIL import Image, ImageTk



def load(gvars):
    window = tkinter.Toplevel()
    menuChoice = tkinter.StringVar(window)
    menuChoice.set("Image")
    menu = tkinter.OptionMenu(window, menuChoice, "Image", "TileMap")
    menu.pack()
    tkinter.Label(window, text="Nom: ").pack()
    name = tkinter.StringVar(window)
    tkinter.Entry(window, textvariable=name).pack()        
    
    tkinter.Label(window, text="Dimension (1 image): largeur/hauteur(nombre entier)").pack()
    width = tkinter.StringVar(window)
    tkinter.Spinbox(window, textvariable=width).pack()
    height = tkinter.StringVar(window)
    tkinter.Spinbox(window, textvariable=height).pack()
       
    openButton = tkinter.Button(window, text="Ouvrir le fichier", command=lambda: onClickOpen(gvars, menuChoice, name, width, height))    
    openButton.pack()



def onClickOpen(gvars, menuChoice, name, width, height):
    try:
        imageType = menuChoice.get()
    except:
        tkinter.messagebox.showerror("Erreur", "Une erreur est survenue, \navez-vous tous bien remplis ?")
        return
    
    try:
        dimension = (int(width.get()), int(height.get()))
    except:
        dimension = None
    fileName = tkinter.filedialog.askopenfilename(filetypes=[("Image", "*")])
    if(imageType == "Image"):
        textureManageur.openTextureImageFile(gvars, fileName, name.get(), dimension)
    elif(imageType == "TileMap"):
        tileConfigureGui.tileConfigureGui(gvars, fileName, name.get(), dimension)
    else:
        tkinter.messagebox.showerror("Erreur", "Type incorrect")
        
