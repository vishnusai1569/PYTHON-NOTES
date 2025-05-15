#  Find  outputs  (Home  work)
def    f1():
        print('f1    function')
def    f2():
        print('f2  function')
# End  of  the  function
f1()  # Executes  function  f1()
f2()  # Executes  function  f2()
print(f1  is  f2)  #   False  :  f1  and  f2  point  to  different  functions
f2 = f1  #  Ref f2  points to  function  f1
f2()  #   # Executes  function  f1()  becoz  f2  points  to  function f1
print(f1  is  f2)  #   True  :  f1  and  f2  point  to  same  function
f2 = f1()   #  Executes  function  f1  which  returns  None  by default  i.e.  f2 = None
print(f2)  #  None
print(type(f2))  #  <class  'NoneType'>
#f2()  #  None()  throws  error  as  None  is  not  a  function

'''
f1    function
f2  function
False
f1    function
True
f1    function
None
<class 'NoneType'>
'''


'''
def   None():
	pass
Can  function  name  be  None  ?   --->  No  becoz  function  name  can  not  be  a  keyword  such  as  None
'''
