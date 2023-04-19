rows = int(input("Enter rows count: "))
for row_no in range(1,rows+1):
    for col_no in range(1,row_no+1):
        print(col_no, end=' ')
    print()