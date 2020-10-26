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
import blur_gaussian
import blur_average
import heatmap
import pixelate
import cartoonify
import gamma
import dither
import canny
import noise_gaussian
import verticalnoisebands

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
        self.ui.actionGaussian_2.triggered.connect(self.clicked_blur_gaussian)
        self.ui.actionAverage.triggered.connect(self.clicked_blur_average)
        self.ui.actionIntensity_Map.triggered.connect(self.clicked_intensity_map)
        self.ui.actionPixelate.triggered.connect(self.clicked_pixelate)
        self.ui.actionCartoonify.triggered.connect(self.clicked_cartoonify)
        self.ui.actionGamma_Correction.triggered.connect(self.clicked_gamma)
        self.ui.actionDithering.triggered.connect(self.clicked_dither)
        self.ui.actionEdge_Detection.triggered.connect(self.clicked_canny)
        self.ui.actionGaussian.triggered.connect(self.clicked_gaussian_noise)
        self.ui.actionVertical_Bands.triggered.connect(self.clicked_vertical_noise_bands)

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
        if len(self.current.shape) ==2:
            error = 'No colors to swap.'
            QtWidgets.QMessageBox.warning(self, 'Image is grayscale.', error)
        else:
            img = image_editor.swap_gr(self.current)
            self.update_current(img)
            self.update_imagebox()

    def clicked_swap_gb(self):
        if len(self.current.shape) ==2:
            error = 'No colors to swap.'
            QtWidgets.QMessageBox.warning(self, 'Image is grayscale.', error)
        else:
            img = image_editor.swap_bg(self.current)
            self.update_current(img)
            self.update_imagebox()

    def clicked_swap_br(self):
        if len(self.current.shape) ==2:
            error = 'No colors to swap.'
            QtWidgets.QMessageBox.warning(self, 'Image is grayscale.', error)
        else:
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

    def clicked_blur_gaussian(self):
        Dialog = QtWidgets.QDialog()
        ui = blur_gaussian.Ui_Dialog()
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
            self.clicked_blur_gaussian()
        elif result:
            img = image_editor.gaussian_blur(self.current, ui.spinBox_kernelsize.text(), ui.spinBox_numberofapplications.text())
            print('accepted')
            self.update_current(img)
            self.update_imagebox()

    def clicked_blur_average(self):
        Dialog = QtWidgets.QDialog()
        ui = blur_average.Ui_Dialog_avgblur()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result==False:
            print('rejected')
            return
        # elif result and int(ui.spinBox_kernelsize.text()) % 2 == 0:
        #     print('try again')
        #     error = 'Kernel size can only be odd.'
        #     QtWidgets.QMessageBox.warning(self, 'Error', error)
        #     self.clicked_blur_average()
        elif result:
            img = image_editor.avg_blur(self.current, ui.spinBox_kernelsize.text(), ui.spinBox_numberofapplications.text())
            print('accepted')
            self.update_current(img)
            self.update_imagebox()

    def clicked_intensity_map(self):
        Dialog = QtWidgets.QDialog()
        ui = heatmap.Ui_Dialog_heatmap()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        img = image_editor.intensity_map(self.current, ui.comboBox_heatmap.currentText())
        self.update_current(img)
        self.update_imagebox()

    def clicked_pixelate(self):
        Dialog = QtWidgets.QDialog()
        ui = pixelate.Ui_Dialog_pixelate()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        img = image_editor.pixelate(self.current, ui.spinBox_pixelate.text())
        self.update_current(img)
        self.update_imagebox()

    def clicked_cartoonify(self):
        Dialog = QtWidgets.QDialog()
        ui = cartoonify.Ui_Dialog_cartoonify()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        img = image_editor.cartoonify(self.current, ui.spinBox_thresh1.text(), ui.spinBox_thresh2.text())
        self.update_current(img)
        self.update_imagebox()

    def clicked_gamma(self):
        Dialog = QtWidgets.QDialog()
        ui = gamma.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        img = image_editor.gamma_correction(self.current, ui.doubleSpinBox_gamma.text())
        self.update_current(img)
        self.update_imagebox()

    def clicked_dither(self):
        Dialog = QtWidgets.QDialog()
        ui = dither.Ui_Dialog_dither()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        img = image_editor.dither(self.current, ui.spinBox_order.text())
        self.update_current(img)
        self.update_imagebox()

    def clicked_canny(self):
        Dialog = QtWidgets.QDialog()
        ui = canny.Ui_Dialog_canny()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result and int(ui.spinBox_kernelsize.text()) % 2 == 0:
            print('try again')
            error = 'Kernel size can only be odd.'
            QtWidgets.QMessageBox.warning(self, 'Error', error)
            self.clicked_canny()
        elif result and int(ui.spinBox_thresh1.text()) == int(ui.spinBox_thresh2.text()):
            print('try again')
            error = 'Thresholds cannot be equal.'
            QtWidgets.QMessageBox.warning(self, 'Error', error)
            self.clicked_canny()

        else:
            img = image_editor.edge_detection(self.current, ui.spinBox_thresh1.text(), ui.spinBox_thresh2.text(), ui.spinBox_kernelsize.text(), ui.comboBox.currentText())
            self.update_current(img)
            self.update_imagebox()

    def clicked_gaussian_noise(self):
        Dialog = QtWidgets.QDialog()
        ui = noise_gaussian.Ui_Dialog_gaussian_noise()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        img = image_editor.add_Gaussian_noise(self.current, ui.doubleSpinBox_sigma.text(), ui.comboBox_channel.currentText())
        self.update_current(img)
        self.update_imagebox()

    def clicked_vertical_noise_bands(self):
        Dialog = QtWidgets.QDialog()
        ui = verticalnoisebands.Ui_Dialog_noiseband_vertical()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        img = image_editor.band_noise_vertical(self.current, ui.spinBox_width.text(), ui.spinBox_period.text(), ui.spinBox_magnitude.text())
        self.update_current(img)
        self.update_imagebox()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    mainwin = MainProgram()
    mainwin.show()

    app.exec_()
