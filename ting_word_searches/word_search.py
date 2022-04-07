

def exists_word(word, instance):
    word_list = []
    word_dict = {}
    occurrences = []
    word_dict["palavra"] = word

    for position in range(len(instance)):
        path_name = instance.search(position)
        word_dict["arquivo"] = path_name["nome_do_arquivo"]

        for position, row in enumerate(path_name["linhas_do_arquivo"]):
            if word in row.lower():
                occurrences.append({"linha": position + 1})
    if occurrences == []:
        return []

    word_dict["ocorrencias"] = occurrences
    word_list.append(word_dict)

    return word_list


def ocorr(path_n, path_name, occurrences):
    for position, row in enumerate(path_n["linhas_do_arquivo"]):
        if path_name in row.lower():
            if row[-1:] != ".":
                row = row + "."
            occurrences.append({"linha": position + 1, "conteudo": row})
    return occurrences


def search_by_word(path_name, instance):
    word_list = []
    word_dict = {}
    occurrences = []
    word_dict["palavra"] = path_name

    for position in range(len(instance)):
        path_n = instance.search(position)
        word_dict["arquivo"] = path_n["nome_do_arquivo"]
        occurrences = ocorr(path_n, path_name, occurrences)

    if occurrences == []:
        return []

    word_dict["ocorrencias"] = occurrences
    word_list.append(word_dict)

    return word_list
