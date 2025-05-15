'''(Home  work)
Find  outputs

Assumption:   Time  is  elapsed  after  5  iterations  of  for  loop   for  each  thread
'''
from  threading  import  *
def    f1():   #  Executed  by  t1 , t2  and t3  concurrently
	name = current_thread() . name
	for  i  in  range(1 , 11):
			print(name , ' : ' , i)
	print(name , 'is  dead')
t1 = Thread(target = f1 , name = 'One')  # Creates  3  new  threads
t2 = Thread(target = f1 , name = 'Two')
t3 = Thread(target = f1 , name = 'Three')
t3 . daemon = True  #  t3  is  made  daemon
t1 . start()  #  t1  executes  function  f1()
t2 . start()   #  t2   also  executes  function  f1()
t3 . start()    #  t3   also  executes  function  f1()
print('main  thread  is  dead')




'''
1) How  many  non-daemon  threads  are  in  the  program ?  --->  3  i.e.  t1 , t2  and  main

2) Program  terminates  as  soon  as  non-daemon  threads  are  finished

3) PVM  does  not  wait  for  termination  of  t3  becoz  it  is  a  daemon  thread

4) PVM  kills  t3  as  soon  as  t1 , t2  and  main  are  dead

5) t1  and  t2  execute  for  loop  10  times  (guranteed)  becoz   they  are  non-daemon

6) t3  may (or) may  not  execute  for  loop  10  times  due  to  daemon  nature

7) When  is  error  not  reported  ?  ---> If   PVM  kills  sleeping  or  waiting  daemon  thread
    When  is  error  reported ?  ---> If  PVM  kills  ready  (or)  running  daemon  thread
'''