# Find  outputs (Home  work)
from  threading  import   *
class   c1:
	def  m1(self):
		for  i  in  range(10):
			print('child  thread')
a = c1()
child = Thread(target =  a . m1()) #  Executes   m1()  method  of   class  c1 which  returns  None   i.e.  target = None
child . start() #  child  thread  does  nothing  becoz  target  is   None
for  i  in  range(10):
        print('main  thread')


'''
1) What  does  target = a . m1()  do ?  --->  Executes  m1()   method  due  to  ()

2) What  is  the  target ?  --->   None  becoz  m1()  method  returns  None  by  default

3) What  does  child  thread  do ?  --->  Nothing  becoz  target  is  None

4) How  many  threads  are  in  the  program ?  --->  2  threads  i.e.  main  thread  and   child  thread

5) What  are  the  outputs ?  ---> 10  times  child  thread
													 10  times  main  thread

6) Are  outputs  same  for  every  run ?  --->  Yes  becoz   child  thread  is  not  doing  anything

7) target = a . m1
    target = a . m1()
    What  is  the  difference  between  the  above  two  statements ?  --->
																						target  is  m1  method  when  ()  are  missing
									   													and  target  is  result  of  m1()  method  when  ()  are  present
'''