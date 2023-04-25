def nth_fib_rec(n):
    if n==0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fib_rec(n-1)+fib_rec(n-2)

n = int(input())
print(nth_fib_rec(n))