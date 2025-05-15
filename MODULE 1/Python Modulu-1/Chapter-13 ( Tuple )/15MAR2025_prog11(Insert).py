# How  to  insert  35  at  index  3  of  tuple  'a'  without  converting  to   list
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3     4
#a . insert(3 , 35) #   Error becoz  there  is  no  insert()  method  in  tuple
print(a)  #  (10,20,30,40,50)
print(id(a))  # Address  of   tuple  with  5  elements  (may  be  1000)
a = a[:3] + (35,) + a[3 :  ]  #    a = (10,20,30) + (35,) + (40,50)  ---> How  to  insert  35  at  index  3  of  tuple  'a'
print(a) #  (10,20,30,35,40,50)
print(id(a))  # Address  of   tuple  with  6  elements  (may  be  2000)



'''
1) Can  element  be  inserted  into  a  tuple ?  --->  No  becoz  tuple  is  immutable

2) a = a[ : 3] + (35 , ) + a[3 : ]
    What  is  modified  when  the  above  statement  is  executed ?  --->	Reference  but  not  tuple

3) In  other  words,  three  tuples  are  concatenated  to  form  a  new  tuple  with  35  at  index  3

4) Is  a[: 3] + (35)  valid ? --->  No  becoz  tuple  and  int  can  not  be  concatenated

5) Are  a[0 : 3]  and  a[:3]  same ?  --->  Yes  becoz  default  begin  0

6) Are  a[3 : 5]  and  a[3 : ]  same ?  ---> Yes  becoz  default  end  is  length  of  the  tuple
'''
