

# time()  function  demo  program
import   time
begin = time . time()  #   Current  time  before  execution  of  for  loop
for  i  in  range(10):
        print(i)  #  Do  nothing
end = time . time()   #   Current  time  after  execution  of  for  loop
print(end - begin) #   for  loop  execution  time



'''
time()  function
------------------
1) What  does  time()  function  do ?  --->
												Returns  current  time  in  seconds  since  1 . 1 . 1970  midnight (which  is  called  epoch  time)

2) What  is  the  result  of  time()  function  ?  --->  55 * 365 * 24 * 60 * 60  (Approx)

3) Where  is  time()  function  defined ?  --->  In  time  module

4) a = time . time()  --->  Current  time  before  execution  of  100  statements
    100  statements
    b = time . time()  --->  Current  time   after  execution  of  100  statements
    What  is  b - a ?  --->  Execution  time  of  100   statements

5) a = time . time()  --->   Current  time  before  execution  of  f1()  function
    f1()
    b = time . time()  --->    Current  time  after  execution  of  f1()  function
    What  is  b - a ?  --->  Execution  time  of  f1()  function

6) a = time . time()
    if stmt / match  stmt / for loop / while loop
    b = time . time()
    What  is  b - a ?  ---> Execution  time  of  if / match / for / while

7) It  is  possible  to  determine  execution  time  of
    a) A  group  of  statements
    b) if  statement
    c) match  statement
    d) for  loop
    e) while  loop
    f) function
    g) program
'''