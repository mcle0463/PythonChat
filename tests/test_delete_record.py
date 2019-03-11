# test_delete_record.py
import pytest
from ChatApp import delete_record
from data_object import DataObject

def test_delete_record(data_object, record_selection):
    delete_record(data_object)
    assert len(data_object.records) < 10