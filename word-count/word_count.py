def word_count(phrase):
    words = phrase.strip().replace("\n", " ").split(" ")
    words = filter(None, words)
    count = {}
    for word in words:
        count[word] = 1 if word not in count else count [word] + 1
    return count