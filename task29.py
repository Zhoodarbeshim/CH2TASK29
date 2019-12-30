def write_sentence():
    sentence = input("Enter some sentence: ")
    pun = sentence.replace(","," ")
    no_pun1 = pun.replace(".", " ")
    no_pun2 = no_pun1.replace("!", " ")
    no_pun3 = no_pun2.replace("?", " ")
    return no_pun3
print(write_sentence())