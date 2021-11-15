from Model import TG148Analysis, FilmLoader
from View.MainGUI import MainGUI
from PyQt5.QtWidgets import QApplication
import sys


mainStyleSheet = '''

QWidget{
        background-color:#66258b;
        color:white;
        }

QLabel{
        background-color:#dfcbeb;
        color:white;
        }

QTableWidget{
            font-size:10pt;
            }
            
QHeaderView{
           font-size:12pt;
           background-color:#2E6E3E;
           }

QComboBox{
         font-size:12pt;
         }

QPushButton{
            qproperty-iconSize:28px;
            font-size:10px;
            height:30px;
            width:32px;
           }

QToolTip{
    font-size:14px;
    background-color:#FFFFB7;
    }

QDialog QCheckBox{
    font-size:14px;
    }

QMessageBox{
    font-size:14px;
    }

QMessageBox DetailedText{
    font-size:14px;
    }
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(mainStyleSheet)
    app.setStyle('Fusion')
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())