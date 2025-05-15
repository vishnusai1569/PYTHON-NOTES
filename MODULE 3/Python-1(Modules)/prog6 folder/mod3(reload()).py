

# reload()  function  demo  program
import    importlib
import  mod1    #  3  statements  are  imported
print()
importlib . reload(mod1) #   Statements of  mod1  are  executed  due to  reload()
print()
importlib . reload(mod1)  #   Statements of  mod1  are  executed  due to  reload()
#importlib . reload('mod1')   #  Error  due  to  string  module
#reload(mod1)  #   Error :  No  reload()  function  in  current  module



'''
reload()   function
----------------------
1) What  does  reload(module)  do ?  --->
								Loads  the  module  into  memory  and  thereby  all  the  statements  of  module  gets  executed

2) What  is  the  argument  of  reload()  function ?  ---> The  module  to  be   loaded

3) Can  module  be  reloaded  with  load (i.e.  import) ?  --->  No  i.e.  load  (i.e.  import) the  module  first  and  then  reload

4) Where  is  reload()  function  defined ?  --->  In  importlib  module

5) importlib . reload('mod1')
    Is  the  above  statement  valid  ?  --->  No  becoz  argument  should  be  module  but  not  string  module

6) What  is  the  use  of  reload()  function ?  --->  When  same  module  needs  to  be  imported  again,  use  reload()  function

7) run_module('mod1')
    reload(mod1)
    What  is  the  difference  between  the  above  two  statements ?  --->
	a) run_module('mod1')  --->  mod1  need  not  be  imported  becoz   argument  is  a  string  module
	b) reload(mod1)  --->   mod1  has  to  be  imported  becoz   argument  is  a   module
'''