#  dir()  function  demo  program
print(dir(int))  # List  of  all  the  methods   of  int  class  and  environment  variables
print()
print()
print(dir(str))   # List  of  all  the  methods   of  str  class  and  environment  variables
print()
print()
print(dir([10 , 20 , 15]))   # List  of  all  the  methods   of  list  class  and  environment  variables



'''
dir()   function
------------------
1) What  does  dir(classname)  do ?  --->
					Returns  all  the  methods  of  the  class  in  the  form  of  list  of  strings  along  with  environment  variables

2) What  is  the  argument  of  dir()  function ?  --->  Either  class  name  (or)  object

3) Are  dir(25)  and  dir(int)  same ?  --->  Yes

4) Where  is  dir()  function  defined ?  ---> In  builtins  module
'''
