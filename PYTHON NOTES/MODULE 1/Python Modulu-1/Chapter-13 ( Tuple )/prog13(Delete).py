# How  to  delete  an  element  of  tuple ?   (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30) #  Error  becoz  there is  no  remove()  method  in  tuple
#del  a[2]  #  Error  becoz  tuple  is  immutable
#a . pop(2)  #   Error  becoz  there is  no   pop()  method  in  tuple
print(a) #   (10 , 20 , 30 , 40 , 50)
print(id(a))  #  Address  of  tuple  (1000)
a = a[:2] + a[3:]  #  How  to  remove  30  from  tuple  'a'
print(a) #  (10,20,40,50)
print(id(a))   #  Address  of  2nd  tuple  (2000)



'''
1) Can  tuple  element  be  removed ?  ---> No  becoz  tuple  is  immutable

2) a = a[ : 2] + a[3 : ]
    What  is  modified  when  the  above  statement  is  executed ?  ---> Reference  but  not  tuple

3) In  other  words, two  tuples  are  concatenated  to  form  a  new  tuple  and  reference  is  modified  to  new  tuple
'''
