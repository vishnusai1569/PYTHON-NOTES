'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5

Hint:  Use  for  loop
'''


n=int(input("enter the number :"))
a, b = 0, 1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c