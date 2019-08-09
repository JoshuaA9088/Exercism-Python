nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}

second_part = [
    "and a Partridge in a Pear Tree.",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing", 
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]

def recite(start_verse, end_verse):
    starting_verse = "On the {} day of Christmas my true love gave to me: ".format(nth[start_verse])
    if end_verse == 1:
        return [starting_verse + "a Partridge in a Pear Tree."]

    ending_verse = second_part[:end_verse]
    ending_verse.reverse()
    ending_verse = ", ".join(ending_verse)
    
    return [starting_verse + ending_verse]