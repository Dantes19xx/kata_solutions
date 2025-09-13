def spin_words(sentence):
    sen_arr = sentence.split()
    res_arr = []

    for i in range(len(sen_arr)):
        if len(sen_arr[i]) < 5:
            res_arr.append(sen_arr[i])
        else:
            res_arr.append(sen_arr[i][::-1])

    return " ".join(res_arr)
