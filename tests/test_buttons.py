import pytestqt

from PyQt5 import QtCore, QtGui, QtWidgets


def test_buttons(qtbot):
    from pythonchat.view.user_interface import UserInterface
    from pythonchat.controller.controller import Controller
    controller = Controller()
    widget = UserInterface(controller)
    qtbot.addWidget(widget)
   # qtbot.mouseClick(widget.size, QtCore.Qt.LeftButton)
  # https://doc.qt.io/qt-5/qsize.html#QSize
    print(widget.size().height())
    assert widget.size().height() == 400
    assert widget.size().width() == 709
    # assert widget.greet_label.text() == "Hello!"
