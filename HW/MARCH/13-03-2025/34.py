'''
Write a program to print even numbers between 1 and 20 with  comprehension without  using  if

Output: [Even  numbers  between  1  and  20]
'''

k=int(input("enter the range:"))
c=[i for i in range(2,k+1,2) ]
print(c)