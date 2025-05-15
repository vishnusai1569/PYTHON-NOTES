#  How  to  iterate  zip  object  in  differenet  ways  (Home  work)
import   time
a = ['Telangana' , 'Andhra Pradesh' , 'Karnataka ', 'Tamilnadu']
b = ['Hyderabad' , 'Amaravathi' , 'Bangalore', 'Chennai']
z = zip(a , b)  #  Creates  an  empty  zip  class  object
print(type(z)) # <class  'zip'>
print(z) # __str__()  returns  type and address of the object
print('Iterate  zip  object  with   next()   function')
while   True:  # How  to   iterate  zip  object  with  next  function
	try:
		print(next(z))  #  ('Telangana', 'Hyderabad')  <next  line>  ('Andhra Pradesh', 'Amaravathi')  <next  line>  ('Karnataka ', 'Bangalore')  <next  line>  ('Tamilnadu', 'Chennai')
		time . sleep(1)
	except  StopIteration:
		break
print('Iterate  zip  object  with  __next__  method')
z = zip(a , b)  #   Creates  another  zip  object  to  iterate  again
while   True:  #How  to   iterate  zip  object  with  __next__  method
	try:
		print(z . __next__()) #  ('Telangana', 'Hyderabad')  <next  line>  ('Andhra Pradesh', 'Amaravathi')  <next  line>  ('Karnataka ', 'Bangalore')  <next  line>  ('Tamilnadu', 'Chennai')
		time . sleep(1)
	except:
		break
print('Iterate  zip  object  with   for  loop')
for  x  in   zip(a , b):  #  Creates  another  zip  object  to  iterate  again  with  for  loop
	print(x)  #  ('Telangana', 'Hyderabad')  <next  line>  ('Andhra Pradesh', 'Amaravathi')  <next  line>  ('Karnataka ', 'Bangalore')  <next  line>  ('Tamilnadu', 'Chennai')
	time . sleep(1)
print('Iterate  elements  of  each  tuple  in  zip  object')
for x , y in  zip(a , b):  #  x  and  y  are  elements  of  each  tuple  yielded  by  zip   iterator
	print(x , y, sep = '...')  #  Telangana ... Hyderabad <next  line>  Andhra Pradesh ... Amaravathi  <next  line>  Karnataka ... Bangalore  <next  line>  Tamilnadu ... Chennai
	time . sleep(1)
print('Unpacks  zip  object  with   *  operator')
print(*zip(a , b)) #  All  the  tuples  are  stored  in   zip  object  which  are   unpacked  i.e.('Telangana', 'Hyderabad')  <space>  ('Andhra Pradesh', 'Amaravathi')  <space>  ('Karnataka ', 'Bangalore')  <space>  ('Tamilnadu', 'Chennai')
print()
print('zip   object  in  the  form  of   list')
print(list(zip(a , b))) # All  the  tuples  are  stored  in   zip  object  which   is  converted  to  list  i.e. [('Telangana', 'Hyderabad'), ('Andhra Pradesh', 'Amaravathi'), ('Karnataka ', 'Bangalore'), ('Tamilnadu', 'Chennai')]
print()
print('zip   object  in  the  form  of   dictionary')
print(dict(zip(a , b))) # All  the  tuples  are  stored  in   zip  object  which   is  converted  to   dictionary  i.e.  {'Telangana': 'Hyderabad', 'Andhra Pradesh': 'Amaravathi', 'Karnataka ': 'Bangalore', 'Tamilnadu': 'Chennai'}