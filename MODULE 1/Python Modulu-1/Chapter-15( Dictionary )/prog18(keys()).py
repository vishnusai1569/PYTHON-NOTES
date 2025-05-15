#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()
print(b) # dict_keys([10 , 20 , 15 , 18])
print(type(b)) # <class 'dict_keys'>
for  x  in   b:  # 'x'  is each  element  of the  list  in  dict_keys  object
        print(x) # 10 <nextline> 20 <nextline> 15 <nextline> 18 <nextline>



'''
What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys
'''
