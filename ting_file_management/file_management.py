def txt_importer(path_file):
    data_list = []
    with open(path_file) as file:
        for row in file:
            new_row = row[:-1]
            if len(row) > 2:
                data_list.append(new_row)
    return data_list
