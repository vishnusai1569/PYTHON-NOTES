# Find  outputs  (Home  work)
class   Thread: #  Discarded   becoz  Thread  class  is  imported  from  Threading  module
        def   run(self):
                for  i  in  range(10):
                        print('Child  Thread')
from  threading  import  Thread   #  Recognized
t = Thread()  #  Thread  class  object
t . start() #   Thread  't'  executes  empty run method  of  Thread  class
for  i  in  range(10):
        print('Main  Thread')  #  Main  Thread  10 times


'''
1) Which  class  is  recognized  when  multiple  classes  have  same  name ?  --->  Last  defined  class

2) Therefore  use-defined  class  Thread  is  discarded

3) Which  Thread  class  object  is  created  for  Thread() ?  --->
															Pre-defined  becoz  it  is  imported  after  user  defined  class
'''