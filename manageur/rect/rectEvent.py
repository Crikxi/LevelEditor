
from manageur.rect import rectManageur

oldX = -1
oldY = -1
selectionedRect = []

clickX = None
clickY = None



def onMove(gvars, ev):
    global oldX, oldY
    deltaX = ev.x - oldX
    deltaY = ev.y - oldY
    oldX = ev.x
    oldY = ev.y
    for rect in selectionedRect:
        x0 = rect["coords"][0][0] + deltaX
        y0 = rect["coords"][0][1] + deltaY
        x1 = rect["coords"][1][0] + deltaX
        y1 = rect["coords"][1][1] + deltaY
        rect["coords"] = [[x0,y0],[x1,y1]]
        gvars.canvas.coords(rect["tkId"], x0, y0, x1, y1)
        
def onButton1Release(ev):
    global selectionedRect
    selectionedRect = []

def onButton1Press(rect, ev):
    global selectionedRect
    selectionedRect.append(rect)

def onButton2Press(gvars, ev):
    global clickX, clickY
    if(clickX == None and clickY == None):
        clickX = ev.x
        clickY = ev.y
    else:
        x0 = min(clickX, ev.x)
        x1 = max(clickX, ev.x)
        y0 = min(clickY, ev.y)
        y1 = max(clickY, ev.y)
        
        clickX = None
        clickY = None
        rectManageur.creerPlateforme(gvars, gvars.currentMode, [[x0,y0],[x1,y1]])

        

def onButton3Press(gvars, rect, rectType, ev):
    gvars.canvas.delete(rect["tkId"])
    rectManageur.getListFromType(gvars, rectType).remove(rect)
        