'''
1) What  are  the  outputs  for  t1 . start() ?  --->  10  times  f1  function

2) What  are  the  outputs  for  t2 . start() ?  --->  10  times  m1  method  of  class  c1

3) What  are  the  outputs  for  t3 . start() ?  --->   Nothing

4) What  are  the  outputs  for  t4 . start() ?  --->  10  times  run   method  of  MyThread  class

5) What  are  the  outputs  for  t5 . start() ?  --->  10  times  run   method  of  MyThread  class

6) What  are  the  outputs  for  t6 . start() ?  --->  10  times  f1  function

7) What  are  the  outputs  for  t7 . start() ?  --->   Nothing

8) What  are  the  outputs  for  t8 . start() ?  --->  10  times  run   method  of  MyThread  class

9) What  are  the  outputs  for  t9 . start() ?  --->  10  times  m1  method  of  class  c1

10) What  are  the  outputs  for  t10 . start() ?  --->  10  times  run   method  of  MyThread  class

11) What  are  the  outputs  for  t11 . start() ?  --->   Nothing

12) What  are  the  outputs  for  t12 . start() ?  --->  10  times  m1  method  of  MyThread  class

13) What  are  the  outputs  for  t13 . start() ?  --->  10  times  f1  method  of  class  c1
'''
from  threading  import  *
class  MyThread(Thread):
        def  run(self):
                for  i  in  range(10):
                        print('run   method  of  MyThread  class')
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  MyThread  class')
class  c1(Thread):
        def  m1(self):
                for  i  in  range(10):
                        print('m1  method  of  class  c1')
        def   f1(self):
                 for  i  in  range(10):
                         print('f1  method  of  class  c1')
# end of class
def   f1():
        for  i  in  range(10):
                print('f1  function')
#end of f1 function
t1 = Thread(target = f1)
t2 = Thread(target = c1() . m1)
t3 = Thread()
t4 = MyThread()
t5 = MyThread(target = f1)
t6 = c1(target =  f1)
t7 = c1()
t8 = MyThread(target = c1() . m1)
t9 = c1(target = c1() . m1)
t10 = MyThread(target = t4 . run)
t11 = c1(target = t7 . run)
t12 = c1(target = t4 . m1)
t13 = c1(target = t7 . f1)
# Run  with  any  one  of  the  following  stmts
#t1 . start()  #   t1  executes  function  f1  becoz  target  is  f1
#t2 . start()   #   t2  executes  method  m1  of  class   c1  becoz  target  is  c1() . m1
#t3 . start()  #   t3  executes  empty  run()  method of  Thread  class   becoz   there  is  no   target
#t4 . start()  #   t4  executes  run()  method of  MyThread  class
#t5 . start()   #   t5  executes  run()  method of  MyThread  class   and  ignores  target
#t6 . start()   #   t6  executes  function  f1  becoz  there  is  no  run()  method  in  class  c1
#t7 . start()    #   t7  executes  empty   run()  method  of  Thread  class   becoz  there  is  no  run()  method  in  class  c1  and  also  there  is  no  target
#t8 . start()  #   t8  executes  run()  method of  MyThread  class   and  ignores  target
#t9 . start()  #   t9  executes  method  m1  of  class   c1  becoz   there  is  no  run()  method  in  class  c1
#t10 . start()   #   t10  executes  run()  method of  MyThread  class   and  ignores  target
#t11 . start()  #   t11   executes  empty   run()  method  of  Thread  class   becoz  there  is  no  run()  method  in  class  c1
#t12 . start()   #   t12  executes  method  m1  of   MyThread  class   becoz   target  is   m1()  method  of   MyThread  class
t13 . start()   #   t13  executes  method  f1  of   class  c1   becoz   target  is   f1()  method  of   class  c1