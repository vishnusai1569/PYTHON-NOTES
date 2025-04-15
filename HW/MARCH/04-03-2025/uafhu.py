a=[10,20,15,12,18]
k=int(input("enter the number to be searched :"))
for i in range(len(a)):
    if k==a[i]:
        print("found",i)
        break
    else:
        print("not found")