# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b) # dict_values(['Hyd' , 'Sec' , 'Cyb' , 'Pune'])
print(type(b)) # <class 'dict_values'>
for  x   in   b: #   'x'  is  each  element  of  the  list  in  dict_values  object
	print(x) # Hyd <nextline> Sec <nextline> Cyb <nextline> Pune <nextline>



'''
What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values
'''
