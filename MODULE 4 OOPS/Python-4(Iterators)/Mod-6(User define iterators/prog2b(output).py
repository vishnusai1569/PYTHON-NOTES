# Find  outputs
import  time
class   c3: #   c3 is  iterable  but  not  iterator  as  it  has  only  __iter__()  method  but  not   __next__()
	def  __iter__(self):  #  self  is   object  itr
		print('__iter__  method ')
		return  reversed([10 , 20 , 15 , 18])  #  Returned  to   itr  in  the  for  loop
# End  of  the  class
itr = c3()
for  x  in   itr:  #  for  x  in  list_reverseiterator:  --->  'x' is  each  element  yileded  by  __next__()  method  list_reverseiterator
	print(x)  #   18  <next  line>   15  <next  line>  20  <next  line>  10  <next  line>
	time . sleep(1)
#print(next(itr)) #  Error :   next()  function  needs  iterator  but  itr  is  not  an  iterator

'''
__iter__  method
18
15
20
10
'''


'''
1) Which  object  is  returned  by   __iter__ ()  method  ?  --->  list_reverseiterator  object  which  is  an  empty  object

2) Can  __iter__()  method  return  list_reverseiterator  object ?  --->  Yes  becoz  it  is  an  iterator

3) Where  is  the  list_reverseiterator  object  returned  to  ?  --->  for  loop  object   itr

4) for   x   in   itr:
	How  is  the  above  for  loop  reduced  to ?  --->  for  x   in   list_reverseiterator:

5) What  does  for  loop  do ?  --->  Iterates  list_reverseiterator  object

6) Which  methods  are  executed  in  1st  iteration  of  for  loop ?  --->
																__iter__()  method  of  c3  class  as  itr  is  c3  class  object  and
																__next__()   method  of  list_reverseiterator  class  as  itr  is  replaced  with
																list_reverseiterator

7) Which  method  is  executed   in  remaining  iterations  of  for  loop ?  --->
																						__next__()  method  of  list_reverseiterator  class
'''