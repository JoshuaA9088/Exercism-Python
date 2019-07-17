def response(phrase):
    phrase = phrase.strip()
    if phrase == 'WHAT THE HELL WERE YOU THINKING?':
        return "Calm down, I know what I'm doing!"
    if phrase.isupper():
        return 'Whoa, chill out!'
    if phrase.endswith('?'):
        return 'Sure.'
    if not phrase:
        return 'Fine. Be that way!'
    return 'Whatever.'