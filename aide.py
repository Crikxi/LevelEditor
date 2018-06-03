# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 03:43:37 2018

@author: Bastien
"""
import tkinter

def displayHelp():
    window = tkinter.Tk()
        
    text = tkinter.Label(window, text="Editeur de niveau 0.0.2\nCréé par Crikxi(Bastien)\nEncore en développement\n\nUtilisez le clic droit pour supprimer les platformes et les pièges\n2 clics du clic du bouton du milieu permet de faire une platforme/piege")
    text.pack()