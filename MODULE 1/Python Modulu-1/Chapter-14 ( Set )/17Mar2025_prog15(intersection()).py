#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)  #  Returns  a  new  set  with  common  elements  between  sets  'a'  and  'b'
print(c) #{30 , 40}  in  any  order
print(type(c))  # <class  'set'>
d = a & b  #    A  new  set  with  common  elements  between  sets  'a'  and  'b'
print(d)   #{30 , 40}  in  any  order
print(type(d))   # <class  'set'>
print(c  is  d)  #  False  becoz   'c'  and  'd'  point  to  different  sets
print(c  ==  d)  #  True  becoz  sets  c  and  d  have  same  elements



'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) Is  set . intersection(list)  valid  ?  --->
							Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . intersection(b) ?  --->  a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) Is  list . intersection(set)  valid ?  --->  No  becoz  list  does  not  have  intersection()  method
'''
