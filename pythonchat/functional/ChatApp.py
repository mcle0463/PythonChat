# pythonchat
# Greg McLeod
# !/usr/bin/env python

"""Function definitions that will manipulate data
passed via the UI and csv files.
"""
__author__ = "Greg McLeod"
__version__ = "1.2."
__maintainer__ = "Greg McLeod"
__email__ = "mcle0463@algonquincollge.com"
__status__ = "Dev"

# module imports
import sys
import csv
from data_object import DataObject


def get_rows(data_object):
    """
    Reads file and parses data to a list object

    Parameters:
        data_object

    Returns:
        None

    """
    data_object.records.clear()
    try:
        input_file = open(data.input_file_path, 'rt')
        reader = csv.reader(input_file)
        for i, row in enumerate(reader):
            if i >= 12:
                break
            if i == 0:
                data_object.data_header = row
            if i >= 2:
                data_object.records.append(list(row))

        input_file.close()
    except OSError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])


def print_data(data_object, name):
    """
    Prints all records

    Parameters:
        data_object

    Returns:
        None

    """
    print(name + "\n\n")
    print(data_object.header)
    for record in data.records:
        print(record)
    # for index, row in enumerate(str_data):
    # count +=1
    # if count % 10 == 0:
    # if (index + 1) % 2 == 0:
    # if ((index + 1) % 2) == 0:
    #  print(index, row)
    #  'did ten'


def create_record(data_object):
    """
    Creates list record

    Parameters:
        data_object

    Returns:
        None

    """
    if record_selected:
        t_record_data = input("Enter record data")
        data.records.insert(record_selection, t_record_data)
    else:
        print("please select a record")


def select_record(data_object):
    """
    Selects list record

    Parameters:
        data_object

    Returns:
        None

    """
    while True:
        t_record_selection = int(
            input("Enter a record to select between 1 and " + str(len(data.records))), 10)
        if t_record_selection >= 1 and t_record_selection <= len(data_object.records):
            break
    print("Selected " + str(t_record_selection))
    return t_record_selection


def display_record(data_object):
    """
    displays currently selected list record

    Parameters:
        data_object

    Returns:
        None

    """
    if record_selected:
        print(data_object.records[record_selection])
    else:
        print("please select a record")


def edit_record(data_object):
    """
    Edits currently selected list record

    Parameters:
        data_object

    Returns:
        None

    """
    if record_selected:
        t_record_data = input("Enter the records new value")
        data_object.records[record_selection] = t_record_data
    else:
        print("please select a record")


def delete_record(data_object):
    """
    Deletes currently selected list record

    Parameters:
        data_object

    Returns:
        None

    """
    if record_selected:
        print(record_selection)
        data_object.records.pop(record_selection)
    else:
        print("please select a record")


my_name = "Greg McLeod"
data = DataObject()
menu_selection = -1
record_selection = 0
record_selected = False
get_rows(data)
print_data(data, my_name)

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
        get_rows(data)
    elif menu_selection == 2:
        print_data(data, my_name)
    elif menu_selection == 3:
        create_record(data)
    elif menu_selection == 4:
        record_selection = select_record(data)
        record_selected = True
    elif menu_selection == 5:
        display_record(data)
    elif menu_selection == 6:
        edit_record(data)
    elif menu_selection == 7:
        delete_record(data)
    else:
        print("Invalid Selection")
