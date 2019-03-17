# test_delete_record.py
import pytest


def test_delete_record(data_object):
    # print(len(data_object.records))
    assert len(data_object.records) == 10

    data_object.delete_record()
    # print(len(data_object.records))
    assert len(data_object.records) == 9

    data_object.record_selection = 1
    print(data_object.record_selection)
    data_object.delete_record()
   # print(len(data_object.records))
    #assert len(data_object.records) == 8
