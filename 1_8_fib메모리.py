def fib3(n):

    if n<=1:
        return n
    else:
        x1 = 0
        x2 = 1
        sum = 0
        for i in range(2, n+1):
            sum = x1 + x2
            x1 = x2
            x2 = sum
        return sum

for i in range(11):
    print(f'{fib3(i)}',end=' ')