# Identify  error  (Home  work)
from  threading  import  Thread   #   Discards  Thread   class  becoz  another  class  is  defined  with  same  name
class   Thread:   #  Regular  class  but  not  Thread  class   becoz  it  is   not  a  child  class  of   Thread
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
# End of the class
t = Thread()  #  Regular  python  class  object
t . start()   #  Error  becoz  there   is   no  start()  method  in  user  defined  Thread  class
for  i  in  range(10):
        print('main  thread')


'''
1) Which  class  is  recognized  when  multiple  classes  have  same  name ?  --->  Last  defined  class

2) Therefore  pre-defined  class  Thread  is  discarded  becoz  another  class  is  defined  with  same  name

3) Which  class  object  is  created  for  Thread() ?  --->  Used-defined  Thread  class  object  becoz
																						   it  is  defined  after importing  pre-defined  class  Thread
'''