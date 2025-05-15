#  Find  outputs  (Home  work)
from  threading  import  RLock
r = RLock()  #  main  thread  creates  RLock  object
r . acquire()  #   main  thread  locks  object  'r'  for  the   1st  time
print('Locked')  #  Locked
r . acquire()  #   main  thread  locks  object  'r'  for  the   2nd   time
print('Locked') #  Locked
r . release()   #   main  thread  unlocks  object  'r'  for  the   1st  time
print('Unlocked') #  Unlocked
r . release()   #   main  thread  unlocks  object  'r'  for  the   2nd   time
print('Unlocked')  #  Unlocked
#r . release() # ERROR:   Can  not  unlock  as  it  is  not  locked  for  3rd  time
print('End')  #  End