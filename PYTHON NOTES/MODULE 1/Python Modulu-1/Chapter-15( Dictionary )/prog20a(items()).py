#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()
print(b) #  dict_items([(10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (18 , 'Pune')])
print(type(b)) # <class 'dict_items'>
for  x   in   b:  #  'x'  is  each  tuple  of  the  list  in  dict_items  object
        print(x) # (10 , 'Hyd') <nextline> (20 , 'Sec') <nextline> (15 , 'Cyb') <nextline> (18 , 'Pune') <nextline>
for  x , y   in  b: #  x  and  y  are  elements  of each  tuple  in  the  list  of  dict_items  object
        print(x , y , sep = ' ... ') # 10...Hyd <nextline> 20...Sec <nextline> 15...Cyb <nextline> 18...Pune <nextline>



'''
1) What  does  items()  method  do  --->  Returns  dict_items  object  which  has  list  of  tuples

2) What  are  the  two  elements  of  each  tuple ?  --->  (key , value)
'''
