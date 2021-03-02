# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1190, 598)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(830, 550, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 30, 421, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.toggleswitch_preprocessing = ToggleSwitch(self.gridLayoutWidget)
        self.toggleswitch_preprocessing.setObjectName("toggleswitch_preprocessing")
        self.gridLayout.addWidget(self.toggleswitch_preprocessing, 0, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(529, 29, 641, 511))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout_2.addWidget(self.plainTextEdit_2, 0, 0, 1, 1)
        self.graphicsview_preview = PlotWidget(self.gridLayoutWidget_2)
        self.graphicsview_preview.setObjectName("graphicsview_preview")
        self.gridLayout_2.addWidget(self.graphicsview_preview, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "This is a pushbutton that is promoted to a custom ToggleSwitch widget.\n"
"\n"
"To do so a bit black magic is needed. Act like your python module is a C++ header file. \n"
"Here for example the module is called `toggle_switch.py` containing the class `ToggleSwitch`. Hence the correct parameters would be:\n"
"Promoted Class Name: ToggleSwitch\n"
"Header: toggle_switch.py\n"
"\n"
"Global Include will be ignored for python."))
        self.toggleswitch_preprocessing.setText(_translate("Dialog", "PushButton"))
        self.plainTextEdit_2.setPlainText(_translate("Dialog", "This is a PlotWidget that is promoted to a pyqtgraph.GraphicsView.\n"
""))

from pyqtgraph import PlotWidget
from toggle_switch import ToggleSwitch
