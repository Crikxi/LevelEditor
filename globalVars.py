# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 03:32:22 2018

@author: Bastien
"""
class GVars():
    def __init__(self):
        

        self.fenetre = None
        
        self.canvas = None
        
        self.mainRessourceDir = ""
        self.canEditImage = True
        self.currentMode = ""
        self.texturesListe = [] #[{'name': 'blablou', 'type': 'image', 'chemin': "", 'tkImage': None, 'dimension':(200, 100)}]#The lsite of all images
        #[{'name': 'blablou', 'type': 'tile', 'chemin': "", 'tkImage': [], 'dimension':[(200, 100)], 'tileInfo':{'lineNb': 1, 'colonneNb': 1}}]#The lsite of all images
        
        
        self.imagesListe = [[], []]#[[{'type': 'image', 'imageId': 0, 'coords':(0,0), 'tkId': 'id'}], [{'type': 'image', 'imageId': 0, 'coords':[0,0], 'tkId': 'id'}]] 
        #imageListe[a] où est index-z(plus a grand plus devant)
        #[{'type': 'image', 'imageId': 0, 'coords':(0,0), 'tkId': 'id'}]
        #[{'type': 'tile', 'imageId': "0-0", 'coords':(0,0), 'tkId': 'id'}]
        
        self.plateformesListe = []#[{'tkId': 'id', 'coords': [[x0,y0], [x1,y1]]}]
        self.topPlateformesListe = []#[{'tkId': 'id', 'coords': [[x0,y0], [x1,y1]]}]
        self.piegesListe = []#[{'tkId': 'id', 'coords': ((10,100), (20,500))}]# {'tkId': 'id', 'coord': [[x0,y0], [x1,y1]]}




