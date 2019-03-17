# test_create_record.py
import pytest


def test_create_record(data_object):
    assert len(data_object.records) == 10

    data_object.create_record("test record creation")
    assert len(data_object.records) == 11

    data_object.record_selection = 0
    data_object.delete_record()
