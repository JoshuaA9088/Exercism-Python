def is_armstrong_number(number):
    finalNums = []
    digits = [int(x) for x in str(number)]
    for x in digits:
        newNum = x ** len(digits)
        finalNums.append(newNum)
    finalNums = sum(finalNums)
    if finalNums == number:
        return True
    else:
        return False
