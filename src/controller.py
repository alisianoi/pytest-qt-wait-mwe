from random import randint

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Worker(QObject):

    started = pyqtSignal()
    stopped = pyqtSignal()
    errored = pyqtSignal()

    def __init__(self, parent: QObject=None):

        super().__init__(parent)

    def work(self):
        self.started.emit()

        QThread.currentThread().sleep(randint(0, 3))

        self.stopped.emit()


class Wrapper(QRunnable):

    def __init__(self, worker: Worker):

        super().__init__()

        self.worker = worker

    def run(self):
        self.worker.work()


class Controller(QObject):

    started = pyqtSignal()
    stopped = pyqtSignal()
    errored = pyqtSignal()

    def __init__(self, parent: QObject=None):

        super().__init__(parent)

        self.threadpool = QThreadPool()

    def work(self):
        worker = Worker(self)

        worker.started.connect(self.fn_started)
        worker.stopped.connect(self.fn_stopped)
        worker.errored.connect(self.fn_errored)

        self.threadpool.start(Wrapper(worker))

    @pyqtSlot()
    def fn_started(self):
        print('fn_started')

        self.started.emit()

    @pyqtSlot()
    def fn_stopped(self):
        print('fn_stopped')

        self.stopped.emit()

    @pyqtSlot()
    def fn_errored(self):
        print('fn_errored')

        self.errored.emit()
