# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 03:08:42 2018

@author: Bastien
"""

from manageur.image import imageEvent
from manageur.rect import rectEvent
from functools import partial

def onButton1Release(ev):
    imageEvent.onButton1Release(ev)
    rectEvent.onButton1Release(ev)
    
def onMove(gvars, ev):
    imageEvent.onMove(gvars, ev)
    rectEvent.onMove(gvars, ev)
    
def onButton2Press(gvars, ev):
    rectEvent.onButton2Press(gvars, ev)

def onKeyReleaseE(gvars, ev):
	if ev.keycode == 69:
	    rectEvent.onButton2Press(gvars, ev)


def loadCanvas(gvars):
    gvars.canvas.bind("<ButtonRelease-1>", onButton1Release)
    gvars.canvas.bind("<Motion>", partial(onMove, gvars))
    gvars.canvas.bind("<ButtonRelease-2>", partial(onButton2Press, gvars))
    gvars.fenetre.bind("<KeyRelease>", partial(onKeyReleaseE, gvars))
    #canvas.bind("<ButtonRelease>", test)