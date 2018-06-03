# -*- coding: utf-8 -*-

import tkinter
import tkinter.filedialog
import tkinter.messagebox

import globalVars

import canvasEvent

from manageur.rect import rectManageur
from manageur.image import imageManageur
from manageur.save import saveManageur

from manageur.image.gui import loadTextureGui
from manageur.image.gui import displayImageGui


from functools import partial

import aide



if __name__ == '__main__':
    gvars = globalVars.GVars()
    gvars.fenetre = tkinter.Tk()
    
    gvars.fenetre.resizable(width=False, height=False)
    #globalVars.fenetre.attributes("-fullscreen", True)
    #globalVars.fenetre.geometry("1280x720")
    
    gvars.canvas = tkinter.Canvas(master=gvars.fenetre, width=1280,height=720, bg="black", highlightthickness=0)
    gvars.canvas.pack(anchor=tkinter.CENTER, expand=True)
    
    canvasEvent.loadCanvas(gvars)
    
    menuPrincipal = tkinter.Menu(gvars.fenetre)
    
    menuFichier = tkinter.Menu(menuPrincipal, tearoff=False)        
    menuPrincipal.add_cascade(label = "Fichier", menu = menuFichier)
    
    menuFichier.add_command(label = "Nouveau", command = partial(saveManageur.newFile, gvars))
    menuFichier.add_command(label = "Nouveau sauf textures", command = partial(saveManageur.newFile, gvars, resetTextures=False))
    menuFichier.add_command(label = "Ouvrir", command = partial(saveManageur.openFile, gvars))
    menuFichier.add_command(label = "Sauvegarder", command = partial(saveManageur.saveFile, gvars))
    menuFichier.add_separator()
    menuFichier.add_command(label = "Changer le dossier de ressource", command = lambda:saveManageur.setMainDir(gvars, True))
    #menuFichier.add_command(label = "open", command = lambda: print("world"))

    menuEditerImage = tkinter.Menu(menuPrincipal, tearoff=True)
    menuPrincipal.add_cascade(label = "Editer Image", menu = menuEditerImage)
    menuEditerImage.add_command(label = "Charger des images", command=lambda: loadTextureGui.load(gvars))
    menuEditerImage.add_command(label = "Creer image", command=lambda: displayImageGui.load(gvars))
    menuEditerImage.add_command(label = "Afficher images", command=lambda: imageManageur.displayImages(gvars))
    menuEditerImage.add_command(label = "Cacher images", command=lambda: imageManageur.hideImages(gvars))
    menuEditerImage.add_command(label = "Activer/Désactiver le déplacement des images", command=lambda: imageManageur.toggleEditImage(gvars))
    
    menuPiege = tkinter.Menu(menuPrincipal, tearoff=True)   
    menuPrincipal.add_cascade(label = "Editer Pieges", menu = menuPiege)
    menuPiege.add_command(label = "Afficher pièges", command= lambda: rectManageur.displayRect(gvars, "piege", color="red"))
    menuPiege.add_command(label = "Cacher pièges", command=lambda: rectManageur.hideRect(gvars, "piege"))    
    menuPiege.add_command(label = "Clic milieu : creer piège", command=lambda: rectManageur.setMiddleClicMode(gvars, "piege"))
    
    menuPlatforme = tkinter.Menu(menuPrincipal, tearoff=True)   
    menuPrincipal.add_cascade(label = "Editer Platformes", menu = menuPlatforme)
    menuPlatforme.add_command(label = "Afficher platformes", command=lambda: rectManageur.displayRect(gvars, "plateforme", color="green"))
    menuPlatforme.add_command(label = "Cacher platformes", command=lambda: rectManageur.hideRect(gvars, "plateforme"))
    menuPlatforme.add_command(label = "Clic milieu : creer platformes", command=lambda: rectManageur.setMiddleClicMode(gvars, "plateforme"))
    
    menuPlatformeTop = tkinter.Menu(menuPrincipal, tearoff=True)   
    menuPrincipal.add_cascade(label = "Editer Platformes traversables", menu = menuPlatformeTop)
    menuPlatformeTop.add_command(label = "Afficher platformes traversables", command=lambda: rectManageur.displayRect(gvars, "topPlateforme", color="blue"))
    menuPlatformeTop.add_command(label = "Cacher platformes traversables", command=lambda: rectManageur.hideRect(gvars, "topPlateforme"))
    menuPlatformeTop.add_command(label = "Clic milieu : creer platformes traversables", command=lambda: rectManageur.setMiddleClicMode(gvars, "topPlateforme"))
    
    menuPrincipal.add_command(label = "Aide", command=aide.displayHelp)
    
    gvars.fenetre.configure(menu = menuPrincipal)
    
    gvars.fenetre.mainloop()
