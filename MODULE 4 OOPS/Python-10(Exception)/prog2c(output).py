# Find  outputs  (Home  work)
#print(7 / 0) # ERROR: ZeroDivisionError  can  not  be  caught  as  it  is   thrown  outside  try  suite
try:
	print(7 / 0)   #  Throws   ZeroDivisionError
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
#print(7 / 0) # ERROR: ZeroDivisionError  can  not  be  caught  as  it  is   thrown  outside  try  suite
print('Bye')

'''
Division  by  zero  is  not  permitted
Bye
'''


'''
1) If  try  suite  raises  an  error
    a) Can  the  error  be  caught ?  ---> Yes  with  except  suite
    b) Is  except  suite  executed ?  ---> Yes
    c) Is  the  error  reported  ?  --->  No  provided  it  is  caught
    d) Is  it  normal  termination (or) abnoraml ? --->  Normal  termination  provided  error  is  caught
    e) Is  rest  of  the  program  executed ? --->  Yes  provided  error  is  caught

2) If  the  code  outside  try  suite  raises  an  error,
    a) Can  the  error  be  caught ?  ---> No
    b) Is  except  suite  executed ?  ---> No
    c) Is  error  reported  ?  ---> Yes
    d) Is  it  normal  termination (or) abnoraml ? --->  Abnormal  termination
    e) Is  rest  of  the  program  executed ? ---> No
'''