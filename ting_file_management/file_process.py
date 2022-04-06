import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    path_file_list = []
    dict_process = {}
    data_list = txt_importer(path_file)
    number_of_rows = len(data_list)

    if len(instance) != 0:
        for path_name in path_file_list:
            if path_file == path_name:
                return len(instance)

    dict_process["nome_do_arquivo"] = path_file
    dict_process["qtd_linhas"] = number_of_rows
    dict_process["linhas_do_arquivo"] = data_list

    if len(instance) == 0:
        path_file_list.append(path_file)
        instance.enqueue(dict_process)

    print(dict_process, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        instance.dequeue()
        print(
            "Arquivo statics/arquivo_teste.txt removido com sucesso\n",
            file=sys.stdout
        )


def file_metadata(instance, position):
    dict_metadata = {}
    try:
        path_name = instance.search(position)
        dict_metadata["nome_do_arquivo"] = path_name["nome_do_arquivo"]
        dict_metadata["qtd_linhas"] = path_name["qtd_linhas"]
        dict_metadata["linhas_do_arquivo"] = path_name["linhas_do_arquivo"]
        print(dict_metadata, file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
