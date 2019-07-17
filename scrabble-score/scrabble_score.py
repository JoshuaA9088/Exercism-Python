"""
Scoring Key

Letter                           Value
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
"""

ONE_POINT = ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]
TWO_POINT = ["D", "G"]
THREE_POINT = ["B", "C", "M", "P"]
FOUR_POINT = ["F", "H", "V", "W", "Y"]
FIVE_POINT = ["K"]
EIGHT_POINT = ["J", "X"]
TEN_POINT = ["Q", "Z"]

def generate_key():
    scoring = {}
    for i in ONE_POINT:
        scoring[i] = 1
    for i in TWO_POINT:
        scoring[i] = 2
    for i in THREE_POINT:
        scoring[i] = 3
    for i in FOUR_POINT:
        scoring[i] = 4
    for i in FIVE_POINT:
        scoring[i] = 5
    for i in EIGHT_POINT:
        scoring[i] = 8
    for i in TEN_POINT:
        scoring[i] = 10
    return scoring

def score(word):
    scoring = generate_key()
    sum = 0
    for i in word:
        sum += scoring[i.upper()]
    return sum
