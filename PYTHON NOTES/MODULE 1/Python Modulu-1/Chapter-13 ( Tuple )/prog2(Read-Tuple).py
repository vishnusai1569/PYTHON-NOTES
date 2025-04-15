#  What   are  the  outputs  if  input  is  (10 , 20 , 30 , 40) ?   (Home  work)
a = input('Enter  Tuple  :  ')
print(a) #  '(10,20,30,40)'
print(type(a))  #  <class 'str'>
b = eval(a)
print(b)  #  (10, 20, 30, 40)
print(type(b))  #  <class 'tuple'>
print(len(b))  #  4


'''
1) Let  input  be  (10 , 20 , 30 , 40)
    What  does  input()  function  read ?  ---> '(10 , 20 , 30 , 40)'
    What  does  eval()  function  do ?  --->  Converts   '(10 , 20 , 30 , 40)'  to   (10 , 20 , 30 , 40)

2) Which  of  the  following  are  valid  inputs ?
     a)  10 , 20 , 30 , 40  --->  Valid  becoz  ()  are  optional
     b)  10 , 20 , 30 , 40 , --->  Valid  and  last ,  is  optional
     c) 25 ,  --->  Valid  and  ,  is  mandatory
     d) (25 , )  --->  Valid  and  ,  is  mandatory  but  ()  are  optional
     e) (25) --->  Valid  but  it  is  int  and  not  tuple
     f)  ( ) ---> Valid   and  it  is  an  empty  tuple
     g) tuple() --->  Valid   and  it  is  an  empty  tuple
'''
