

#  Find  outputs
import  time
from  importlib  import  reload
import   mod1   #   All  the  statements  of mod1  are  imported  and  executed
print('Program   sleeps  for  30  sec')
time . sleep(30)  #  Suspends  execution  for  30  sec
reload(mod1)  #  Executes  the  modified  mod1
print('End')  # End



'''
Modify  mod1  within  30  sec  after  execution  of  current  module
i.e.  Add  two  more  print  statements  to  mod1.py
'''