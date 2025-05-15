#  How  to  print  list_reverseiterator  object  in  different  ways  (Home   work)
import   time
a = [25 , 10.8 , 'Hyd' , True]
r = reversed(a)  #  Creates  an  empty  list_reverseiterator  object
print(type(r)) # <class 'list_reverseiterator'>
print(r) # __str__()  returns type and address of  object  'r'
print('Iterate  list_reverseiterator  object  with   next()   function')
while   True:   # How  to  iterate   list_reverseiterator  object  with   next()   function
	try:
		print(next(r))  #  True  <next line>  Hyd  <next line>  10.8  <next line>   25  <next line>
		time . sleep(1)
	except:
		break
print('Iterate  list_reverseiterator  object  with   __next__()   method')
r = reversed(a)  #  Creates  another  object to  iterate  again
while   True:  # How  to  iterate   list_reverseiterator  object  with   __next__()  method
	try:
		print(r.__next__()) #  True  <next line>  Hyd  <next line>  10.8  <next line>   25  <next line>
		time . sleep(1)
	except:
		break
print('Iterate  list_reverseiterator  object  with   for  loop')
for  x  in   reversed(a):  #   Creates   another  list_reverseiterator  object   to  iterate  with  for  loop
	print(x)  #  True  <next line>  Hyd  <next line>  10.8  <next line>   25  <next line>
	time . sleep(1)
print('Unpack  list_reverseiterator  object  with   *  operator   :  ' , *reversed(a)) #  Stores  all   the  elements  in  reverse  order  in  list_reverseiterator  object  and  unpacks
														#  i.e.  True  <space>  Hyd  <space>  10.8  <space>   25  <next line>
print('Reverse  list  :  '  ,  list(reversed(a))) #   Stores  all   the  elements  in  reverse  order  in  list_reverseiterator  object  and   converted  to  list  i.e.   [True , 'Hyd' , 10.8  ,   25]