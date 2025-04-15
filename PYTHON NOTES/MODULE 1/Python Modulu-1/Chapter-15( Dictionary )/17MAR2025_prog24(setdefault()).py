# setdefault()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec'  , 15 : 'Cyb' , 18 : 'Pune'}
print(a . setdefault(15))  #  Value  of  key  15  i.e.  Cyb
print(a . setdefault(19))  #  None  becoz  19  is  invalid  key  and  appends  19 : None  to  dict  'a'
print(a)  #  {10 : 'Hyd' , 20 : 'Sec'  , 15 : 'Cyb' , 18 : 'Pune' , 19 : None}
print(a . setdefault(14 , 'Chennai'))   #  Chennai  becoz  14  is  invalid  key  and  appends  14 :  'Chennai' to  dict  'a'
print(a)   #  {10 : 'Hyd' , 20 : 'Sec'  , 15 : 'Cyb' , 18 : 'Pune' , 19 : None , 14 : 'Chennai'}
print(a . setdefault(18 , 'Delhi'))  #  Value  of  key  18  i.e.  Pune  (Ignores  'Delhi')
print(a)    #  {10 : 'Hyd' , 20 : 'Sec'  , 15 : 'Cyb' , 18 : 'Pune' , 19 : None , 14 : 'Chennai'}


'''
setdefault()  method
--------------------------
1) What  does  setdefault(valid-key)  do  ? --->  Returns  value  of  the  key  in  the  dictionary

2) What  does  setdefault(Invalid-key)  do ? --->  Returns  None  and  appends  key : None  to  the  dictionary

3) What  does  setdefault(Invalid-key , x)  do ?  --->  Returns  x  and  appends  key : x  to  the  dictionary

4) What  does  setdefault(valid-key , x)  do ?  --->  Returns  value  of  the  key  and  ignores  'x'
'''
