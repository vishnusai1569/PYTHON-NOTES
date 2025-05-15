#  Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
child = Thread(target = f1)  # A  new  thread  is  created
f1()  #  Function  call  to  f1()  but  not  a  thread
for  i  in  range(10):
        print('main  thread')


'''
1) How  many  threads  are  in  the  program ? --->    Single  thread  i.e. MainThread

2) Why  is  there  only  single  thread ?  --->  Since  child  thread  is  created  but  not  started  and
						 											   hence  it  is   not  treated  as  a  thread

3) What  are  the  outputs  of  program ?  --->  10  times  child  thread
                                                                           10  times  main  thread

4) Are  outputs  same  for  every  run  ?  --->  Yes  due  to  single  thread  in  the  program

5) Finally,  do  not  call  f1()  function  directly  instead   start  the  thread  with  child . start()

6) child = Thread(target = f1)
     child . start()
     f1()
     Who  is  executing  f1()  function  wrt  child . start() ? --->  Child  thread  becoz  it  is  started
     Who  is  executing  f1()  function  wrt  f1()  ? --->  main  thread  becoz  program  is  executed  by  main  thread
'''