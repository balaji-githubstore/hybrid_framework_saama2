import pandas
from utilities import read_utils


class DataSource:
    test_invalid_data = [
        ('ken', 'john123', 'Invalid credential'),
        ('saul', 'peter123', 'Invalid credentials')
    ]

    test_invalid_data_csv = read_utils.get_csv_data_as_list("../test_data/test_invalid_data.csv")
