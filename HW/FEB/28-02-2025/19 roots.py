import math
a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))
disc=b**2-4*a*c
if a==0:
    print("Value  of  a  can  not  be  0")

else a!=b!=c!=0:
    if disc==0:
        print("Roots are real and equal")
        print(f'Root1 = {-b/(2*a)}')
        print(f'Root2 = {-b/(2*a)}')
    elif disc>0:
        print("Roots  are  real  and  distinct")
        k=(-b + math.sqrt(disc))/(2*a)
        g=(-b - math.sqrt(disc))/(2*a)
        print((f'Root1 = {k:.2f}'))
        print(f'Root2 = {g:.2f}')
    elif disc<0:
        print("Roots  are  imaginary  (or) complex")
        real=-b/(2*a)
        imag=math.sqrt(-disc)/(2*a)
        k=(f'{imag}j')
        print(f'Root1 = {real}+ {k}j')
        print(f'Root1 = {real}-{k}j')