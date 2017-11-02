# QUESTION: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from functools import reduce

num_factors = [1]

# Produces all the factors of the number
def use_factorization(number):
    print(number)
    for test in range(2, number+1):
        if(number % test == 0):
            num_factors.append(test)
            return use_factorization(int(number/test))

#Produces array of numbers that would be multiplied together to solve for the lowest number divisible by all numbers 1-20
def cleanDiv():
    total = reduce(lambda x, y: x*y, num_factors)
    print("Total is--> " + str(total))
    for n in range(20,2,-1):
        if (total % n != 0):
            for num in num_factors:
                print("Num is--> "+str(n))
                if(n % num == 0):
                    n = n // num
            use_factorization(n)
            return cleanDiv()

cleanDiv()
# print(num_factors)
# print(reduce(lambda x, y: x*y, num_factors))
