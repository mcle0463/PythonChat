# test_editrecord.py
import pytest


def test_edit_record(data_object):
    assert len(data_object.records) == 10

    test_record = data_object.records[data_object.record_selected]
    assert len(test_record) != ""

    data_object.edit_record("test input")
    assert data_object.records[data_object.record_selected] == "test input"
