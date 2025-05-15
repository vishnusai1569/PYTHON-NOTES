# union()  method  demo  program
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . union(b)  # Returns  a  new  set  with  all  the elements  of  sets  'a'  and  'b'
print(c) #  {10,20,30,40,50,60}  in  any  order
print(type(c)) #  <class 'set'>
d = a | b  #  A  new  set  with  all  the  elements  of   sets  a  and  b
print(d)  #  {10,20,30,40,50,60}  in  any  order
print(type(d))  #  <class 'set'>
print(c  is  d) #  False  becoz  'c' and 'd'  point  to different  sets
print(c  ==  d)  #  True  becoz  sets   c  and  d  have  same  elements
#print(a + b)  #  Error  becoz  sets  can  not  be  concatenated  with  + operator



'''
union()  method
------------------
1) What  does  a . union(b)  do ?  --->  Returns  a  set  with  all  the  elements  of  sets  'a'  and  'b'
														   (i.e.  concatenation)

2) a . union(b)
    Is  set  'a'   modified  after  execution  of  union()  method  ?  --->  No  becoz  results  are  stored  in  a  different  set

3) Is  set . union(list)  valid  ?  --->  Yes  becoz  argument  of  union()  method  can  be  any  sequence  but  not  necessarily  set

4) What  is  the  alternative  to  a . union(b) ?  --->  a | b

5) Is  set + set  valid ?  --->  No  becoz  sets  can  not  be  concatenated  with  +  operator

6) How  to  concatenate  sets ?   --->  a . union(b)
										                     and
										                    a |  b

7) Is  set | list  valid ?  --->  No  becoz  operands  of  |  operator  should  be  sets  only

8) Is  list . union(set)  valid ?  --->  No  becoz  list  does  not  have  union()  method
'''
