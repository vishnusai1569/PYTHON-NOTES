# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():  #  x  and  y are  elements  of  each  tuple  in  the  list  of  dict_items  object
	print(x , y , sep = '...') #  10 ... 20  <next line>  30  ... 40 <next line>50  ... 60 <next line>
'''
for  x ,  y  in   a:  # Error  due  to 2  variables  x  and  y
	print(x , y
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:  # Error  due  to 2  variables  x  and  y
	print(x , y , sep = '...')
'''


'''
1) What  does  items()  method  return ?  --->  dict_items([(10 , 20) , (30 , 40) , (50 , 60)])

2) for  x   in  a:
	      print(x)
    Which   method  is  called  by  for  loop  internally  ?  ---> keys()  method

3) When  are  two  variables  permitted  in  for  loop ?  --->
																	Only  for  items()  method  but  not  for  keys()  and  values()  methods
'''
