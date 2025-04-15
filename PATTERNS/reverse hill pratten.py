k=int(input("enter the number:"))
for i in range(k):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,k-1):
        print('*',end='')
    for j in range(i,k):
        print("*",end='')
    print()