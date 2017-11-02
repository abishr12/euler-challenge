# QUESTION: A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.



def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


palindromes =[]

def palindrome_product():
    for numOne in range(100, 1000):
        for numTwo in range(100, 1000):
            product = numOne*numTwo
            if(is_palindrome(product) == True):
                palindromes.append(product)
    print(max(palindromes))


palindrome_product()
