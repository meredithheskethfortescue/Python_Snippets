import sys
import time

# todo: minimize imports
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow, QGridLayout, QTextEdit

try:
    from frontend.design_overlay_progress import Ui_Form
except ModuleNotFoundError:
    from design_overlay_progress import Ui_Form


class Worker(QThread):
    """Thread using the controller's functions to do processing on the model's data"""
    signal_idx = pyqtSignal(int)
    signal_msg = pyqtSignal(str)

    def __init__(self, controller):
        super(Worker, self).__init__()
        self._controller = controller

    def __del__(self):
        self.wait()

    def run(self):
        """Override"""
        self.signal_idx.emit(0)
        for idx, element in enumerate(self._controller.model.data_input):
            self.signal_msg.emit(f"Loading {element}")
            time.sleep(.2)

            self.signal_msg.emit(f"Processing {element}")
            time.sleep(.4)
            self._controller.processing_routine(idx)

            self.signal_idx.emit(idx + 1)
        self.signal_msg.emit("Finished")


class Model:
    def __init__(self):
        self._data_input = ['filename_alice.exmpl',
                            'filename_bob.exmpl',
                            'filename_cynthia.exmpl',
                            'filename_dave.exmpl',
                            'filename_eve.exmpl',
                            'filename_frank.exmpl']

        self.data_result = []

    @property
    def data_input(self):
        return self._data_input


class Controller:
    def __init__(self, model: Model):
        self.model = model

    def processing_routine(self, value):
        self.model.data_result.append(self.model.data_input[value])

    def start_processing(self, receiver):  # respondent is of type `Overlay`
        """Function to be connected (originally in overlay)"""
        # controller knows data length and should thus set the maximum
        receiver.maximum = len(self.model.data_input)

        # start a new thread
        self.worker = Worker(self)  # needs to be in init to preserve it from garbage collection
        self.worker.signal_idx.connect(receiver.signal_accept_idx)  # connect signal of thread with gui
        self.worker.signal_msg.connect(receiver.signal_accept_msg)  # connect signal of thread with gui
        self.worker.start()

        receiver.show()


class Overlay(QWidget):  # QWidget
    def __init__(self, parent=None, **kwargs):
        super(Overlay, self).__init__(parent, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(6, 9, 15, 240)))
        painter.end()

    @property
    def maximum(self):
        return self.ui.progressBar.maximum()

    @maximum.setter
    def maximum(self, value):
        self.ui.progressBar.setMaximum(value)

    def signal_accept_idx(self, idx: int):
        self.ui.progressBar.setValue(idx)
        self.ui.label_progress.setText(f"{idx} / {self.maximum}")

        if idx >= self.maximum:
            time.sleep(.4)
            self.hide()

    def signal_accept_msg(self, msg: str):
        self.ui.label_message.setText(msg)


class View(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        widget = QWidget(self)
        self.editor = QTextEdit()
        self.editor.setPlainText("0123456789" * 100)
        layout = QGridLayout(widget)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        button = QPushButton("Run")
        layout.addWidget(button, 1, 1, 1, 1)
        self.setCentralWidget(widget)

        self.overlay = Overlay(self.centralWidget())
        self.overlay.hide()

        # init MVC
        self.model = Model()
        self.controller = Controller(self.model)

        button.clicked.connect(lambda: self.controller.start_processing(self.overlay))

    def resizeEvent(self, event):
        self.overlay.resize(event.size())
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = View()
    window.show()
    sys.exit(app.exec_())
