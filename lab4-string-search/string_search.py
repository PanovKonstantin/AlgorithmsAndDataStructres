def naive(string, text):
    if len(text) < len(string) or string == "":
        return []
    positions = []
    for i in range(0, len(text) - len(string) + 1):
        j = 0
        while(j < len(string)):
            if text[i+j] != string[j]:
                break
            j += 1
        if j == len(string):
            positions.append(i)
    return positions


def boyer_moore(string, text):
    string_len = len(string)
    text_len = len(text)
    if text_len < string_len or string == "":  # Check if arguments are correct
        return []
    bad_char = {}   # Bad characters dictionary
    for string_index in range(string_len):
        bad_char[string[string_index]] = max(1, string_len - string_index - 1)
    positions = []
    text_index = 0
    while text_index <= text_len - string_len:
        string_index = string_len - 1
        while string_index >= 0 and string[string_index] == text[text_index + string_index]:
            string_index -= 1
        if string_index == -1:
            positions.append(text_index)
            if string_len + text_index >= text_len:
                text_index += 1
            else:
                text_index += string_len - bad_char.get(text[text_index + string_len], string_len - 1)
        else:
            text_index += bad_char.get(text[text_index + string_index], string_len - 1)  # Shift the pattern string
    return positions


if __name__ == '__main__':
    print(boyer_moore("test", "this is a test"))
