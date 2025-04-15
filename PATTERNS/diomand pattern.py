'''
k=int(input("enter the number:"))
for i in range(k-1):
    for j in range(i,k):
        print(' ',end='')
    for j in range(i):
        print('*',end='')
    for j in range(i+1):
        print("*",end='')
    print()
for i in range(k):
    for j in range(i+1):
        print(' ',end='')
    for j in range(i,k-1):
        print('*',end='')
    for j in range(i,k):
        print("*",end='')
    print()
'''
n=int(input("enter the number:"))
for i in range(1,n+1):
    if i==1:
        print("*")
    else:
        print(' '*(n-1), end='')
        print("*"*(2*i),end="")
        print()
for i in range(n-1,0,-1):
    print(" "*(n-1),end="")
    print("*"*(2*i),end=" ")
    print()