k=int(input("enter the number:"))
n=input("enter the item:")
for i in range(k):
    for j in range(i+1):
        print(f"{n}",end=" ")
    print()