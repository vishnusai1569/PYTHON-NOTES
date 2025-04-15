# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():  #  'x'  is  each  element  of  the  list  in  dict_keys  object
	print(x) #  10  <next  line> 30  <next  line>  50  <next  line>
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values(): #  'x'  is  each  element  of  the  list  in  dict_values  object
	print(x)  #  20  <next  line>  40  <next  line>  60  <next  line>
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():  #  'x'  is  each   tuple   of  the  list  in  dict_items  object
	print(x) #  (10,20)  <next  line>  (30,40)  <next  line>  (50 , 60)  <next  line>
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:  #  'x'  is  each  element  of  the  list  in  dict_keys  object
	print(x)   #  10  <next  line> 30  <next  line>  50  <next  line>



'''
1) What  does  keys()  method  do ?  --->  Returns  dict_keys  object  which  contains  list  of  all  the  keys  of  dictionary

2) What  does  values()  method  do ?  --->  Returns  dict_values  object  which  contains  list  of  all  the  values  of  dictionary

3) What  does  items()  method  do ?  --->   Returns  dict_items  object  which  contains  list  of  tuples  where  each  tuple
																    contains  (key , value)

4) for  x  in  dict:
	       print(x)
    Which  method  is  called  by  the  above  for  loop  ?  --->  keys()  method  by  default
'''
