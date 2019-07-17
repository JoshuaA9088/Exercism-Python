def is_pangram(sentence):
    x = set([])
    sentence = sentence.lower()
    for letter in sentence:
        if letter.isalpha():
            x.add(letter)
    return (len(x) == 26)
