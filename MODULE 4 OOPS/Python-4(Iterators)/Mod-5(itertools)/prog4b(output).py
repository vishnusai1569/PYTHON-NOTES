#  Find  outputs  (Home  work)
from  itertools  import  zip_longest
import   time
def  disp(z):
	while   True:
		try:
			print(next(z))
			time . sleep(1)
		except:
			break
list = [10 , 20 , 30 , 40]
z1  =  zip(range(7) , list)  #  Empty   object
print(type(z1)) # <class 'zip'>
disp(z1)  #  (0 , 10)  <next  line>  (1 , 20)  <next  line>  (2 , 30)  <next  line>  (3 , 40)  <next  line>
z2 = zip_longest(range(7) , list)  #  Empty  object
print(type(z2)) # <class 'itertools . zip_longest'>
disp(z2)   #   (0 , 10)  <next  line>  (1 , 20)   <next  line>  (2 , 30)   <next  line>  (3 , 40)   <next  line>   (4 , None)   <next  line>  (5 , None)   <next  line>   (6 , None)   <next  line>


'''
1) How  long  objects  are  zipped  for  zip  ?  --->  Until  at  least  one  object  is  exhausted

2) How  long  objects  are  zipped  for  zip_longest  ?  --->  Until  both  the  objects   are  exhausted
'''