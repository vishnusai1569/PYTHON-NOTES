# Find  outputs  (Home  work)
from  threading  import  *
def   f1(x):
	s = current_thread() . name
	while   True:
		print(s , ' : ' , x)
t1 = Thread(target = f1 , name = 'Hyd' , args = (10,))
t2 = Thread(target = f1 , name = 'Sec' , args = [20])
t1 . start()  #  t1  executes  f1(10)
t2 . start()   #  t2  executes  f1(20)
print(active_count())  #   3
print('Press  ctrl + break  or  Fn + b  to  stop ')



'''
1) Which  of  the  following  are  valid ?
    args = [10]  --->  Valid  due  to  sequence
    args = (10,) --->  Valid  due  to  sequence
    args = {10}  --->  Valid  due  to  sequence
    args = 10   --->  Invalid  becoz  10  is  not  a  sequence
    args = 10.8 ---> Invalid  becoz  10.8  is  not  a  sequence
    args = '10'  --->  Invalid  when  function  has  single  argument  and  valid  when  when function  has  2  args
                              becoz  '10'  has  2  characters
    args = (10)  --->  Invalid  becoz  10  is  not  a  sequence

2) In  general,  args  argument  of  Thread  constructor  can  be  any  sequence

3) How  to  kill  multi-thread  execution ? --->  ctrl + break  (or) Fn + b
    How  to  kill  single  thread  execution ? ---> ctrl + c

4) Which  thread  is  first  executed  between  t1  and  t2  ?  --->  t1  becoz  it  is  started  before  t2

5) How  many  threads  are  in  the  above  program ? --->  3  i.e.  main  thread , t1  and  t2

6) What  does  main  thread  do  ?  --->  Creates  2  threads  t1  and  t2  and  starts  both  of  them
    What  does  thread  t1  do  ?  --->   Prints  Hyd  :  10  infinite  number  of  times  due  to  while  True:
    What  does  thread  t2  do  ? --->  Prints   Sec  :  30  infinite  number  of  times  due  to  while  True

7) Are  t1  and  t2   finite  threads  (or)  infinite ?  --->  Infinite  due  to  while  True:
    What  about  main  thread  ?  --->  Finite  thread

8) Are  t1  and  t2  sharing  same  local  variable  's'  ?  --->  No  and  each  thread  has  a  different  local  variable  's'

Note:
t1   prints   Hyd :  10  for  15  times  and  time  is  elapsed
t2   prints   Sec :  30  for  12  times  and  time  is  elapsed
t1   resumes  16th  iteration  and  prints   Hyd :  10  for  7  times  and  time  is  elapsed
t2   resumes  13th  iteration  and  prints   Sec :  30  for  9  times  and  time  is  elapsed
t1   resumes  24th  iteration  and  prints   Hyd :  10  for  2  times  and  time  is  elapsed
t2   resumes  23th  iteration  and  prints   Sec  :  30  for  4  times  and  time  is  elapsed
and  so  on
'''