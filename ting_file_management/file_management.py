import sys


def txt_importer(path_file):
    data_list = []
    if path_file[len(path_file)-4:] != ".txt":
        print("Formato inválido", file=sys.stderr)
    if path_file[
        len(path_file)-4:
    ] == ".txt" and path_file == "statics/arquivo_nao_existe.txt":
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        with open(path_file) as file:
            for row in file:
                new_row = row[:-len("\n")]
                if len(row) > 2:
                    data_list.append(new_row)
    return data_list
