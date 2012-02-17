from PyQt4.QtGui import QDialog, QFileDialog
from PyQt4 import uic
import os

class SaveDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        
        self.initUic()

    def initUic(self):
        p = os.path.split(__file__)[0]+'/'
        if p == "/": p = "."+p
        uic.loadUi(p+"saveDialog.ui", self)
        
        self.selectPathButton.clicked.connect(self.on_SelectPathButtonClicked)

    def on_SelectPathButtonClicked(self):
        fileName = QFileDialog.getSaveFileName(self, "Save File", os.path.abspath(__file__))
        self.lineEdit.setText(fileName)
    
    def exec_(self):
        if QDialog.exec_(self) == QDialog.Accepted:
            return  self.lineEdit.text()
        else:
            return "Cancel"
        
if __name__ == '__main__':
    from PyQt4.QtGui import QApplication
    app = QApplication(list())
    d = SaveDialog()
    d.show()
    app.exec_()