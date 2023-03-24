import config
from utilities import read_utils


class DataSource:
    test_invalid_data = [
        ('ken', 'john123', 'Invalid credential'),
        ('saul', 'peter123', 'Invalid credentials')
    ]

    test_invalid_data_csv = read_utils.get_csv_data_as_list(config.test_data_path+"test_invalid_data.csv")
    #
    test_add_valid_employee_data=read_utils.get_sheet_as_list(config.test_data_path+"orange_test_data.xlsx","test_add_valid_employee")
