#  Which  of  the  following  statements  throw  ValueError ?  (Home  work)
import  math
#print(int('10.8')) # ValueError  becoz  '10.8'  can  not  be  converted  to  integer
#print(float('Ten')) # ValueError  becoz  'Ten'  can  not  be  converted  to  integer
#print(complex('Ten')) # ValueError  becoz  'Ten'  can  not  be  converted  to  complex
print(bool('Ten')) # True  becoz  'Ten'  is  a  non-empty   string
print(bool('')) # False  due  to  empty  string
print(float('10.8')) # 10.8
print(float('25')) # 25.0
print(int(10.8)) # 10
#print(math . sqrt(-25)) # ValueError  becoz  sqrt(-ve)  value  can  not  be   determined



'''
When  is  ValueError  raised  ?  --->  When   a  function  (or)  method  does  not  return  any  result
													      i.e. not  even  None
'''