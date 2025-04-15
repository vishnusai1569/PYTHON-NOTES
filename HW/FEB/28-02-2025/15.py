a=int(input("Enter 1st input:"))
b=int(input("Enter 2nd input:"))
c=int(input("Enter 3rd input:"))
if a>b>c:
    max=a
    print("max=",a)
elif b>a>c:
    max=b
    print('max=',b)
else:
    max=c
    print('max=',c)
if a<b<c:
    min=a
    print('min=',a)
elif b<a<c:
    min = b
    print("min=",b)
else:
    min = c
    print("main=",c)

print(f'mid ={(a+b+c)-(min+max)}')