def is_substring(word_a: str, word_b: str):
    rotations = []
    # rotate second word
    for i in range(len(word_b)):
        temp = ""
        for j in range(i, len(word_b)):
            temp += word_b[j]
        for k in range(0, i):
            temp += word_b[k]
        rotations.append(temp)
   # print(rotations)
    return word_a in rotations


print(is_substring('waterbottle', 'erbottlewat'))
