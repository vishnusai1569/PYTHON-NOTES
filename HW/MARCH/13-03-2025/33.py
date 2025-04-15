#Write a program to print even numbers between 1 and 20 with  comprehension
k=int(input("enter the range:"))
c=[i for i in range(1,k) if i%2==0 ]
print(c)