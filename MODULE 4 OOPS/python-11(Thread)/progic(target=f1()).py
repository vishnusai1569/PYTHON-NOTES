#  Find  outputs  (Home  work)
from  threading  import   Thread
def  f1():
        for  i  in  range(10) :
                print('child  thread')
child = Thread(target =  f1())  #    Executes  f1()  function  and  target = None
child . start()   # child  thread  does  nothing  becoz  target is  None
for  i  in  range(10):
        print('main  thread')



'''
1) What  does  target = f1()  do ?  --->  Executes  f1()  function  due  to  ()

2) What  is  the  target  ?  --->  None  becoz  f1()  function  returns  None  by  default

3) What  does  child  thread  do  ?  --->  Nothing  becoz  target  is  None

4) How  many  threads  are  in  the  program ? --->  Two  threads

5) What  are  the  outputs ?  --->  10   times  child  thread
													  10   times  main  thread

6) Are  outputs  same  for  every  run  ?  --->  Yes  becoz  child  thread  is  not  doing  anything

7) Finally,  what  is  the  morale ?  --->  target  should  be  f1  but  not  f1()
'''