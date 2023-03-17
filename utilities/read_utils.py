import pandas

"""Get csv into List of list"""


def get_csv_data_as_list(file_path):
    df = pandas.read_csv(filepath_or_buffer=file_path, delimiter=';')
    return df.values.tolist()


"""Get csv into List of tuple"""


def get_csv_data_as_list_of_tuple(file_path):
    df = pandas.read_csv(filepath_or_buffer=file_path, delimiter=';')
    list = []
    for i in df.index:
        list.append(tuple(df.loc[i]))
    return list


"""Get Excel Sheet into List of list"""


def get_sheet_as_list(file_path, sheet_name):
    df = pandas.read_excel(io=file_path, sheet_name=sheet_name)
    return df.values.tolist()
