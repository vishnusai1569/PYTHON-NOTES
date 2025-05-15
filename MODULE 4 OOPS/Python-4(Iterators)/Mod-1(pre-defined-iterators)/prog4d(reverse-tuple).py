# Can  tuple  be  reversed ?   --->  Yes (Home  work)
import   time
a = (25 , 10.8 , 'Hyd' , True)
b = reversed(a)  # Creates  an  empty  reversed  object
print(type(b)) # <class 'reversed'>
for  x  in   b: #   'x'  is  each  element   which  is   yielded  by  reversed  iterator
	print(x)  #   True  <next  line>  Hyd   <next  line>  10.8    <next  line>  25   <next  line>
	time . sleep(1)