def is_isogram(string):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace("-", "")
    list_of_chars = list(string)
    return len(list_of_chars) == len(set(list_of_chars))