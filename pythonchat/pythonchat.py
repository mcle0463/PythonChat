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
from functional.data_object import DataObject


my_name = "Greg McLeod"
data = DataObject()
menu_selection = -1
data.record_selection = 0
data.get_rows()
data.print_data(my_name)

while menu_selection != 0:
    print("\nMenu")
    print("1. Reload data set")
    print("2. Display full data set")
    print("3. Create new data record")
    print("4. Select a record")
    print("5. Display a record")
    print("6. Edit a record")
    print("7. Delete a record")
    print("0. Exit")

    menu_selection = int(input("\nMake a selection and press ENTER"), 10)
    if menu_selection == 1:
        data.get_rows()
    elif menu_selection == 2:
        data.print_data(my_name)
    elif menu_selection == 3:
        data.create_record()
    elif menu_selection == 4:
        data.select_record()
    elif menu_selection == 5:
        data.display_record()
    elif menu_selection == 6:
        data.edit_record()
    elif menu_selection == 7:
        data.delete_record()
    elif menu_selection == 0:
        print("Exiting...\n")
        break
    else:
        print("Invalid Selection")
