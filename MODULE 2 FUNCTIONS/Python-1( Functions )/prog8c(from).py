# How  to  call  function  f1()  of  prog8a  using  from  statement ?
from  prog8a  import  f1  as  f2  #  How  to  import  function  f1()  of  prog8a  module  with  from  statement
def   f1():
	print('Function  of  prog8c')
f2() #  How  to  call  function  f1()   of  prog8a
f1()  #  How  to  call  function  f1()   of  prog8c (i.e. current  program)



'''
1) from   prog8a  import  f1  as  f2
    What  does  above  statement  do ? ---> 	Imports  function  f1  from  module  prog8a  with  a  new  name  f2

2) What  is  this  process  called ?  --->  Member  alias

3) from   prog8a  import  f1
    What  is  the  issue  if  member  alias  is  not  made ?  --->
									Imported  function  f1()  is  discarded  becoz  another  function  is  defined  with  same  name

4) from   prog8a  import  f1()
    Is  the  above  statement  valid  ?  ---> No  due  to  ()
'''
