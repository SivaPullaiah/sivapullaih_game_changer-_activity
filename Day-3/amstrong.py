num = int(input("number: "))
len_gth = len(str(num))
temp = num
amstrong = 0
while num:
    rem = num%10
    # print(rem)
    amstrong = amstrong +(rem**len_gth)
    num = num//10
    # print(amstrong)
if temp == amstrong:
    # print(temp)
    print("amstrong")
else:
    print("Not a amstrong")