'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  --->  [4 , 16 , 36 , ... ,  400]
'''

k=int(input("enter the range:"))
c=[i**2 for i in range(1,k)if(i**2)%2==0]
print(c)