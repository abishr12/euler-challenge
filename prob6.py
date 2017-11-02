# QUESTION: The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(number):
    sum = 0
    sum_sq = 0
    for num in range(1, number+1):
        sum += num
        sum_sq += (num*num)
    return (sum*sum)-sum_sq

# print(sum_of_squares(100))

def square_of_sums(number):
    sum = 0
    for num in range(1,number+1):
        sum += num
    total = sum * sum
    return total

print(sum_of_squares(100))
