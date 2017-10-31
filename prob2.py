def fibonacci(n):
    if(n <= 2):
        return n

    else:
        return(fibonacci(n-1) + fibonacci(n-2))

limit = 4000000
i = 0
answer = 0
while fibonacci(i)<= limit:
    if fibonacci(i)%2 == 0:
        answer += fibonacci(i)
    i+=1

print(answer)
