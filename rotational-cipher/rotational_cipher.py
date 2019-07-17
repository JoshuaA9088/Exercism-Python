def rotate(text, key):
    word = []
    textList = list(text)
    # text = list(text)
    for x in range (len(textList)):
        ordText = ord(textList[x])
        ordText = ordText + key
        intText = chr(ordText)
        word.append(intText)
    word = ''.join(word)
    return word
    pass