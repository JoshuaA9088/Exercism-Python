def is_valid(isbn):
    sum = 0
    multiplier = 10
    isbn = isbn.replace("-", "")
    isbn = list(isbn)
    if len(isbn) != 10: return False
    for i in range(len(isbn)):
        try:
            sum += int(isbn[i]) * multiplier
        except:
            if i == len(isbn) - 1 and isbn[i] == "X":
                sum += 10 * multiplier
            else:
                return False
        multiplier -= 1
    return (sum % 11 == 0)