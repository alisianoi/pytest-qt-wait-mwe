import pytest

from src.controller import Controller


def errored_callback():
    assert False

def stopped_callback():
    assert True

def test_controller(qtbot):

    controller = Controller()

    with qtbot.waitSignal(controller.stopped, timeout=5000) as blocker:
        controller.stopped.connect(stopped_callback)
        controller.errored.connect(errored_callback)

        controller.work()
