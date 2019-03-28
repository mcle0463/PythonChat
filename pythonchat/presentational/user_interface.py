import sys
from PyQt5 import QtCore, QtGui, QtWidgets
#from data_object import DataObject


class UserInterface(QtWidgets.QMainWindow):

    def __init__(self, controller):
        super().__init__()
        print(__name__)
        self.control = controller
        self.initUI()

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
        # reload button
        button = QtWidgets.QToolButton()
        button.setText(menu_option_titles[0])
        button.setObjectName('reload_button_clicked')
        button.clicked.connect(self.reload_button_clicked)
        button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.button_layout.addWidget(button)
        # display full data button
        button = QtWidgets.QToolButton()
        button.setText(menu_option_titles[1])
        button.setObjectName('display_full_data_button_clicked')
        button.clicked.connect(self.display_full_data_button_clicked)
        button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.button_layout.addWidget(button)
        # Create New record button
        button = QtWidgets.QToolButton()
        button.setText(menu_option_titles[2])
        button.setObjectName('create_new_record_button_clicked')
        button.clicked.connect(self.create_new_record_button_clicked)
        button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.button_layout.addWidget(button)
        # Select record button
        button = QtWidgets.QToolButton()
        button.setText(menu_option_titles[3])
        button.setObjectName('select_record_button_clicked')
        button.clicked.connect(self.select_record_button_clicked)
        button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.button_layout.addWidget(button)
        # Display single record button
        button = QtWidgets.QToolButton()
        button.setText(menu_option_titles[4])
        button.setObjectName('display_single_record_button_clicked')
        button.clicked.connect(self.display_single_record_button_clicked)
        button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.button_layout.addWidget(button)
        # edit record button
        button = QtWidgets.QToolButton()
        button.setText(menu_option_titles[5])
        button.setObjectName('edit_record_button_clicked')
        button.clicked.connect(self.edit_record_button_clicked)
        button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.button_layout.addWidget(button)
        # delete record button
        button = QtWidgets.QToolButton()
        button.setText(menu_option_titles[6])
        button.setObjectName('delete_record_button_clicked')
        button.clicked.connect(self.delete_record_button_clicked)
        button.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Preferred)
        self.button_layout.addWidget(button)
        # exit record button
        button = QtWidgets.QToolButton()
        button.setText(menu_option_titles[7])
        button.setObjectName('exit_pychat_button_clicked')
        button.clicked.connect(self.exit_pychat_button_clicked)
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
        self.setWindowTitle('Python Chat - Greg McLeod')
        self.show()

    def reload_button_clicked(self):
        sender = self.sender()
        self.status_label.setText("Currently selected: " + sender.text())
        self.statusBar().showMessage(sender.objectName() +
                                     ' was pressed')
        self.control.get_rows()
        self.output_textarea.setText(self.control.print_data())

    def display_full_data_button_clicked(self):
        sender = self.sender()
        self.status_label.setText("Currently selected: " + sender.text())
        self.statusBar().showMessage(sender.objectName() +
                                     ' was pressed')
        self.output_textarea.setText(self.control.print_data())
        # self.control.print_data()

    def create_new_record_button_clicked(self):
        sender = self.sender()
        self.status_label.setText("Currently selected: " + sender.text())
        self.statusBar().showMessage(sender.objectName() +
                                     ' was pressed')
        text, ok = QtWidgets.QInputDialog.getText(
            self, 'New Record', 'Enter record data:')
        if ok:
            self.control.create_record(str(text))
        self.output_textarea.setText(self.control.print_data())

    def select_record_button_clicked(self):
        dialog_text = "Enter a record to select between 1 and 10"
        record_selection, ok = QtWidgets.QInputDialog.getInt(
            self, 'Select Record', dialog_text)
        if ok:
            self.control.select_record(record_selection)
        self.output_textarea.setText(self.control.print_data())

    def display_single_record_button_clicked(self):
        sender = self.sender()
        self.status_label.setText("Currently selected: " + sender.text())
        self.statusBar().showMessage(sender.objectName() +
                                     ' was pressed')
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(self.control.display_one_record())
        msg.setStandardButtons(
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msg.setWindowTitle("Diplay record")
        msg.exec_()

    def edit_record_button_clicked(self):
        sender = self.sender()
        self.status_label.setText("Currently selected: " + sender.text())
        self.statusBar().showMessage(sender.objectName() +
                                     ' was pressed')
        text, ok = QtWidgets.QInputDialog.getText(
            self, 'Text Input Dialog', 'Enter record data:')
        if ok:
            self.control.edit_record(str(text))
        self.output_textarea.setText(self.control.print_data())

    def delete_record_button_clicked(self):
        sender = self.sender()
        self.status_label.setText("Currently selected: " + sender.text())
        self.statusBar().showMessage(sender.objectName() +
                                     ' was pressed')
        self.control.delete_record()
        self.output_textarea.setText(self.control.print_data())

    def exit_pychat_button_clicked(self):
        sender = self.sender()
        self.status_label.setText("Currently selected: " + sender.text())
        self.statusBar().showMessage(sender.objectName() +
                                     ' was pressed')
        self.control.quit_pythonchat()
