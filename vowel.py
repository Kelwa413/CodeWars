def get_count(sentence):
    total = 0
    sentence = sentence.lower()
    for i in sentence:
        if i in ('a', 'e', 'i', 'o', 'u'):
            total +=1 
    return total