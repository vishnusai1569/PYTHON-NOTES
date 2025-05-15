# popitem()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
print(a . popitem())   #  Removes  last  key : value  pair from  dict  'a'  and  is   returned  in  the  form  of  tuplei.e.  (18 , 'Pune')
print(a)  #  {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb'}
b = { }
#print(b . popitem())  #Error  becoz  'b'  is  empty  dictionary



'''
popitem()  method
---------------------
1) What  does  popitem()  method  do  ?  --->  Removes  last  key : value  pair  of  dictionary  and  returns
							                                             the  deleted  key : value  pair  in  the  form  of  tuple

2) What  does  popitem()  method  do  when  dictionary  is  empty ?  --->  Throws  error

3) What  is  the  difference  between  pop()  method  and  popitem()  method ?  --->
																						pop()  removes  desired  key : value  pair  from  dictionary
																						but   popitem()  removes  last  key : value  pair  from dictionary
'''
