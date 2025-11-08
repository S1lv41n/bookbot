def get_num_words (filepath):
    with open (filepath) as file:
        file_contents = (file.read()).split()
        counter = 0
        for word in file_contents:
            counter += 1
    return counter

def get_num_char (filepath):
    with open (filepath) as file:
        file_contents = (file.read()).lower()
        char_dict = {}
        for char in file_contents:
            if char in char_dict:
                char_dict[f"{char}"] += 1
            else:
                char_dict[f"{char}"] = 1
        dict_list = []
        for ch, count in char_dict.items():
            if not ch.isalpha():
                continue
            pair = {"char": ch, "num": count}
            dict_list.append(pair)
    return char_dict, dict_list

def sort_dict (dictionary):
    return dictionary["num"]