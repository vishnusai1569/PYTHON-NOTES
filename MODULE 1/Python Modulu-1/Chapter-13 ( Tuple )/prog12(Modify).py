#  How  to  modify  an  element  of  tuple ?    (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35  #  Error  becoz  tuple  is  immutable
print(a)  #  (10,20,30,40,50)
print(id(a))  #  Address  of  tuple (1000)
a = a[:2] + (35,) + a[3:]  #   How  to  modify  30  in  tuple  to  35
print(a)   #  (10, 20, 35, 40, 50)
print(id(a))  #  Address  of  2nd  tuple (2000)



'''
1) Can  tuple  element  be  modified ?  ---> No  becoz  it  is  immutable

2) a = a[ : 2] + (35,) + a[3 : ]
    What  is  modified  when  the  above  statement  is  executed ?  ---> Reference  but  not  tuple

3) In  other  words,  three  tuples  are  concatenated  to  form  a  new  tuple  and
    reference  'a'  points  to  the  new  tuple
'''
