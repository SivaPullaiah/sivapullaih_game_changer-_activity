# problem 1
def nth_fib_rec(n):
    if n==0:
        return -1
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return nth_fib_rec(n-1)+nth_fib_rec(n-2)

# n = int(input())
# print(nth_fib_rec(n))

# problemm 2

def fib_seq(n):
    if n<=1:
        return n
    else:
        return fib_seq(n-1)+fib_seq(n-2)

# n = int(input())
# if n<=0:
#     print("Enter valid statement")
# else:
#     for fib in range(n):
#         print(fib_seq(fib), end=' ')

# problem 3
def sum_fib(n):
    if n<=1:
        return n
    else:
        return sum_fib(n-1)+sum_fib(n-2)

n = int(input())
sum=0
if n<=0:
    print("Enter valid input")
else:
    for num in range(n):
        sum+=sum_fib(num)

print(sum)