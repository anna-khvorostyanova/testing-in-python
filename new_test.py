import math


def add(a, b):
    return a + b


def division(a, b):
    if b == 0:
        return "Division to zero is not possible"
    return a / b


def test_add_positive_numbers():
    assert add(5, 9) == 14


def test_add_negative_numbers():
    assert add(-5, -9) == -14


def test_division_to_zero():
    assert division(1, 0) == "Division to zero is not possible"


def test_sqrt_works():
    assert math.sqrt(5) == 2
    assert math.sqrt(4) == 2



# Подготавливаем программу к тестированию
# 1. Обернуть код программы в функцию
# 2. Вернуть значения с помощью return

def find_max_min_value(a_list):
    max_value = a_list[0]
    min_value = a_list[0]
    # если используются сами значения, el (element), item, number
    for item in a_list:
        if item<min_value:
            min_value = item
        if item>max_value:
            max_value = item
    return max_value, min_value

# 3. Написать тесты
def test_positive_path_max_min_value():
    assert find_max_min_value([5, 6, 3, 1, 2, 3, 4, 5, 1, 2, 5]) == (6, 1)
