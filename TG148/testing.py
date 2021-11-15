from PIL import Image
from PIL.TiffTags import TAGS
from skimage.transform import rotate
from PyQt5 import QtWidgets 
from PyQt5 import QtGui
from scipy.ndimage import gaussian_filter1d
import matplotlib.pyplot as plt
import numpy as np
 

################
test_file = 'H:\\test_film.tif'
################

tif = Image.open(test_file).convert('F')
#meta_dict = {TAGS[key] : tif.tag[key] for key in tif.tag.iterkeys()}



def auto_rotate(filmImage, filmMetaData):
    #takes scanned film image and rotates it so the beam profiles are horizontal
    
    filmImage       = np.array(filmImage)
    lineSum         = 0
    lineSumMaxi     = 0
    lineSumIndex    = round(filmImage.shape[0]/2.0)
    print(lineSumIndex)
    
    angles    = np.linspace(0, 180, num=500, endpoint=True)
    angleSave = 0 
    
    for ii in angles:
        filmImageRotated = rotate(filmImage, ii)
        lineSum = np.sum(filmImageRotated[lineSumIndex-2:lineSumIndex+2,:])
        #print(lineSum)
        if lineSum > lineSumMaxi:
            lineSumMaxi = lineSum
            angleSave   = ii
    #print(angleSave)
    
    return rotate(filmImage, angleSave)
        
    

def find_junction(filmImage):
    horIndex = round(filmImage.shape[0]/2.0)
    return np.argmax(np.abs(np.gradient(filmImage[horIndex,:])))       
        
def get_centers(filmImage, vertIndex):
    #vert index is the junction of the two fields, which we start a little
    #left and right of
    a1Index = vertIndex - 5
    b1Index = vertIndex + 5
    
    a11, a12 = get_fwhm_points(filmImage[:,a1Index])
    b11, b12 = get_fwhm_points(filmImage[:,b1Index])
    
    a1Center = (a11+a12)/2.0
    b1Center = (b11+b12)/2.0
    
    return a1Center, b1Center
    
    
def get_fwhm_points(curve):
    curve = gaussian_filter1d(curve, .01)
    print(curve)
    plt.plot(curve)
    maxi    = np.max(curve)
    width   = []
    for ii in range(len(curve)):
        if curve[ii]>maxi/2.0:
            width.append(ii)
            
    return width[0], width[-1]
    
    
    
    
def preprocess(filmImage):
    #this will invert the image values so the beam profile is the max value
    
    maxi = np.max(np.reshape(filmImage, -1))
    filmImage = filmImage - maxi
    filmImage = filmImage * -1.0
    return filmImage    
    