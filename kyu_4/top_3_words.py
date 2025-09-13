import re

def top_3_words(text):
    
    text_arr = re.sub(r"[^a-z']", " ", text)
    text_arr = text_arr.lower().split()
    text_arr = [x for x in text_arr if re.search(r"[a-z]", x)]

    matching_dict = {}

    for word in set(text_arr):
        matching_dict[word] = text_arr.count(word)

    max_idx = 0

    arr_len = len(list(matching_dict.items()))

    mathcing_list = list(matching_dict.items())

    for i in range(arr_len):
        max_idx = i

        for j in range(i+1, arr_len):
            if mathcing_list[max_idx][1] < mathcing_list[j][1]:
                max_idx = j

        mathcing_list[max_idx], mathcing_list[i] = mathcing_list[i], mathcing_list[max_idx]

    return [x[0] for x in mathcing_list[:3]]

