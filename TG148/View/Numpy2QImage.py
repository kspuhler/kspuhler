import numpy as np
from PyQt5.QtGui import QImage

class Numpy2QImage(object):
    
    def __init__(self, numpy):
        h,w = numpy.shape
        numpy = numpy.astype(np.uint8)
        self.result = QImage(numpy.data, w, h, numpy.strides[0], QImage.Format_Grayscale8)
        self.result.ndarray = numpy
