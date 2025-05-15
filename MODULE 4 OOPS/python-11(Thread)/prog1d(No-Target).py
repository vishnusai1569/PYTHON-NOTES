# Find  outputs  (Home  work)
from  threading  import  *
def   f1():
        for  i  in  range(10):
                print('child  thread')
child = Thread()
child . start()  #  child  thread  executes  empty   run()  method  of  Thread  class
for  i   in   range(10):
        print('main  thread')



'''
1) How  many  threads  are  in  the  program  ? --->  Two  threads

2) What  does  child  thread   do ?  --->  	Executes  empty  run()  method  of  Thread  class  becoz  there  is  no  target

3) What  are  the  outputs ?  --->  10  times  main  thread

4) Are  outputs  same  for  every  run  ?  --->  Yes   becoz   child  thread  executes  empty  run()  method  of  Thread  class

5) Finally,  what  is  the  morale ? --->  Specify  the  target
'''