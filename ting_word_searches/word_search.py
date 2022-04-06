from mimetypes import suffix_map


def exists_word(word, instance):
    word_list = []
    word_dict = {}
    occurrences = []
    count = 0
    word_dict["palavra"] = word

    for position in range(len(instance)):
        path_name = instance.search(position)
        word_dict["arquivo"] = path_name["nome_do_arquivo"]

        for position, row in enumerate(path_name["linhas_do_arquivo"]):
            if word in row.lower():
                occurrences.append({"linha": position + 1})
                count += 1
        
    word_dict["ocorrencias"] = occurrences
    word_list.append(word_dict)

    return word_list

def search_by_word(path_name, instance):
    """Aqui irá sua implementação"""
