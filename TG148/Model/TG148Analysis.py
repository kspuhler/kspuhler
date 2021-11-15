import numpy as np
from skimage.transform import rotate
from scipy.ndimage import gaussian_filter1d


class TG148Analysis(object):
    
    def __init__(self, FilmLoader):
        film = FilmLoader.filmToAnalyze
        
        self.ind   = self.find_junction(film)
        print(self.ind)
        self.a1, self.b1 =  self.get_centers(film, self.ind)      
        print(self.a1)
        print(self.b1)
        self.d = np.abs(self.a1 - self.b1) # number of "dots" apart
        self.d *= 0.35 #converts to mm
        print(self.d)
        
    def find_junction(self, filmImage):
        horIndex = round(filmImage.shape[0]/2.0)
        return np.argmax(np.abs(np.gradient(filmImage[horIndex,:])))       
        
    def get_centers(self, filmImage, vertIndex):
        #vert index is the junction of the two fields, which we start a little
        #left and right of
        a1Index = vertIndex -35
        b1Index = vertIndex +35
    
        a11, a12 = self.get_fwhm_points(filmImage[:,a1Index])
        b11, b12 = self.get_fwhm_points(filmImage[:,b1Index])
    
        a1Center = round((a11+a12)/2.0)
        b1Center = round((b11+b12)/2.0)
        
        return a1Center, b1Center
    
    
    def get_fwhm_points(self, curve):
        curve = gaussian_filter1d(curve, .01)
        maxi    = np.max(curve)
        width   = []

        for ii in range(len(curve)):
            if curve[ii]>maxi/2.0:
                width.append(ii)
               
        return width[0], width[-1]
        