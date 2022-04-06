import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue



def process(path_file, instance):
    path_file_list = []
    dict_process = {}
    data_list = txt_importer(path_file)
    number_of_rows = len(data_list)

    if len(instance) != 0:
        for path_name in path_file_list:
            if path_file == path_name:
                return len(instance)

    if len(instance) == 0:
        instance.enqueue(1)
        path_file_list.append(path_file)

    dict_process["nome_do_arquivo"] = path_file
    dict_process["qtd_linhas"] = number_of_rows
    dict_process["linhas_do_arquivo"] = data_list

    print(dict_process, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
