#1)
input=input("enter the number:")
c=[]
for i in input:
    if int(i)==1:
        c.append("one")
    elif int(i)==2:
        c.append("two")
    elif int(i) == 3:
        c.append("Three")
    elif int(i) == 4:
        c.append("four")
    elif int(i)==5:
        c.append("five")
    elif int(i)==6:
        c.append("six")
    elif int(i)==7:
        c.append("seven")
    elif int(i)==8:
        c.append("eight")
    elif int(i)==9:
        c.append("nine")

for i in c:
    print(i,end=" ")
print()

#2)
'''#3)
print("1.insert an element")
print("2.delete an element")
print("3.exit")
k=int(input("enter the number from (1-3):"))
a=[]
try:
    while k==1:
        p=int(input("enter a no of elements:"))
        for i in range(p):
            c=input(("enter the element to append:"))
            a.append(c)
        print(a)
        break
    while k==2:
        print(a)
        p=input("enter the elements to pop from th list:")
        a.pop(p)
        print(a)
        break
    while k==3:
        exit()
except ValueError:
    print("enter the value b/w 1 to 3")
    '''
#3

while True:
    print("\nStock Logging System")
    print("1. Insert the element ")
    print("2. Stock Out")
    print("3. Exit")
#4)
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

#6
string=input("enter the string:")
k=string.split(" ")

c=[]
for i in range(len(k)):
    c.append(len(k[i]))
s=max(c)

for i in k:
    if s==len(i):
        print(i)

#7
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]


for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for r in result:
   print(r)
