#  How  to  iterate  enumerate  object  in  different  ways
import   time
a = [25 , 10.8 , 'Hyd' , True]
e = enumerate(a)  #  Empty  object
print(type(e)) #  <class  'enumerate'>
print(e) #   Type  and  address  ofobject  'e'
print('Iterate  enumerate  object  with   next   function')
while   True:  #   Iteration   2
	try:
		print(next(e))  #  (0 , 25) <next   line>  (1 , 10.8)   <next   line>   (2 , 'Hyd')  <next   line>   (3 , True) <next   line>
		time . sleep(1)
	except:
		break
e = enumerate(a)  #  2nd  object
print('Iterate  enumerate  object  with   __next__   method')
while   True:
	try:
		print(e . __next__())   #  (0 , 25) <next   line>  (1 , 10.8)   <next   line>   (2 , 'Hyd')  <next   line>   (3 , True) <next   line>
		time . sleep(1)
	except:
		break
print('Iterate  enumerate  object  with   for  loop')
for  x  in   enumerate(a): #  'x'  is   each   tuple  yielded  by  the  enumerate   iterator
	print(x)  #  (0 , 25) <next   line>  (1 , 10.8)   <next   line>   (2 , 'Hyd')  <next   line>   (3 , True) <next   line>
	time . sleep(1)
print('Elements  of  each   tuple  in  enumerate  object')
for  x , y  in  enumerate(a):  #  'x'  and  'y'  are  elements  of  each   tuple  yielded  by  the  enumerate  iterator
	print(x , y , sep = '...')   #  0  ... 25  <next   line>  1  ... 10.8   <next   line>   2  ... Hyd   <next   line>  3  ... True <next   line>
	time . sleep(1)
print('enumerate  object  with   *  operator  :  ' , *enumerate(a))  #  All  the   4  tuples  are  stored  in  enumerate  object  and   then  unpacked  i.e.   #  (0 , 25) <space>  (1 , 10.8)   <space>   (2 , 'Hyd')  <space>   (3 , True)
print()
print('enumerate  object  in  the  form   of  list  :  ' , list(enumerate(a)))   #  All  the   4  tuples  are  stored  in  enumerate  object  and   converted  to  list   i.e.  [(0 , 25) , (1 , 10.8) ,  (2 , 'Hyd') ,(3 , True) ]
print()
print('enumerate  object  in  the  form   of  dictionary   :  ' , dict(enumerate(a)))   #  All  the   4  tuples  are  stored  in  enumerate  object  and   converted  to  dictionary   i.e. {0 : 25 , 1 : 10.8 , 2 : 'Hyd' , 3 : True}



'''
1) What  is  the  alternative  to  next(e) ?  ---> e . __next__()

2) In  other  words,  next()  function  internally  calls   __next__()  method

3) Why  is  the  list  enumerated  so  many  times ?  --->  To  iterate  again  and  again

4) In  other  words,  iterator  can  be  iterated  only  once  and  hence  list  is  enumerated  multiple  times
'''