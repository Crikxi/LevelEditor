
import globalVars
from manageur.image import imageManageur
from manageur.image.gui import imageInfoGui


oldX = -1
oldY = -1
selectionedImageToMove = []

def onMove(gvars, ev):
    global oldX, oldY
    deltaX = ev.x - oldX
    deltaY = ev.y - oldY
    oldX = ev.x
    oldY = ev.y
    if(gvars.canEditImage == True):
        for image in selectionedImageToMove:
            x = image["coords"][0] + deltaX
            y = image["coords"][1] + deltaY
            image["coords"] = [x,y]
            gvars.canvas.coords(image["tkId"], x, y)
        
def onButton1Release(ev):
    global selectionedImageToMove
    selectionedImageToMove = []

def onButton1Press(image, ev):
    global selectionedImageToMove
    selectionedImageToMove.append(image)

def onButton3Press(gvars, image, zindex, ev):
   imageInfoGui.load(gvars, image, zindex)