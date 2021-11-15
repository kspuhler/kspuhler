import numpy as np
from PIL import Image
from skimage.transform import rotate
import sys
sys.path.append("F://SHARING//Radiation Oncology Physics//Physics Staff//KS//Python//TG 148//View")
from View.Numpy2QImage import Numpy2QImage


class FilmLoader(object):
    
    def __init__(self, fname):
        self.originalFilm    = self._load_film(fname)
        self.processedFilm   = self._preproc(self.originalFilm)
        self.rotatedFilm     = self._auto_rotate(self.processedFilm)
        
        self.processedFilmImg = Numpy2QImage(self.processedFilm)
        self.rotatedFilmImage = Numpy2QImage(self.rotatedFilm)
    
    def _load_film(self, fname):
        originalFilm = Image.open(fname).convert('F')
        return np.array(originalFilm)
        
    def _preproc(self, filmImage):
        #returns an image with positive values, increasing with radiation
        #probably need a way to make this work for non negative films
        maxi = np.max(np.reshape(filmImage, -1))
        filmImage = filmImage - maxi
        filmImage = filmImage * -1.0
        return filmImage    
        
    def _auto_rotate(self, filmImage):
        #takes a raw film and orients it horizontally
        filmImage       = np.array(filmImage)
        lineSum         = 0
        lineSumMaxi     = 0
        lineSumIndex    = round(filmImage.shape[0]/2.0)
        print(lineSumIndex)
        
        angles    = np.linspace(0, 180, num=200, endpoint=True)
        angleSave = 0 
        
        for ii in angles:
            filmImageRotated = rotate(filmImage, ii)
            lineSum = np.sum(filmImageRotated[lineSumIndex-2:lineSumIndex+2,:])
            if lineSum > lineSumMaxi:
                lineSumMaxi = lineSum
                angleSave   = ii
        return rotate(filmImage, angleSave)
