# pop()  method  demo program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
print(a . pop(15))  #  Removes  15 : 'Cyb'  from  dict  'a'  and  returns  the  deleted value  i.e.  Cyb
print(a)  # {10 : 'Hyd' , 20 : 'Sec' , 18 : 'Pune'}
#print(a . pop(19))  # Error  becoz  19  is  invalid  key
print(a . pop(14 , 'Chennai'))  #  Returns  'Chennai'  becoz  14  is  invalid  key
print(a)   # {10 : 'Hyd' , 20 : 'Sec' , 18 : 'Pune'}
print(a . pop(20 , 'Delhi'))   #  Removes  20 : 'Sec'  from  dict  'a'  and  returns  the  deleted value  i.e.  Sec  (Ignores  'Delhi')
print(a)    # {10 : 'Hyd' , 18 : 'Pune'}
#print(a . pop())   #   Error  due  to  no  args



'''
pop()  method
----------------
1) What  does  pop(valid-key)  do ?  --->  Removes  key :  value  pair  from  dictionary  and  returns  the  deleted  value

2) What  does  pop(Invalid-key)  do ?  ---> Throws  error

3) What  does  pop(Invalid-key , x)  do ?  --->  Removes  nothing  and  returns   'x'

4) What  does  pop(valid-key , x)  do ?  --->  Removes  key :  value  pair  from  dictionary  and  returns  the  deleted  value
											                         (Second  argument 'x'  is  ignored)

5) What  are  the  two  ways  to  remove  key :  value  pair  from  dictionary ?  --->  dict . pop(key)
																																	 	  and
																																    del   dict[key]

6) del   dict[key]
    dict . pop(key)
    What  is  the  difference  between  the  above  two  statements  ?  --->
																	pop(key)  returns  the  deleted  value  but  del  operator  returns  nothing

Note:
1) What  does  list . pop(No  args)  do  ?  --->  Removes  last  element  of  the  list  and  returns  the  deleted  element
    What  does  set . pop(No  args)  do  ?  --->	Removes  first  element  of  the  set  and  returns  the  deleted  element
    What  does  dict . pop(No  args)  do  ?  ---> Throws  error  due  to  no  args

2) How  many  arguments  can  list . pop()  take ?  --->  0  (or)  1 (i.e.  index)
    How  many  arguments  can  set . pop()  take ?  --->  0  becoz  set  has  no  index
    How  many  arguments  can  dict . pop()  take ?  ---> 1  (or)  2
'''
