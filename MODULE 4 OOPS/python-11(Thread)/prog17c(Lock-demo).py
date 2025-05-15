# Find  outputs  (Home  work)
from threading import *
l = Lock()  # main  thread  creates  Lock  object
l . acquire()  #  main  thread locks  object  'l'
print('Locked')  # Locked
l . acquire() #  main  thread  waits  as  object  'l'  is  already   locked
print('Locked')    #  Not  executed  becoz  main  thread is  waitimg
l . release()
print('Unlocked')
l . release()
print('Unlocked')
print('End')