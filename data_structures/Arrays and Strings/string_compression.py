
def string_compression(word: str):
    result = ""
    curr_char = word[0]
    curr_char_count = 1
    for index in range(1, len(word)):
        if word[index] == word[index-1]:
            curr_char_count += 1
            continue
        else:
            result += curr_char
            result += str(curr_char_count)
            curr_char = word[index]
            curr_char_count = 1
    result += curr_char
    result += str(curr_char_count)

    return result if len(result) < len(word) else word


string_compression('aabcccccaaa')
