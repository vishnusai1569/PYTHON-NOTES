# How  to  implement  a  thread  with  function
from  threading  import   Thread
def  f1():  #  Executed  by  child  thread
	for  i  in  range(1 , 11) :
		print('Child  Thread  :  ' , i)
#  child  thread  is  dead
#  main  thread  executes  all  the  following  statements
child = Thread(target = f1) #   Creates  a  new  thread
child . start() #   Registers  child  thread  with  Thread scheduler and  child  thread executes  f1()  function
for  i  in  range(1 , 11):
        print('Main  Thread  :  ' , i)
#  main  thread  is  dead


'''
1) child = Thread(target = f1)
    child . start()
    What  is  the  issue  when  Thread  class  object  is  not  created ?  --->
														child . start()  throws  error  becoz  start()  method  can  not  be  called  without
														Thread  class  object  as  start()  is  an  instance  method  of  Thread  class

2) What  does  start()  method  do ?  --->  Registers  child  thread   with  Thread  Scheduler(TS)

3) What  does  child  thread  do ?  --->  Executes  target  i.e.  f1()  function

4) What  does  main  thread  do ?  --->  Executes  whole  program  except  f1()  function

5) Who  creates  main  thread ?  --->  PVM

6) When  is  main  thread  created ?  --->  As  soon  as  program  is   executed

7) How  to  run  the  program ?  --->  py  filename . py

8) How  many  threads  are  in  the  above  program ?  --->  Two  i.e.  main  thread  and  child  thread

9)  Are  they  executed  parallely  (or)  serially ?  --->  Parallely  (or)  concurrently  (or)  simultaneously  on  round  robin  basis

10) Can  outputs  be  predicted  when  program  has  multiple  threads ?  --->
																		No  becoz  we  have  no  idea  when  is  the  time  elapsed  for  a  thread

11) When  can  outputs  be  predicted ?  --->  When  program  has  single  thread    i.e.  main  thread

12) Are  outputs  same  for  every  run  when  program  has  multiple  threads  ?  --->
															No  becoz  we  have  no  idea  when  is  the  time  elapsed  for  a  thread

13) In  other  words,  outputs  vary  from  run  to  run  due  to  multiple  threads

14) When  are  outputs  same  for  every  run ? --->  When  program  has  single  thread  i.e.  main  thread

15) What  does  Thread  Scheduler  do  ?  --->
																Controls  (or)  executes  all  the  threads  one - by - one  on  round  robin  basis
'''