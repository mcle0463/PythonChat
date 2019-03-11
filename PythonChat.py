import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def setup_gui(Form):
    """Generate a GUI.
    """
    Form.setObjectName("Form")
    Form.resize(400, 300)
    pushButton = QtWidgets.QPushButton(Form)
    pushButton.setGeometry(QtCore.QRect(70, 50, 75, 23))
    pushButton.setObjectName("pushButton")

    # QtCore.QMetaObject.connectSlotsByName(Form)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_widget = QtWidgets.QWidget()
    setup_gui(Form)
    Form.show()
    sys.exit(app.exec_())
