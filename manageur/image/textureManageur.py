

from PIL import Image, ImageTk
from manageur.image.gui import imageInfoGui
from manageur.image import imageManageur


def openTextureImageFile(gvars, fileName, name, dimension):
    if(fileName == None or fileName == ''):
        return
    if(dimension != None):
        gvars.texturesListe.append({'name': name, 'type': 'image', 'chemin': fileName, 'tkImage': ImageTk.PhotoImage(Image.open(fileName).resize(dimension)), 'dimension': dimension})
    else:
        image = Image.open(fileName)
        gvars.texturesListe.append({'name': name, 'type': 'image', 'chemin': fileName, 'tkImage': ImageTk.PhotoImage(image), 'dimension': image.size})
    
def resizeTexture(gvars, image, zindex, dwidth, dheight): 
    
    if(image["type"] == "image"):
        texture = gvars.texturesListe[image["imageId"]]     
        exDim = texture["dimension"]   
    if(image["type"] == "tile"):
        splitId = image["imageId"].split("-")
        imageId = int(splitId[0])
        tileId = int(splitId[1])
        texture = gvars.texturesListe[imageId]   
        exDim = texture["dimension"][tileId]
    
    setTextureDim(gvars, image, zindex, exDim[0] + dwidth, exDim[1] + dheight)
    
    
def setTextureDim(gvars, image, zindex, width, height):
    
    if(image["type"] == "image"):        
        texture = gvars.texturesListe[image["imageId"]]           
        dimension = texture["dimension"]            
    elif(image["type"] == "tile"):
        splitId = image["imageId"].split("-")
        imageId = int(splitId[0])
        tileId = int(splitId[1])
        texture = gvars.texturesListe[imageId]  
        dimension = texture["dimension"][tileId]
    else:
        return
    
    if(width == None):
        width = dimension[0]
    if(height == None):
        height = dimension[1]
    dimension = (width, height)
    
    if(image["type"] == "image"):
        texture["tkImage"] = ImageTk.PhotoImage(Image.open(texture["chemin"]).resize(dimension))
        texture["dimension"]  = dimension
    if(image["type"] == "tile"):
        imagePil = Image.open(texture["chemin"])
        imgDimension = imagePil.size
        ligne = texture['tileInfo']['lineNb']
        colonne = texture['tileInfo']['colonneNb']
        parLigne = imgDimension[1]/ligne        
        parColonne = imgDimension[0]/colonne
        
        colonneI = tileId % colonne
        ligneI = tileId // ligne
        
        texture["tkImage"][tileId] = ImageTk.PhotoImage(imagePil.crop((parColonne*(colonneI), parLigne*(ligneI), parColonne*(colonneI+1), parLigne*(ligneI+1))).resize(dimension))
        texture["dimension"][tileId] = dimension
    
    imageManageur.displayImages(gvars)
    imageInfoGui.load(gvars, image, zindex)
  