def abbreviate(words):
    ret = ""
    # Cleanup the string to make processing easier
    words = words.lower()
    words = words.replace("-", " ")
    words = words.replace("_", " ")
    for i in words.split():
        letter = i[0].upper()
        if letter.isalpha():
            ret += letter
    return ret