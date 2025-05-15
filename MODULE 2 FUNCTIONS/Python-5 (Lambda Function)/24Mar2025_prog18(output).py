# Find  output  (Home  work)
add = lambda  x  :   x == 25
print(add(10)) # False
add = lambda  x = 25 :   x == 35
print(add()) # False
#add = lambda  x  :   x = 25  #  Error :  Lambda  function  can  not  modify  argument
#add = lambda  x  :   x := 25  #  Error :  Lambda  function  can  not  modify  argument



'''
1) Can  regular  function  modify  value  of  argument  ?  --->  Yes

2) What  about  lambda   function  ?  --->  No  and  the  argument  is  treated  as   read  only  argument  in  lambda  function
'''
