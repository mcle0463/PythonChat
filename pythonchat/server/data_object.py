# data_object
# Greg McLeod
# !/usr/bin/env python

"""Class that will instantiate a data object and
operate on data passed via the UI and csv files.
"""
__author__ = "Greg McLeod"
__version__ = "1.1"
__maintainer__ = "Greg McLeod"
__email__ = "mcle0463@algonquincollge.com"
__status__ = "Dev"

# module imports
import sys
import csv
import os


class DataObject(object):
    """A data object that can contain and manipulate csv file records
    """

    def __init__(self):
        """Creating a data object"""
        # self.input_file_path = os.path.abspath(
        # "PythonChat\pythonchat\\server\Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv")
        self.input_file_path = "Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv"
        self.records = list()
        self.header = ""
        self.record_selected = 0

    def get_rows(self):
        """Reads file and parses data to a list object"""
        self.records.clear()
        try:
            input_file = open(self.input_file_path, 'rt')
            reader = csv.reader(input_file)
            for i, row in enumerate(reader):
                if i >= 12:
                    break
                if i == 0:
                    self.data_header = row
                if i >= 2:
                    self.records.append(list(row))
            input_file.close()
        except OSError as e:
            print("I/O error({0}): {1}".format(e.errno, e.strerror))
            print(self.input_file_path)
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])

    def print_data(self):
        """Prints all records"""
        data_string = "Greg McLeod" + "\n\n"
        for record in self.records:
            data_string += str(record)
            data_string += "\n"
        return data_string

    def create_record(self, record_data):
        """Creates list record"""
        if self.record_selected != -1:
            self.records.insert(self.record_selected, record_data)
        else:
            print("please select a record")

    def select_record(self, selection):
        """Selects list record"""
        print("select record")
        if selection >= 1 and selection <= len(self.records):
                # break
            self.record_selected = selection
            print("Selected " + str(selection))

    def display_record(self):
        """displays currently selected list record"""
        if self.record_selected != -1:
            return str(self.records[self.record_selected])
        else:
            print("please select a record")

    def edit_record(self, record_data):
        """Edits currently selected list record"""
        if self.record_selected != -1:
            self.records[self.record_selected] = record_data
        else:
            print("please select a record")

    def delete_record(self):
        """Deletes currently selected list record"""
        if self.record_selected != -1:
            self.records.pop(self.record_selected)
            print(self.record_selected)
            print("has been deleted\n")
            self.record_selected = -1
        else:
            print("please select a record")
