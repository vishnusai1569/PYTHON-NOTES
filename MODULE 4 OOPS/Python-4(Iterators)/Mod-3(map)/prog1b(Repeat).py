#  Modify  following  program  with  regular  function  and  for  loop
import time
def   square(x):
	return x * x
a = [10 , 20 , 15 , 18 , 5]
m = map(square , a)  #  Creates  an  empty  map   object
print(type(m)) # <class 'map'>
print(m) # __str__()  returns  type  and  address  of  object  'm'
for  y  in  m:
	print(y)  #   100  <next  line>  400  <next  line>   225  <next  line>  324  <next  line>  25  <next  line>
	time . sleep(1)