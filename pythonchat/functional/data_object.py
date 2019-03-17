# self
# Greg McLeod
# !/usr/bin/env python

"""Class that will instantiate a data object and 
operate on data passed via the UI and csv files.
"""
__author__ = "Greg McLeod"
__version__ = "1.0"
__maintainer__ = "Greg McLeod"
__email__ = "mcle0463@algonquincollge.com"
__status__ = "Dev"

# module imports
import sys
import csv


class DataObject(object):
    """A data object that can contain and manipulate csv file records
    """

    def __init__(self):
        """Creating a data object"""
        self.input_file_path = "pythonchat\functional\Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv"
        self.records = list()
        self.header = ""
        self.record_selected = -1

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

    def print_data(self, name):
        """Prints all records"""
        print(name + "\n")
        print(self.header)
        for record in self.records:
            print(record)
        # for index, row in enumerate(str_data):
        # count +=1
        # if count % 10 == 0:
        # if (index + 1) % 2 == 0:
        # if ((index + 1) % 2) == 0:
        #  print(index, row)
        #  'did ten'

    def create_record(self, record_data):
        """Creates list record"""
        if self.record_selected != -1:
            #t_record_data = input("Enter record data")
            self.records.insert(self.record_selected, record_data)
        else:
            print("please select a record")

    def select_record(self):
        """Selects list record"""
        while True:
            t_record_selection = int(
                input("Enter a record to select between 1 and " + str(len(self.records))), 10)
            if t_record_selection >= 1 and t_record_selection <= len(self.records):
                break
        print("Selected " + str(t_record_selection))
        self.record_selected = t_record_selection

    def display_record(self):
        """displays currently selected list record"""
        if self.record_selected != -1:
            print(self.records[self.record_selected])
        else:
            print("please select a record")

    def edit_record(self, record_data):
        """Edits currently selected list record"""
        if self.record_selected != -1:
            #t_record_data = input("Enter the records new value")
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
