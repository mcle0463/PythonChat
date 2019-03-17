# test_delete_record.py
import pytest


def test_display_record(data_object):
    # print(len(data_object.records))
    assert len(data_object.records) == 10
