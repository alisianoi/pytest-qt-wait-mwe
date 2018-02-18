#!/usr/bin/env python

import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from src.controller import Controller

class TMainWidget(QWidget):

    stopped = pyqtSignal()

    def __init__(self, parent: QWidget=None):

        super().__init__(parent)

        self.counter = 0

        self.setup_controller()
        self.controller.work()

    def setup_controller(self):
        self.controller = Controller(self)
        self.controller.stopped.connect(self.handle_stopped)

    def handle_stopped(self):

        self.counter += 1

        print(f"Counter (for python): {self.counter}")


class TMainWindow(QMainWindow):

    def __init__(self, parent: QWidget=None):

        super().__init__(parent)

        self.main_widget = TMainWidget(self)

        self.setCentralWidget(self.main_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = TMainWindow()
    main_window.show()

    sys.exit(app.exec())
