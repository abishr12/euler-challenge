def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

# is_palindrome(353)
# print(digits)

palindromes =[]

def palindrome_product():
    for numOne in range(100, 1000):
        for numTwo in range(100, 1000):
            product = numOne*numTwo
            if(is_palindrome(product) == True):
                palindromes.append(product)
    print(max(palindromes))


palindrome_product()
