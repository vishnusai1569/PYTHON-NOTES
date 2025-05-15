# What  are  the  outputs  if  input  is   [25 , 10.8 , 'Hyd' , True]   (Home  work)
a = input('Enter  list  :  ')   #   [25 , 10.8 , 'Hyd' , True]
print(type(a))  #  <class  'str'>
print(a) #   "[25 , 10.8 , 'Hyd' , True] "
b = eval(a)
print(b)   #   [25 , 10.8 , 'Hyd' , True]
print(type(b))  #  <class  'list'>


'''
1) What  does  input()  function  do  when  input  is  list  ?  --->  Reads  string  list

2) What  does  eval()  function   do ?  ---> Converts  string  list  to  list

3) What  does  input()  function  do  when  input  is  [] ?  --->  Reads  '[]'
    What  does  eval('[]')  do  ?  --->  Converts  '[]'   to  []
'''
