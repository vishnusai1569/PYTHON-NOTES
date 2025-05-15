# update()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = {12 : 'Chennai' , 18 : 'Delhi' , 14 : 'Vijayawada'}
print(a)  #  {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
a . update(b)  #  Appends  all  the  key : value  pairs  of  dictionary  to  dict  'a'   i.e.  a = a + b
print(a)   #  {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Delhi' , 12 : 'Chennai' , 14 : 'Vijayawada'}
a . update( {19 : 'Mumbai'} )  #  Appends  19 : 'Mumbai'  to  dict  'a'
print(a)  #   #  {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Delhi' , 12 : 'Chennai' , 14 : 'Vijayawada' , 19 : 'Mumbai'}


'''
update()   method
---------------------
1) What  does  dict1 . update(dict2)  do ? ---> Appends  all  the  key : value  pairs  of  dict2  to  dict1

2) What  does  dict1  finally  contain ?  --->  All  the  key : value  pairs  of  dict1  and  dict2

3) What  does  dict . update(Nested  sequence)  do ?  --->  Appends  elements  of  inner  sequences  to  the  dictionary
												                                             in  the  form  of  key : value pairs

4) What  are  the  three  ways  to  concatenate  two  dictionaries ? --->  a) dict1 . update(dict2)
																												  b) dict1 = {**dict1 , **dict2}
																												  c)  dict1 = dict1 |  dict2
'''
