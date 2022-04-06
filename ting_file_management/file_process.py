import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    data_list = txt_importer(path_file)
    number_of_rows = len(data_list)

    dict_process = {}

    dict_process["nome_do_arquivo"] = path_file
    dict_process["qtd_linhas"] = number_of_rows
    dict_process["linhas_do_arquivo"] = data_list

    print(dict_process, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
