import pytest

#  Fixture for data object used across multiple tests
@pytest.fixture(scope="module")
def data_object():
    from pythonchat.functional.data_object import DataObject
    data = DataObject()
    data.record_selected = 0
    data.input_file_path = "Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv"
    data.get_rows()

    return data
    # return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
