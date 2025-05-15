# Find  outputs  (Home  work)
from threading import *
class    MyThread(Thread):
        def   run(self):
                for  i  in  range(10):
                        print('child  thread')
#end of the class
child = MyThread()  # A new  thread  is  created
child . run()    #   Method  call  to  run()  method  but  not  thread  execution
for  i  in  range(10):
        print('main  thread')


'''
1) How  many  threads  are  in  the  program ?  --->  Single  thread  i.e. MainThread

2) Why  is  there  single  thread ?  --->  Since  child  thread  is  created  but  not  started

3) What  are  the  outputs  of  program ?  --->   10  times  child  thread
																	        10  times  main  thread

4) Are  outputs  same  for  every  run ?  --->  Yes  due  to  single  thread

5) child = MyThread()
     child . start()
     child . run()
     Who  is  executing  run()  method  wrt  child  . start() ? --->  Child  Thread
     Who  is  executing  run()  method  for  child . run()  ? --->  main  thread  becoz  program  is  executed  by  main  thread
'''