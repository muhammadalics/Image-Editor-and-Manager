from main_gui import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import cv2
import image_editor
import scipy
import numpy as np

class MainProgram(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.clicked_open)
        self.ui.actionMirror.triggered.connect(self.clicked_mirror)
        self.ui.actionFlip_Upside_Down.triggered.connect(self.clicked_flip)


        self.original = None #Original Image
        self.current = None # this is the image in progress

    def update_current(self, image):
        self.current = image

    def update_imagebox(self):

        if len(self.current.shape) == 3: #for color images
            print('yes')
            # self.current = np.require(self.current, np.uint8, 'C')
            print(self.current.shape[1])
            print(self.current.shape[0])
            print(self.current.shape[1]*3)
            copyofcurrent = self.current.copy()
            self.updated_pic = QtGui.QImage(copyofcurrent,
                                      copyofcurrent.shape[1],
                                      copyofcurrent.shape[0],
                                      copyofcurrent.shape[1]*3,
                                      QtGui.QImage.Format_BGR888)#.QtGui.QImage.rgbSwapped()

        print('here')
        self.updated_pic = QtGui.QPixmap(self.updated_pic)
        self.ui.label_imagebox.setPixmap(self.updated_pic)

    def clicked_open(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
                                                  options=options)

        self.original = cv2.imread(fileName)
        self.update_current(self.original)
        print(self.original.dtype)

        self.pixmap = QtGui.QPixmap(fileName)
        self.ui.label_imagebox.setPixmap(self.pixmap)

    def clicked_mirror(self):
        img = image_editor.mirror(self.current)
        self.update_current(img)
        self.update_imagebox()

    def clicked_flip(self):
        img = image_editor.flip_upsidedown(self.current)
        self.update_current(img)
        self.update_imagebox()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    mainwin = MainProgram()
    mainwin.show()

    app.exec_()
