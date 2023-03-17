import pandas


def get_csv_data_as_list(file_path):
    df = pandas.read_csv(filepath_or_buffer=file_path, delimiter=';')
    return df.values.tolist()


def get_csv_data_as_list_of_tuple(file_path):
    df = pandas.read_csv(filepath_or_buffer=file_path, delimiter=';')
    list = []
    for i in df.index:
        list.append(tuple(df.loc[i]))
    return list
