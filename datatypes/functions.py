# TAKES IN INPUT THEN GIVES AN OUTPUT
import math


def adds_two(number):
    return number + 2


my_number = 10

print(adds_two(my_number))


def calculate_quadratic_equation(a, b, c):
    return (-b + (4 * a * c)) / 2 * a


def calculate_hypotenuse(side_1, side_2):
    return math.sqrt((side_1 * side_1) + (side_2 * side_2))


def calculate_average(list_of_numbers):
    return sum(list_of_numbers) / len(list_of_numbers)


print(calculate_quadratic_equation(2, 3, 1))

my_list = [1, 2, 3]
print(calculate_average(my_list))
