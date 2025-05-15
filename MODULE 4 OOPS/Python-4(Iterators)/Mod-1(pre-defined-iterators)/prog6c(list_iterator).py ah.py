# How  to  iterate   list_iterator  in  different  ways
import   time
list  =  [10  ,  20  ,  15  ,  18]
print('Iterate  list  with  for  loop')
for x in list:  #  'x'  is  each  element  of  the  list
	print(x)  #  10  <next  line>  20   <next  line>  15 <next  line> 18 <next  line>
#print(next(list)) #  Error :  list is  not  an  iterator
list_itr  =  iter(list)  #  Converts  list  to  list_iterator
print(type(list_itr)) # <class 'list_iterator'>
print(list_itr) # __str__() method  returns type and address  of  list_itr
print('Iterate  List_iterator  with  next()  function')
while   True:  # How  to  iterate  list_iterator  with  next()  function
	try:
		print(next(list_itr))  #  10  <next  line>  20   <next  line>  15 <next  line> 18 <next  line>
		time . sleep(1)
	except  StopIteration:
		break
print('Iterate  List_iterator  with   __next__()  method')
list_itr  =  iter(list)  # Convert  again  to  iterate  one  more  time
while   True:  #How  to  iterate  list_iterator  with   next  method
	try:
		print(list_itr  . __next__())  #  10  <next  line>  20   <next  line>  15 <next  line> 18 <next  line>
		time . sleep(1)
	except:
		break
print('Iterate  List_iterator  with   for    loop')
for  x  in  iter(list):  #How  to  iterate  list_iterator  with  for  loop
	print(x)  #  10  <next  line>  20   <next  line>  15 <next  line> 18 <next  line>
	time . sleep(1)
print('Unpacks  List_iterator  with  *  operator')
print(*iter(list)) # How  to  unpack  list_iterator    --->   #  10  <space>  20   <space>  15 <space> 18