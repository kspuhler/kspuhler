import sys
sys.path.append("F://SHARING//Radiation Oncology Physics//Physics Staff//KS//Python//TG 148//Model")


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QToolBar
#from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QColor
from PIL import Image
from PIL.TiffTags import TAGS
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import rotate
from Model.FilmLoader import FilmLoader
from Model.TG148Analysis import TG148Analysis




class MainGUI(QWidget):
    
    def __init__(self, parent=None):
        
        super().__init__(parent)
        
        self.resize(750,750)
        self.mainwindow = QGridLayout()  
        self.originalFilm = QLabel(self)
        self.originalFilm.setGeometry(0, 250, 250, 250)
        self.originalFilm.setScaledContents(True)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("TG148 Y Divergence Test")
        fileButton = QPushButton("Select Film", self)
        fileButton.move(100,550)
        fileButton.clicked.connect(self._get_film_image)
        
        rotateButton = QPushButton("Rotate Film", self)
        rotateButton.setToolTip('Click without entering a number for auto-rotate \n Or enter a custom angle')
        rotateButton.move(100,600)
        rotateButton.clicked.connect(self._showRotatedFilm)

        self.userAngle =  QLineEdit(self)
        self.userAngle.move(200, 605) 
        self.userAngle.resize(50, 30)
        
        self.analyzeButton = QPushButton("Analyze Film", self)
        self.analyzeButton.setEnabled(False)
        self.analyzeButton.move(100,650)
        self.analyzeButton.clicked.connect(self._analyze_film)
            
        self.show()
        
    def _get_film_image(self):
        #make file loader 
        dlg = QFileDialog().getOpenFileName(parent=self, caption="Select a Film File")
        self.Loader = FilmLoader(dlg[0])
        
        pix_proc = QPixmap(self.Loader.processedFilmImg.result)        
        self.originalFilm.setPixmap((pix_proc))        
        self.originalFilm.show()
        self.analyzeButton.setEnabled(True)
        
    def _showRotatedFilm(self):
        if self.userAngle.text() != "":
               self.Loader.rotatedFilm = rotate(self.Loader.processedFilm, float(self.userAngle.text()))
               self.Loader.rotatedFilmImage = Numpy2QImage(self.Loader.rotatedFilm)
        pix_rot  = QPixmap(self.Loader.rotatedFilmImage.result)     
        self.originalFilm.setPixmap((pix_rot))
        self.Loader.filmToAnalyze = self.Loader.rotatedFilm
        self.originalFilm.show()
        #have some display of the center and shit
    
    def _analyze_film(self):
        TG = TG148Analysis(self.Loader)
        

    


        

        
