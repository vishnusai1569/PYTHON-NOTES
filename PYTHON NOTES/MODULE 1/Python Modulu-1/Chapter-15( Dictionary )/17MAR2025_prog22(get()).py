#  get()  method  demo  program
a = {10 : 'Hyd ' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
print(a . get(15))  #  Value  of   key  15  i.e.  Cyb
print(a[15])   #  Value  of   key  15  i.e.  Cyb
#print(a[19])  #  Error  becoz  19  is  invalid  key  in  dict  'a'
print(a . get(19))  #   None  becoz  19  is   invalid   key
print(a . get(14 , 'Chennai'))  #   Chennai  becoz  14  is  invalid  key
print(a . get(18 , 'Delhi'))  #   Value  of  key  18  i.e.  Pune( Ignores  'Delhi')



'''
get()  method
----------------
1) What  does  get(valid-key)  do  ? --->  Returns  value  of  the  key  in  the  dictionary
    What  does  get(invalid-key)  do ? --->	Returns  None

2) What  does  get(invalid-key , x)  do ?  ---> Returns  'x'
     What  does  get(valid-key , x)  do ?  ---> Returns  value  of  the  key  in  the  dictionary  and  'x'  is  ignored

3) What  are  the  two  ways  to  obtain  value  of  the  key ?  --->  dict[key]  and  dict . get(key)

4) What  is  the  difference  between  dict . get(invalid-key)  and  dict[invalid-key] ?  --->
									dict . get(invalid-key)  returns  None  but  dict[invalid-key]  throws  error
'''
