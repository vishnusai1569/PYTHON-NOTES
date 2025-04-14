# Identify  error  (Home  work)
def  f4(* , a , b , c , /):   #  Error  :  Confusion  about  a , b and c  are  PA's  (or)  KA's
	        pass


'''
1) def  f1(a , b , c):
           pass
    What  can  be  passed  to  function  f1() ?  --->  Either  positional  arguments  (or)  keyword  arguments

2) def  f2(*, a , b , c):
            pass
    What  can  be  passed  to  function  f2() ?  ---> Keyword  only  arguments  becoz  a , b ,  c   are  after  *

3) def  f3(a , b , c , /):
            pass
    What  can  be  passed  to  function  f3() ?  --->  Positional  only  arguments  becoz   a , b , c  are  before  /

4) def  f4(* , a , b , c , /):
	        pass
    What  can  be  passed  to  function  f4() ?  ---> Ambiguity  error  becoz  a , b ,  c  are  after  *  and  before  /
'''
