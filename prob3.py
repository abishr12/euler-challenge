import time
start_time = time.time()




# Checks if the number is prime
def is_prime(number):
    if (even_num(number) == True):
        return False
    if (divisible_by_three(number) == True):
        return False
    else:
        i=2
        while(i<number):
            if(number%i == 0):
                return False
                break
            i += 1
    #print("--- %s seconds ---" % (time.time() - start_time))
    return True


# If the number is even then it can't be prime
def even_num(number):
    if(int(repr(number)[-1]) % 2 == 0):
        return True
    return False

# If the sum of all the digits of the number is divisible by three, then the number is divisible by three, hence not prime
def divisible_by_three(n):
    tot=0
    while(n>0):
        # dig=n%10
        tot=tot+(n%10)
        n=n//10
    if(tot%3 == 0):
        return True
    else:
        return False


# Runs the number through factorization but only stores the numbers that are prime into the array
prime_factors = []
def highest_prime(number):
    #print(number)
    for test in range(2, number+1):
        if(number % test == 0 and is_prime(test) != False ):
            if(test not in prime_factors):
                prime_factors.append(test)
            return highest_prime(int(number/test))







highest_prime(600851475143)

# Produces the highest factor in the array
print (max(prime_factors))
print("--- %s seconds ---" % (time.time() - start_time))


# def use_factorization(number):
#     print(number)
#     for test in range(2, number):
#         if(number % test == 0):
#             numFactors.append(test)
#             return use_factorization(int(number/test))
