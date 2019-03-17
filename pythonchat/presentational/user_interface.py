import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import functional.data_object


class UserInterface(QtWidgets.QMainWindow):
    selected = -1

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        super().__init__()
        self.initUI()
        sys.exit(app.exec_())

    def initUI(self):
        # set main widget and main widget layout
        main_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QtWidgets.QVBoxLayout()
        main_widget.setLayout(main_layout)
        # set child layout objects
        self.button_layout = QtWidgets.QHBoxLayout()
        self.widget_layout = QtWidgets.QVBoxLayout()
        # Build Qpushuttons
        menu_option_titles = ["Reload data set", "Display full data set", "Create new data record",
                              "Select a record", "Display a record", "Edit a record", "Delete a record", "Exit"]
        for button_number in range(0, 8):
            button = QtWidgets.QToolButton()
            button.setText(menu_option_titles[button_number])
            button.setObjectName('Button%d' % button_number)
            button.clicked.connect(self.buttonClicked)
            button.setSizePolicy(
                QtWidgets.QSizePolicy.Preferred,
                QtWidgets.QSizePolicy.Preferred)
            self.button_layout.addWidget(button)

        self.status_label = QtWidgets.QLabel('No button clicked')
        self.output_textarea = QtWidgets.QTextEdit(
            "Messages will appear here...")
        self.output_textarea.setReadOnly(True)
        self.output_textarea.setMinimumSize(QtCore.QSize(40, 80))
        self.output_textarea.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)

        font = self.output_textarea.font()
        font.setFamily("Courier")
        font.setPointSize(10)
        # add buttons layout and status lable to widget
        self.widget_layout.addItem(self.button_layout)
        self.widget_layout.addWidget(self.status_label)
        self.widget_layout.addWidget(self.output_textarea)
        # add widget to main layout
        main_layout.addLayout(self.widget_layout)
        self.statusBar()
        self.setGeometry(500, 150, 350, 400)
        self.setWindowTitle('Python Chat')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.status_label.setText("Currently selected: " + sender.text())
        self.statusBar().showMessage(sender.objectName() +
                                     ' was pressed' + str(self.selected))
        if(sender.objectName() == "Button1"):
            self.selected = 0


# if __name__ == '__main__':

    # app = QtWidgets.QApplication(sys.argv)

    # ex = UserInterface()

    # - set layout of main container as vbox, then use window.addWidget(self.label, 0, 0, Qt.AlignTop)
