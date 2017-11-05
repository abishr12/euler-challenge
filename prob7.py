# QUESTION: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import time
start_time = time.time()

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

def num_prime(number):
    i =1
    num_of_primes = 0
    while(True):
        if(i > 4):
            i += 2
        else:
            i += 1
        if(is_prime(i) != False or i == 2 or i ==3):
            #print(i)
            num_of_primes += 1
        if(num_of_primes == number):
            return i
            return False


print(num_prime(10001))
