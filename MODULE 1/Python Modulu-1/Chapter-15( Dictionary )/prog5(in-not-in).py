#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys()) # True as 30 is a  valid key
print(60  in  a . keys()) # False as 60 is  invalid   key
print(60  in  a . values()) # True as 60 is a  valid  value
print(30  in  a . values()) # False as 30 is  invalid  value
print(50  in  a) # True   becoz 50  is  a   valid  key
print(20  in  a) # False as 20 is  invalid  key
print(70  not  in  a . keys()) # False as 70 is  a  valid   key
print(40  not  in  a . values()) # False as 40 is a  valid  value
print(25  not  in  a) # True as 25  is  not  a  valid   key



'''
print(50  in   a)
Which  method  is  called  in  the  above  statement ?  --->  keys()  method  is  called  by  default
'''
