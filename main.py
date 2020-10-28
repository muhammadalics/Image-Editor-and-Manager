from PyQt5.QtCore import pyqtSlot

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
import horizontalnoisebands
import extractcolor
import addborder
import image_histogram
import pyramidblending_modified
import alphablending
import resize_ui

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
        self.ui.actionHorizontal_Bands.triggered.connect(self.clicked_horizontal_noise_bands)
        self.ui.actionExtract_Color.triggered.connect(self.clicked_extract_color)
        self.ui.actionAdd_Border.triggered.connect(self.clicked_add_border)
        self.ui.actionHistogram_Equalization.triggered.connect(self.clicked_histogramequalization)
        self.ui.actionImage_Histogram.triggered.connect(self.clicked_image_histogram)
        self.ui.actionSave.triggered.connect(self.clicked_save)
        self.ui.actionPyramid.triggered.connect(self.clicked_pyramid_blending_loadfiles)
        self.ui.actionAlpha.triggered.connect(self.clicked_alpha_blending)
        self.ui.actionResize.triggered.connect(self.resize_image)
        self.ui.actionRotate.triggered.connect(self.clicked_rotate_image)
        self.ui.actionApply_Mask.triggered.connect(self.clicked_apply_mask)

        self.ui.actionUndo.triggered.connect(self.clicked_undo)
        self.ui.actionRedo.triggered.connect(self.clicked_redo)
        self.original = None #Original Image
        self.current = None # this is the image in progress
        self.redo = None
        self.currentminusone = None
        self.counter_undo = 0
        self.counter_redo = 0

    def perform_updates(self, current):
        print('inside perform updates')
        if self.current is not None:
            self.update_current_minus_one(self.current.copy())
        self.update_current(current)
        print('progressing inside perform updates')
        self.update_imagebox()

    def update_current_minus_one(self, image):
        self.currentminusone = image

    # def update_for_redo(self):
    #     self.redo_image = self.current

    def update_current(self, image):
        self.current = image

    def update_imagebox(self):
        print('inside updatebox')
        if len(self.current.shape) == 3: #for color images
            copyofcurrent = self.current.copy()
            # copyofcurrent[:,:,[0,2]] = copyofcurrent[:,:,[2,0]]
            print(copyofcurrent.dtype)
            self.updated_pic = QtGui.QImage(copyofcurrent,
                                      copyofcurrent.shape[1],
                                      copyofcurrent.shape[0],
                                      copyofcurrent.shape[1]*3,
                                      QtGui.QImage.Format_BGR888) #QtGui.QImage.Format_BGR888)

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

    def check_canvas(self):
        if self.current is None:
            QtWidgets.QMessageBox.warning(self, 'No image found', 'Please load an image first.')
            return
        return 1

    def clicked_undo(self):
        if self.counter_redo == self.counter_undo and self.current is not None and self.currentminusone is not None:
            self.redo = self.current.copy()
            self.update_current(self.currentminusone)
            self.update_imagebox()
            self.counter_undo += 1

    def clicked_redo(self):
        if self.counter_undo != 0 and self.counter_undo > self.counter_redo:
            self.currentminusone = self.current.copy()
            self.update_current(self.redo)
            self.update_imagebox()
            self.counter_redo += 1

    def get_filename(self, msg):
        print('get file name')
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, msg, "", "All Files (*)",
                                                  options=options)


        return fileName

    def clicked_open(self):
        # options = QtWidgets.QFileDialog.Options()
        # fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*)",
        #                                           options=options)

        fileName = self.get_filename('Load image')

        if len(fileName) == 0:
            return

        self.original = cv2.imread(fileName)#.astype(np.float32)
        self.update_current(self.original)
        print(self.original.dtype)

        self.pixmap = QtGui.QPixmap(fileName)
        self.ui.label_imagebox.setPixmap(self.pixmap)

    def clicked_save(self):
        if self.current is None:
            QtWidgets.QMessageBox.warning(self, "No file to save", "File can't be saved.")
            return

        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                         "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        print('filepath')
        print(len(filePath))
        print(filePath)
        print('_')
        print(_)
        if len(filePath) != 0:
            cv2.imwrite(filePath, self.current)


    def clicked_mirror(self):
        if self.check_canvas() == None: return
        img = image_editor.mirror(self.current)
        # self.update_current_minus_one(self.current.copy())
        # self.update_current(img)
        # self.update_imagebox()
        self.perform_updates(img)

    def clicked_flip(self):
        if self.check_canvas() == None: return
        img = image_editor.flip_upsidedown(self.current)
        # self.update_current(img)
        # self.update_imagebox()
        self.perform_updates(img)


    def clicked_brightnessup(self):
        img = image_editor.brightness_contrast(self.current, 1, 1)
        self.perform_updates(img)

    def clicked_brightnessdown(self):
        img = image_editor.brightness_contrast(self.current, 1, -1)
        # img = image_editor.brightness_down(self.current, 1, 1)
        self.perform_updates(img)

    def clicked_contrastup(self):
        img = image_editor.brightness_contrast(self.current, 1.01, 0)
        self.perform_updates(img.astype(np.uint8))

    def clicked_contrastdown(self):
        img = image_editor.brightness_contrast(self.current, 0.99, 0)
        self.perform_updates(img)

    def clicked_swap_rg(self):
        if self.check_canvas() == None: return
        if len(self.current.shape) ==2:
            error = 'No colors to swap.'
            QtWidgets.QMessageBox.warning(self, 'Image is grayscale.', error)
        else:
            img = image_editor.swap_gr(self.current)
            # self.update_current(img)
            # self.update_imagebox()
            self.perform_updates(img)

    def clicked_swap_gb(self):
        if self.check_canvas() == None: return
        if len(self.current.shape) ==2:
            error = 'No colors to swap.'
            QtWidgets.QMessageBox.warning(self, 'Image is grayscale.', error)
        else:
            img = image_editor.swap_bg(self.current)
            # self.update_current(img)
            # self.update_imagebox()
            self.perform_updates(img)

    def clicked_swap_br(self):
        if self.check_canvas() == None: return
        if len(self.current.shape) ==2:
            error = 'No colors to swap.'
            QtWidgets.QMessageBox.warning(self, 'Image is grayscale.', error)
        else:
            img = image_editor.swap_rb(self.current)
            # self.update_current(img)
            # self.update_imagebox()
            self.perform_updates(img)

    def clicked_negative(self):
        if self.check_canvas() == None: return
        img = image_editor.negative_color_picture(self.current)
        self.perform_updates(img)

    def clicked_converttobw(self):
        if self.check_canvas() == None: return
        img = image_editor.convert_to_bw(self.current)
        self.perform_updates(img)

    def clicked_replacecolor(self):
        if self.check_canvas() == None: return
        Dialog_replacecolor = QtWidgets.QDialog()
        dialog = replace_color.Ui_Dialog_replacecolor()
        dialog.setupUi(Dialog_replacecolor)
        Dialog_replacecolor.show()
        result = Dialog_replacecolor.exec_()

        if dialog.radioButton_greater.isChecked():
            operator = '>'
        elif dialog.radioButton_lesser.isChecked():
            operator = '<'
        else:
            operator ='='

        if result:
            img = image_editor.replace_color(self.current, dialog.lineEdit.text(), dialog.lineEdit_2.text(), operator)
            self.perform_updates(img)

    def clicked_blur_median(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = blur_median.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result==False:
            print('rejected')
            return

        elif result and (int(ui.spinBox_kernelsize.text()) == 0 or int(ui.spinBox_numberofapplications.text()) == 0):
            return

        elif result and int(ui.spinBox_kernelsize.text()) % 2 == 0:
            print('try again')
            error = 'Kernel size can only be odd.'
            QtWidgets.QMessageBox.warning(self, 'Error', error)
            self.clicked_blur_median()
        elif result:
            img = image_editor.median_blur(self.current, ui.spinBox_kernelsize.text(), ui.spinBox_numberofapplications.text())
            print('accepted')
            # self.update_current(img)
            # self.update_imagebox()
            self.perform_updates(img)

    def clicked_blur_gaussian(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = blur_gaussian.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result==False:
            print('rejected')
            return

        elif result and (int(ui.spinBox_kernelsize.text()) == 0 or int(ui.spinBox_numberofapplications.text()) == 0):
            return

        elif result and int(ui.spinBox_kernelsize.text()) % 2 == 0:
            print('try again')
            error = 'Kernel size can only be odd.'
            QtWidgets.QMessageBox.warning(self, 'Error', error)
            self.clicked_blur_gaussian()
        elif result:
            img = image_editor.gaussian_blur(self.current, ui.spinBox_kernelsize.text(), ui.spinBox_numberofapplications.text())
            print('accepted')
            # self.update_current(img)
            # self.update_imagebox()
            self.perform_updates(img)

    def clicked_blur_average(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = blur_average.Ui_Dialog_avgblur()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result==False:
            print('rejected')
            return

        if result and (int(ui.spinBox_kernelsize.text()) == 0 or  int(ui.spinBox_numberofapplications.text() == 0)):
            return

        elif result:
            img = image_editor.avg_blur(self.current, ui.spinBox_kernelsize.text(), ui.spinBox_numberofapplications.text())
            print('accepted')
            # self.update_current(img)
            # self.update_imagebox()
            self.perform_updates(img)

    def clicked_intensity_map(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = heatmap.Ui_Dialog_heatmap()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            img = image_editor.intensity_map(self.current, ui.comboBox_heatmap.currentText())
            self.perform_updates(img)

    def clicked_pixelate(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = pixelate.Ui_Dialog_pixelate()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            if ui.spinBox_pixelate.text() == 0:
                return
            img = image_editor.pixelate(self.current, ui.spinBox_pixelate.text())
            self.perform_updates(img)

    def clicked_cartoonify(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = cartoonify.Ui_Dialog_cartoonify()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            img = image_editor.cartoonify(self.current, ui.spinBox_thresh1.text(), ui.spinBox_thresh2.text())
            self.perform_updates(img)

    def clicked_gamma(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = gamma.Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            img = image_editor.gamma_correction(self.current, ui.doubleSpinBox_gamma.text())
            self.perform_updates(img)

    def clicked_dither(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = dither.Ui_Dialog_dither()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            img = image_editor.dither(self.current, ui.spinBox_order.text())
            self.perform_updates(img)

    def clicked_canny(self):
        if self.check_canvas() == None: return
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

        elif result:
            img = image_editor.edge_detection(self.current, ui.spinBox_thresh1.text(), ui.spinBox_thresh2.text(), ui.spinBox_kernelsize.text(), ui.comboBox.currentText())
            self.perform_updates(img)

    def clicked_gaussian_noise(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = noise_gaussian.Ui_Dialog_gaussian_noise()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            img = image_editor.add_Gaussian_noise(self.current, ui.doubleSpinBox_sigma.text(), ui.comboBox_channel.currentText())
            # self.update_current(img)
            # self.update_imagebox()
            self.perform_updates(img.astype(np.uint8))

    def clicked_vertical_noise_bands(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = verticalnoisebands.Ui_Dialog_noiseband_vertical()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            if float(ui.spinBox_width.text()) == 0 or float(ui.spinBox_period.text()) == 0 or float(ui.spinBox_magnitude.text()) ==0:
                return
            img = image_editor.band_noise_vertical(self.current, ui.spinBox_width.text(), ui.spinBox_period.text(), ui.spinBox_magnitude.text())
            self.perform_updates(img)

    def clicked_horizontal_noise_bands(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = horizontalnoisebands.Ui_Dialog_horizontalnoise()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            if float(ui.spinBox_width.text()) == 0 or float(ui.spinBox_period.text()) == 0 or float(ui.spinBox_magnitude.text()) ==0:
                return

            img = image_editor.band_noise_horizontal(self.current, ui.spinBox_width.text(), ui.spinBox_period.text(), ui.spinBox_magnitude.text())
            self.perform_updates(img)

    def clicked_extract_color(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = extractcolor.Ui_Dialog_extractcolor()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            img = image_editor.extract_color(self.current, ui.lineEdit_extractcolor.text())
            self.perform_updates(img)

    def clicked_add_border(self):
        if self.check_canvas() == None: return
        Dialog = QtWidgets.QDialog()
        ui = addborder.Ui_Dialog_addborder()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            top = int(ui.spinBox_top.text())
            bottom = int(ui.spinBox_bottom.text())
            left = int(ui.spinBox_left.text())
            right = int(ui.spinBox_right.text())
            value = [int(ui.spinBox_blue.text()), int(ui.spinBox_green.text()), int(ui.spinBox_red.text())]

            if top == 0 and bottom ==0 and left ==0 and right ==0:
                return

            img = image_editor.add_border(self.current,
                                          top=top,
                                          bottom=bottom,
                                          left=left,
                                          right=right,
                                          bordertype=ui.comboBox.currentText(),
                                          value=value)

            self.perform_updates(img)


    def clicked_histogramequalization(self):
        if self.check_canvas() == None: return
        img = image_editor.histogram_equalization_bw(self.current)
        self.perform_updates(img)

    def clicked_image_histogram(self):
        if self.check_canvas() == None: return
        img = image_editor.image_histogram(self.current)
        # img[:,:,[0,3]] = img[:,:,[3,0]]
        print(img[:,:,0].max())
        print(img[:, :, 1].max())
        print(img[:, :, 2].max())
        print(img[:, :, 3].max())
        print(img.dtype)
        # img[:,:,3] = np.ones_like(img[:,:,3]) * 255

        win = QtWidgets.QDialog()
        ui_ = image_histogram.Ui_Dialog()
        ui_.setupUi(win)

        hist_ = QtGui.QImage(img.data,
                            img.shape[1],
                            img.shape[0],
                            img.shape[1]*4,
                            QtGui.QImage.Format_RGBX8888)

        hist = QtGui.QPixmap(hist_)
        ui_.label_hist.setPixmap(hist)
        win.show()
        win.exec_()

    def clicked_pyramid_blending_loadfiles(self):
        self.filenames_pyramidblend = self.get_filenames('Load three images: two for blending and one mask')
        while len(self.filenames_pyramidblend) != 3 and len(self.filenames_pyramidblend) != 0: #program continues if user selects none or 2
            error = 'Please load exactly three files.'
            QtWidgets.QMessageBox.warning(self, 'Error loading files', error)
            self.filenames_pyramidblend = self.get_filenames('Load three images: two for blending and one mask')

        if len(self.filenames_pyramidblend) == 0:
            return

        self.image0 = cv2.imread(self.filenames_pyramidblend[0])
        self.image1 = cv2.imread(self.filenames_pyramidblend[1])
        self.image2 = cv2.imread(self.filenames_pyramidblend[2])

        self.clicked_pyramid_blending()

    def clicked_pyramid_blending(self):
        Dialog = QtWidgets.QDialog()
        ui = pyramidblending_modified.Ui_Dialog()
        ui.setupUi(Dialog)
        ui.label_image0.setText('....' + self.filenames_pyramidblend[0][-30:])
        ui.label_image1.setText('....' + self.filenames_pyramidblend[1][-30:])
        ui.label_image2.setText('....' + self.filenames_pyramidblend[2][-30:])
        Dialog.show()
        result = Dialog.exec_()

        if result and (ui.comboBox_image0.currentText() == ui.comboBox_image1.currentText() or \
            ui.comboBox_image1.currentText() == ui.comboBox_image2.currentText() or \
                ui.comboBox_image2.currentText() == ui.comboBox_image0.currentText()):
            QtWidgets.QMessageBox.warning(self, 'Error', 'An image could either be Top, Bottom or Mask')
            return self.clicked_pyramid_blending()


        levels = int(ui.spinBox_levels.text())

        choice_dict = {ui.comboBox_image0.currentText(): self.image0,
                       ui.comboBox_image1.currentText(): self.image1,
                       ui.comboBox_image2.currentText(): self.image2}

        if result:
            img = image_editor.blending_pyramids(choice_dict['Top'], choice_dict['Bottom'], choice_dict['Mask'], levels)
            cv2.imwrite('saved_image.png',img)
            self.perform_updates(img)


    def get_filenames(self, msg):
        filenames, _ = QtWidgets.QFileDialog.getOpenFileNames(self, msg, '', )
        print(filenames)
        return filenames

    def clicked_alpha_blending(self):
        filenames = self.get_filenames('Load two images only')
        while len(filenames) != 2 and len(filenames) != 0: #program continues if user selects none or 2
            error = 'Please load exactly two files.'
            QtWidgets.QMessageBox.warning(self, 'Error loading files', error)
            filenames = self.get_filenames('Load two images only')

        if len(filenames) == 0:
            return

        image1 = cv2.imread(filenames[0])
        image2 = cv2.imread(filenames[1])

        if image1.shape != image2.shape:
            QtWidgets.QMessageBox.warning(self, 'Cannot blend files', 'Images are not the same shape.')
            return

        Dialog = QtWidgets.QDialog()
        ui = alphablending.Ui_Dialog_alphablending()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        if result:
            alpha= float(ui.doubleSpinBox_alpha.text())
            img = image_editor.blend_images(image1, image2, alpha)
            self.perform_updates(img.astype(np.uint8))



    def resize_image(self):
        if self.check_canvas() == None: return

        Dialog = QtWidgets.QDialog()
        ui = resize_ui.Ui_Dialog_resize()
        ui.setupUi(Dialog)
        Dialog.show()
        result = Dialog.exec_()

        h = ui.doubleSpinBox_height.text()
        w = ui.doubleSpinBox_width.text()

        if result:
            try:
                img = image_editor.resize_image(self.current, w, h)
            except:
                QtWidgets.QMessageBox.warning(self, "Can't resize image.", 'Please try again.')
                return
            self.perform_updates(img)

    def clicked_rotate_image(self):
        if self.check_canvas() == None: return
        img = image_editor.rotate_image(self.current)
        self.perform_updates(img)

    def clicked_apply_mask(self):
        if self.check_canvas() == None: return 1
        filename = self.get_filename('Load mask image')
        if len(filename) == 0:
            return

        mask = cv2.imread(filename, 0)

        if (self.current.shape[0], self.current.shape[1])  != (mask.shape[0], mask.shape[1]):
            QtWidgets.QMessageBox.warning(self, "Can't apply mask", 'Images are not the same shape.')
            return

        if len(self.current.shape) > 2:
            img = image_editor.mask_result_color(self.current, mask)
        else:
            img = image_editor.mask_result_bw(self.current, mask)
        self.perform_updates(img)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    mainwin = MainProgram()
    mainwin.show()

    app.exec_()
