"""
Домашнее задание №1
Функции и структуры данных
"""
from math import sqrt


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = []
    for num in numbers:
        result.append(int(num)**2)
    return result


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def filter_numbers(*numbers, filtr):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    result = []
    if filtr == PRIME:
        result = list(filter(is_prime, numbers))
    elif filtr == EVEN:
        result = [i for i in numbers if i % 2 == 0]
    elif filtr == ODD:
        result = [i for i in numbers if i % 2 != 0]
    return result
