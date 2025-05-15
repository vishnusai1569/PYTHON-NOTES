#  Find  outputs (Home  work)
from  threading  import  *
import  time
def  f1():  #  Executes  by  thread  't'
	for  i  in  range(10):
		print('child  thread')
		time . sleep(2)
main = main_thread()  #  Returns  main  thread  object  created  by  pvm
print(main . daemon)  #  False  :  main  thread  is  always daemon
#main . daemon = True   #  Error :  main  thread  can  not  be  daemon  as  main  thread  execution  is  already  started
t = Thread(target = f1)    #  Creates  a  new  thread
print(t . daemon)  #  False :  The  thread  created  by  main  thread  is  always   non-daemon
t . daemon = True #   Thread  't'  is  converted  to  daemon
print(t . daemon)  #  True  :  Thread  't'  is  daemon
t . start()  #  Thread  't'  executes  function  f1()
#t . daemon = True  #  Error :  Thread  't'  can  not  be  daemon  as  execution  is  already  started  for  thread  't'
time . sleep(5)  #  main  threaad  sleeps   for  5  sec
print('End  of  main  thread') #  Executes  after  5  sec


'''
False
False
True
child  thread
child  thread
child  thread
End  of  main  thread


1) It  is  end  of  the  program  as  soon  as  main  thread(i.e. non-daemon)  is  finished

2) Thread  't'  does  not  execute  remaining  7  iterations  of  for  loop

3) Thread  't'  is  forcibly  killed  by  PVM  after  5th  sec
     i.e.  When  it  is  sleeping
'''