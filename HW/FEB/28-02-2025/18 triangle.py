try:
    import math
    a=int(input("Enter 1st side:"))
    b=int(input("Enter 2nd side:"))
    c=int(input("Enter 3rd side:"))
    if (a+b>c) and (b+c>a) and (a+c>b):
        if a==b==c:
            print("equilateral  triangle")
            print(f'area={math.sqrt(3/4)*a**2}')
            print(f'perimeter={a+b+c}')
        elif a==b or b==c or c==a:
            print("isoscles  triangle ")
            print(f'perimeter={a+b+c}')
        elif a!=b or b!=c or c!=a:
            print("scalene  triangle")
            s=(a+b+c)/2
            k=s*(s-a)*(s-b)*(s-c)
            y=math.sqrt(k)
            print(f'area={y:.2f}')
            print(f'perimeter={a+b+c}')
    else:
            print("not a triangle, sum of every two sides should be > 3rd side")
except:
    print("inputs should be an integer")
    
    