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
import asyncio
import websockets
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from model import data_object
from view import user_interface
from controller.controller import Controller

# main
app = QtWidgets.QApplication(sys.argv)
controller = Controller()
ex = user_interface.UserInterface(controller)
sys.exit(app.exec_())
