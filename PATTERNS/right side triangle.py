k=int(input("enter the number:"))
n=input("enter the item:")
for i in range(k):
    for j in range(1,k):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()