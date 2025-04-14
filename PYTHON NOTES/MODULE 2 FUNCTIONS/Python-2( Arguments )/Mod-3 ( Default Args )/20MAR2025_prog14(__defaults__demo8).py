 # Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"  #  a = 'Hyd' + 'Sec' = 'HydSec'
	b += [1 , 2 , 3]  #  b = [1,2,3,1,2,3] + [1,2,3] = [1,2,3,1,2,3,1,2,3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__)  #  ('Hyd' , [])
f1()  #   'a'  is  default  value  'Hyd'  , 'b'  is  default  value  []  , Results  are   a : HydSec <next  line>  b : [1,2,3]
print('Default Values  :  ' , f1 . __defaults__)  #  ('Hyd' , [1,2,3])
f1()   #   'a'  is  default  value  'Hyd'  , 'b'  is  default  value  [1,2,3]  , Results  are   a : HydSec <next  line>  b : [1,2,3,1,2,3]
print('Default Values  :  ' , f1 . __defaults__)   #  ('Hyd' , [1,2,3,1,2,3])
f1()    #   'a'  is  default  value  'Hyd'  , 'b'  is  default  value  [1,2,3,1,2,3]  , Results  are   a : HydSec <next  line>  b : [1,2,3,1,2,3,1,2,3]



'''
1) When  is  __defaults__ modified ?  --->  When  function  modifies  mutable  default  argument

2) When  is   __defaults__  remains  unchanged ?  ---> When  function  modifies  immutable  default  argument

3) a += "Hyd"
    What  is  modified  (reference  (or)  object) ?  --->  Reference  'a'  but  not  str  object  as  it  is  immutable

4) b += [1 , 2 , 3]
    What  is  modified  (reference  (or)  object) ?  --->  Object  becoz  list  is  mutable
'''
