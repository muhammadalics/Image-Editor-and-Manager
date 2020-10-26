from main_gui import Ui_MainWindow

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import cv2
import image_editor
import scipy
import numpy as np
import replace_color
import blur_median


class MainProgram(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen.triggered.connect(self.clicked_open)
        self.ui.actionMirror.triggered.connect(self.clicked_mirror)
        self.ui.actionFlip_Upside_Down.triggered.connect(self.clicked_flip)
        self.ui.actionBrightness_Increase.triggered.connect(self.clicked_brightnessup)
        self.ui.actionBrightness_Decrease.triggered.connect(self.clicked_brightnessdown)
        self.ui.actionContrast_Increase.triggered.connect(self.clicked_contrastup)
        self.ui.actionContrast_Decrease.triggered.connect(self.clicked_contrastdown)
        self.ui.actionRed_Green.triggered.connect(self.clicked_swap_rg)
        self.ui.actionGreen_Blue.triggered.connect(self.clicked_swap_gb)
        self.ui.actionBlue_Red.triggered.connect(self.clicked_swap_br)
        self.ui.actionNegative.triggered.connect(self.clicked_negative)
        self.ui.actionBlack_and_White.triggered.connect(self.clicked_converttobw)
        self.ui.actionReplace_Color.triggered.connect(self.clicked_replacecolor)
        self.ui.actionMedian.triggered.connect(self.clicked_blur_median)

        self.original = None #Original Image
        self.current = None # this is the image in progress

    def update_current(self, image):
        self.current = image

    def update_imagebox(self):

        if len(self.current.shape) == 3: #for color images
            copyofcurrent = self.current.copy()
            self.updated_pic = QtGui.QImage(copyofcurrent,
                                      copyofcurrent.shape[1],
                                      copyofcurrent.shape[0],
                                      copyofcurrent.shape[1]*3,
                                      QtGui.QImage.Format_BGR888)#.QtGui.QImage.rgbSwapped()

        elif len(self.current.shape) == 2: #for color images
            print('here')
            copyofcurrent = self.current.copy()
            self.updated_pic = QtGui.QImage(copyofcurrent,
                                      copyofcurrent.shape[1],
                                      copyofcurrent.shape[0],
                                      copyofcurrent.shape[1]*1,
                                      QtGui.QImage.Format_Grayscale8)#.QtGui.QImage.rgbSwapped()


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

    def clicked_brightnessup(self):
        img = image_editor.brightness_up(self.current, 1, 1)
        self.update_current(img)
        self.update_imagebox()

    def clicked_brightnessdown(self):
        img = image_editor.brightness_down(self.current, 1, 1)
        self.update_current(img)
        self.update_imagebox()

    def clicked_contrastup(self):
        img = image_editor.brightness_up(self.current, 1.01, 0)
        self.update_current(img)
        self.update_imagebox()

    def clicked_contrastdown(self):
        img = image_editor.brightness_down(self.current, 0.99, 0)
        self.update_current(img)
        self.update_imagebox()

    def clicked_swap_rg(self):
        img = image_editor.swap_gr(self.current)
        self.update_current(img)
        self.update_imagebox()

    def clicked_swap_gb(self):
        img = image_editor.swap_bg(self.current)
        self.update_current(img)
        self.update_imagebox()

    def clicked_swap_br(self):
        img = image_editor.swap_rb(self.current)
        self.update_current(img)
        self.update_imagebox()

    def clicked_negative(self):
        img = image_editor.negative_color_picture(self.current)
        self.update_current(img)
        self.update_imagebox()

    def clicked_converttobw(self):
        img = image_editor.convert_to_bw(self.current)
        self.update_current(img)
        self.update_imagebox()

    def clicked_replacecolor(self):
        Dialog_replacecolor = QtWidgets.QDialog()
        dialog = replace_color.Ui_Dialog_replacecolor()
        dialog.setupUi(Dialog_replacecolor)
        Dialog_replacecolor.show()
        Dialog_replacecolor.exec_()

        if Dialog_replacecolor.accept:
            img = image_editor.replace_color(self.current, dialog.lineEdit.text(), dialog.lineEdit_2.text())
            print(dialog.lineEdit.text())
            self.update_current(img)
            self.update_imagebox()

    def clicked_blur_median(self):

        Dialog = QtWidgets.QDialog()
        ui = blur_median.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result==False:
            print('rejected')
            return

        elif result and int(ui.spinBox_kernelsize.text()) % 2 == 0:
            print('try again')
            error = 'Kernel size can only be odd.'
            QtWidgets.QMessageBox.warning(self, 'Error', error)
            self.clicked_blur_median()

        elif result:
            img = image_editor.median_blur(self.current, ui.spinBox_kernelsize.text(), ui.spinBox_numberofapplications.text())
            print('accepted')
            self.update_current(img)
            self.update_imagebox()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    mainwin = MainProgram()
    mainwin.show()

    app.exec_()
