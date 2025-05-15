# Find  outputs (Home  work)
from  threading  import  *
main = current_thread()   #  Returns  main  thread   object
t1 = Thread(name = 'Hyd') # How  to  create  a  thread  with  name  'Hyd'
t2 = Thread() # How  to  create  another  thread  without  a  name
print(main . name) # How  to  print  name  of  main  thread
print(t1 . name) # How  to  print  name  of  thread  t1
print(t2 . name) # How  to  print  name  of  thread  t2
main . name = 'India' # How  to  modify  name  of  main  thread  to  'India'
t1 . name = 'Sec' # How  to  modify  name  of  thread  t1  to  'Sec'
t2 . name = 'Cyb' # How  to  modify  name  of  thread  t2  to  'Cyb'
print(main . name) # How  to  print  name  of  main  thread
print(t1 . name) # How  to  print  name  of  thread  t1
print(t2 . name) # How  to  print  name  of  thread  t2
print(active_count()) # 1

'''
MainThread
Hyd
Thread-1
India
Sec
Cyb
1
'''