# Find  outputs (Home  work)
from  threading  import  Thread , current_thread
from  random  import  randint
def   f1(n):
	ctr = 0
	s = current_thread() . name
	while  True:
		x = randint(1 , 100)
		ctr += 1
		print(F'{s}  guess  {x}   in  attempt  :  {ctr}')
		if   x ==  n:
			break
	#end of while loop
	print(F'{s}  finish  in  {ctr}  attempts')
t1 = Thread(target = f1 , args = [75] , name = 'Rama')
t2 = Thread(target = f1 , args = [50] , name = 'Sita')
t1 . start()  # t1  executes  f1(75)
t2 . start()  # t2  executes  f1(50)



'''
1) How  many  threads  are  in  the  program ? --->  3  i.e.  main  thread , t1  and  t2

2) What  does  thread  t1  do ?  --->  Generates  random  numbers  continuously  until  75
     What  does  thread  t2  do ?  ---> Generates  random  numbers  continuously  until  50

3) Both  t1  and  t2  have  separate  local variables  ctr , s  and  x

4) t1  generates  random  numbers  except  75   and  time  is  elapsed
    (Let  while  loop  be  executed  10   times)
    t2  generates  random  numbers  except  50   and  time  is  elapsed
    (Let  while  loop  be  executed  12   times)
    t1  resumes  from  where  it  left  off  i.e.  t1  resumes  from  11th  iteration
    t1  generates  random  numbers  except  75   and  time  is  elapsed
    (Let  while  loop  be  executed  7  times)
    t2  resumes  from  where  it  left  off  i.e.  t2  resumes  from  13th  iteration
    t2  generates  random  numbers  except  50   and  time  is  elapsed
    (Let  while  loop  be  executed  9  times)
    t1  resumes  from  where  it  left  off  i.e.  t1  resumes  from  18th  iteration
    t1  generates  random  numbers  except  75   and  time  is  elapsed
    (Let  while  loop  be  executed  15  times)
    t2  resumes  from  where  it  left  off  i.e.  t2  resumes  from  22nd  iteration
    t2  generates  random  numbers  except  50   and  time  is  elapsed
    (Let  while  loop  be  executed  13  times)
    This  process  continues  until  t1  generates  random  number   75  and  t2  generates  random  number   50
'''