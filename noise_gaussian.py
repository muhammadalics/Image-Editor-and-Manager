# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noise_gaussian.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_gaussian_noise(object):
    def setupUi(self, Dialog_gaussian_noise):
        Dialog_gaussian_noise.setObjectName("Dialog_gaussian_noise")
        Dialog_gaussian_noise.resize(400, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_gaussian_noise.sizePolicy().hasHeightForWidth())
        Dialog_gaussian_noise.setSizePolicy(sizePolicy)
        Dialog_gaussian_noise.setMinimumSize(QtCore.QSize(400, 100))
        Dialog_gaussian_noise.setMaximumSize(QtCore.QSize(400, 100))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_gaussian_noise)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog_gaussian_noise)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 20, 114, 53))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_channel = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_channel.setObjectName("comboBox_channel")
        self.comboBox_channel.addItem("")
        self.comboBox_channel.addItem("")
        self.comboBox_channel.addItem("")
        self.comboBox_channel.addItem("")
        self.gridLayout.addWidget(self.comboBox_channel, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.doubleSpinBox_sigma = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBox_sigma.setSingleStep(0.25)
        self.doubleSpinBox_sigma.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_sigma.setProperty("value", 1.0)
        self.doubleSpinBox_sigma.setObjectName("doubleSpinBox_sigma")
        self.gridLayout.addWidget(self.doubleSpinBox_sigma, 1, 1, 1, 1)

        self.retranslateUi(Dialog_gaussian_noise)
        self.buttonBox.accepted.connect(Dialog_gaussian_noise.accept)
        self.buttonBox.rejected.connect(Dialog_gaussian_noise.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_gaussian_noise)

    def retranslateUi(self, Dialog_gaussian_noise):
        _translate = QtCore.QCoreApplication.translate
        Dialog_gaussian_noise.setWindowTitle(_translate("Dialog_gaussian_noise", "Gaussian Noise"))
        self.label.setText(_translate("Dialog_gaussian_noise", "Channel"))
        self.comboBox_channel.setItemText(0, _translate("Dialog_gaussian_noise", "Red"))
        self.comboBox_channel.setItemText(1, _translate("Dialog_gaussian_noise", "Green"))
        self.comboBox_channel.setItemText(2, _translate("Dialog_gaussian_noise", "Blue"))
        self.comboBox_channel.setItemText(3, _translate("Dialog_gaussian_noise", "N/A"))
        self.label_2.setText(_translate("Dialog_gaussian_noise", "Sigma"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_gaussian_noise = QtWidgets.QDialog()
    ui = Ui_Dialog_gaussian_noise()
    ui.setupUi(Dialog_gaussian_noise)
    Dialog_gaussian_noise.show()
    sys.exit(app.exec_())