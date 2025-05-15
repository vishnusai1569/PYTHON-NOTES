# Find  outputs  (Home  work)
from  threading  import  *
class  c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child  = Thread(target = a . m1) #  A  new  thread  is  created
a . m1()   #   Metghod  call  to  m1()  but  not  thread  execution
for  i  in  range(10):
	print('main  thread')



'''
1) How  many  threads  are  in  the  program ?  --->  Just  one  thread
																				 i.e. MainThread

2) Why  is  there  only  single  thread ?  --->   Since  child  thread  is  created  but  not  started  and
																        hence  it  is  not  treated  as  a  thread

3) What  are  the  outputs  of  program ?  --->  10  times  child  thread
																		  10  times  main  thread

4) Are  the  outputs  same  for  every  run ?  --->  Yes   becoz  there  is  only  one  thread

5) child = Thread(target = a . m1)
     child . start()
     a . m1()
     Who  is  executing  m1()  method  wrt  child . start() ?  --->  child  thread
     Who  is  executing  m1()  method  wrt  a . m1() ?  --->  main  thread
'''