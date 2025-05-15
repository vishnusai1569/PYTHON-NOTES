# Find  outputs (Home work)
from  threading  import  *
main = main_thread() #   Returns  main  thread   object  which  was  already  created  by  pvm
name  =  main . name     #    Name  of   main  thread  i.e  MainThread
print(name , ' is started')  #  MainThread  is started
#main . join() # ERROR:  main  thread  waits  for  its  own  expiry  which  raises  an  error
print(name , 'is ended')  #  MainThread is ended



# A  thread  can  wait  for  expiry  of  a  different  thread  but  not  for  same  thread