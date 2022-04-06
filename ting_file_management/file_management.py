import sys

def txt_importer(path_file):
    data_list = []

    if path_file[len(path_file)-4:] != ".txt":
        print("Formato inválido", file=sys.stderr)

    with open(path_file) as file:
        for row in file:
            new_row = row[:-1]
            if len(row) > 2:
                data_list.append(new_row)

    return data_list
