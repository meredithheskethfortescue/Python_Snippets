#!/usr/bin/env python3
import sys

from PyQt5 import QtCore, QtGui

import design


class UiDialog(QtGui.QDialog):
    def __init__(self):
        super(UiDialog, self).__init__()

        # show Window minimizing/maximizing buttons
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, True)

        # setup ui layout
        self.ui = design.Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)  # create app
    dialog = UiDialog()  # create main dialog
    dialog.show()  # show main dialog
    sys.exit(app.exec())  # execute app
