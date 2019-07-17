def find_anagrams(word, candidates):
    true = []
    word = word.lower()
    for x in range (len(candidates)):
        if word.lower() == candidates[x].lower():
            return []
        sortCandidates = sorted(candidates[x].lower())
        sortWords = sorted(word)
        if sortWords == sortCandidates:
            true.append(candidates[x])
    return true