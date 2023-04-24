def add():
    try:
        a=int(input())
    except ValueError as err:
        print(err)
    try:
        b=int(input())
    except ValueError as err:
        print(err)
    try:
        print(a+b)
    except Exception as e:
        print(e,"siva")

# add()

def test(*d):
    #print(c)
    for each in d:
        print(each)
# test(1,2)

def fib(n):
    first=0
    second=1
    if n==0:
        print("Invalid input")
        return None
    for each in range(n):
        if each==0:
            print(0)
        elif each==1:
            print(1)
        else:
            temp=first+second
            print(temp)
            first=second
            second=temp

try:
    fib(int(input()))
except Exception as e:
    print(e)
