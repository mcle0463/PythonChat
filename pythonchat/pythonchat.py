# pythonchat
# Greg McLeod
# !/usr/bin/env python
"""main
"""
__author__ = "Greg McLeod"
__version__ = "1.3"
__maintainer__ = "Greg McLeod"
__email__ = "mcle0463@algonquincollge.com"
__status__ = "Dev"

# module imports
import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from functional import data_object
from presentational import user_interface

# TODO: Controller in separate class


class Controller:
    def __init__(self, data_obj):
        self.data = data_obj

    def get_rows(self):
        # reload data
        print("Button1\n")
        self.data.get_rows()

    def print_data(self):
        # update text area
        print("Button2\n")
        return self.data.print_data()

    def create_record(self, record_data):
        # create a new record
        print("Button3\n")
        self.data.create_record(record_data)

    def select_record(self, record_selection):
        # select a new record
        self.data.select_record(record_selection)

    def display_one_record(self):
        # show only one record
        print("Button5\n")
        return self.data.display_record()

    def edit_record(self, record_data):
        # edit a record
        print("Button6\n")
        self.data.edit_record(record_data)

    def delete_record(self):
        # delete a record
        print("Button7\n")
        self.data.delete_record()

    def quit_pythonchat(self):
        # quit - can remove this function
        print("Exiting...\n")


# main
app = QtWidgets.QApplication(sys.argv)
data = data_object.DataObject()
data.record_selection = 0
data.get_rows()
data.print_data()
controller = Controller(data)
ex = user_interface.UserInterface(controller)
sys.exit(app.exec_())
