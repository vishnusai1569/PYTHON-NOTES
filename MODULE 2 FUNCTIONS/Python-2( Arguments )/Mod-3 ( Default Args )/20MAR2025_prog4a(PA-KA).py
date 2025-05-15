# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)  #  a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)  #  Error :  KA  b = 2  is  not  permitted  due  to  /
#f1(1 , 2 , 3 , 4 , 5 , f = 6) #  Error :  PA   5  is  not  permitted  due  to  *
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)  #  Error :  PA  40  is  not  permitted   after  KA  c = 30
f1(10 , 20 , 30 , 40 , e = 50 , f = 60)  #  a  :  10          b  :  20        c  :  30        d  :  40        e  :  50        f  :  60


'''
def  f1(a , b , / , c , d , * , e  , f):
	      pass
1) Which  arguments  can  be  passed  for  'a'  and  'b' ?  ---> Positional  only  arguments  becoz  they  are  before  /

2) Which  arguments  can  be  passed  for  'e'  and  'f' ?  --->  Keyword  only  arguments  becoz  they  are  after  *

3) Which  arguments  can  be  passed  for  'c'  and  'd' ?  --->  Either  positional  arguments  (or)  keyword  arguments  becoz
				                                                                                  they  are  not  before  /  nor  after  *
'''
