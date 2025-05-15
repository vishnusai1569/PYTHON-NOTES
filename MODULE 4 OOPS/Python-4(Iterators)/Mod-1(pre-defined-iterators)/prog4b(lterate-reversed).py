#  How  to  print  reversed  object  in  different  ways  (Home  work)
import   time
a = input('Enter  any  string  :  ')  #  Assume  that  input  is  HYD
r = reversed(a)  #   Creates  an  empty  reversed  object
print(type(r)) # <class  'reversed'>
print(r) # __str__()  returns type and address of the object
print('Iterate  reversed  object  with   next   function')
while   True:  #  How  to  iterate  reversed  object  'r'  with  next()  function
	try:
		print(next(r))   #  D  <next line>   Y  <next line>   H  <next line>
		time . sleep(1)
	except:
		break
print('Iterate  reversed  object  with   __next__   method')
r = reversed(a)  #  Creates   another  reversed  object  to  iterate  again
while   True:  #How  to  iterate  reversed  object   with  __next__()   method
	try:
		print(r . __next__())    #  D  <next line>   Y  <next line>   H  <next line>  StopIteration
		time . sleep(1)
	except:
		break
print('Iterate  reversed  object  with   for  loop')
for  x  in   reversed(a):  #  Creates  another  reversed  to  iterate  with  for  loop
	print(x)    #  D  <next line>   Y  <next line>   H  <next line>
	time . sleep(1)
print('Unpack  reversed  object  with   *  operator :   ' , *reversed(a)) #   Srores  all  the  characters  of  the  string  in  reverse  order  in  reversed  object  and  unpacks   i.e.  D  <space>   Y  <space>   H  <next line>
print('reversed  object  in  the  form   of  list  :  ' , list(reversed(a))) #  Srores  all  the  characters  of  the  string  in  reverse  order  in  reversed  object  and   converted  to  list   i.e.   ['D' , 'Y' , 'H']
print('Reverse  string   :   ' , '' . join(reversed(a))) #  #  Srores  all  the  characters  of  the  string  in  reverse  order  in  reversed  object  and  joined  to  form  a   string  i.e.   ['D' , 'Y' , 'H']How  to  convert  reversed  object  to   string  --->  DYH