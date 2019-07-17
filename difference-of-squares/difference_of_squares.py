import math

def square_of_sum(count):
    numbers = []
    for x in range (count, 0, -1):
        numbers.append(x)
    numberSum = sum(numbers)
    numberSq = math.pow(numberSum, 2)
    return numberSq
    pass


def sum_of_squares(count):
    numbers = []
    for x in range (count, 0, -1):
        numbers.append(x**2)
    numberSum = sum(numbers)
    return numberSum
    pass

def difference(count):
    diff = square_of_sum(count) - sum_of_squares(count)
    return diff
    pass