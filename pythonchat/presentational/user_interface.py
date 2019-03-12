import sys
from PyQt5 import QtCore, QtGui, QtWidgets  # works for pyqt5


def setup_gui():
    """Generate a basic GUI."""
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.resize(500, 750)
    w.move(300, 300)
    w.setWindowTitle('Python Chat')
    w.show()
    sys.exit(app.exec_())

    # QtCore.QMetaObject.connectSlotsByName(Form)
