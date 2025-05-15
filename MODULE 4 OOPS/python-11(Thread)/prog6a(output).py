# Find  outputs (Home  work)
from threading import *
t = current_thread()  #  Returns  main  thread object
print(t . name) # How  to  determine  name  of  main  thread  --->  MainThread
t . name = 'Hyd' # How  to  modify  name  of  main  thread  to   'Hyd'
print(t . name) # How  to  print  new  name  of  main  thread  ---> Hyd
child = Thread(name = 'Sec') # How  to  create  a  new  child  thread  with  name  "Sec"
print(child . name) # How  to  print  name  of  child  thread  --->  Sec
child . name = 'Cyb' # How  to  modify  name  of  child  thread  to   'Cyb'
print(child . name) # How  to  print  new  name  of  child  thread  --->  Cyb
print(active_count()) # How  to  determine  number  of  threads  under  execution  --->  1  becoz  child  thread  is  not started



'''
1) How  many  threads  are  in  the  program ?   --->  Just  one  thread i.e.  main  thread

2) Why  is  there  only  one  thread ?  --->   Since  child  thread  is  created  but  not  started
'''