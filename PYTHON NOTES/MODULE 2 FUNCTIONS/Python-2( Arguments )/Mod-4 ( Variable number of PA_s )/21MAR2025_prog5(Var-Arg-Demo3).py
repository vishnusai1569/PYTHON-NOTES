#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) # a : (10 , 20 , 30)  <tab> b : 40  
f1(50 , b = 60) # a = (50,) <tab> b = 60
f1(b = 70) # a : () <tab> b : 70
#f1(b = 10 , a = (20 , 30 , 40)) # error  becoz   'a'  cannot be a ka  as  it  is  var-arg  parameter
#f1(b = 10 , (20 , 30 , 40)) # error  due  to  pa  after  ka
#f1() # error  becoz  arg  is  not passed for  'b'
#f1(10 , 20 , 30 , (10 , 20 , 30))   #  'a'  is   (10 , 20 , 30 , (10 , 20 , 30))  and  error  becoz  arg  is  not  passed  for  'b'
#f1(10 , 20 , 30 , 40) #  'a'  is  (10 , 20 , 30  , 40)  and   error  becoz  arg  is  not  passed  for  'b'
#f1(25)  #  'a'  is  (25,)  and   error  becoz  arg  is  not  passed  for  'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30)) #   a : (10 , 20 ,  30)  <tab>  b : (10 , 20 , 30)




'''
1) def    f1(*a , b):
   	    pass
   Can  'a'  be  keyword  argument ?  --->  No  becoz  it  is  a  var-arg   parameter  and  hence  it  should  be  positional  argument  only
   Can  'b'   be  positional  argument ? --->  No  becoz  it  is  after  var-arg  parameter  and   hence  it  should  be  a  keyword  argument  only

2) What  is  the  issue  with  f1(10 , 20 , 30 , 40) ?  --->  'a'  is  (10 , 20 , 30 , 40)  and  no  argument  is  passed  for  'b'

3) What  is  the  order  of  arguments  to  call  f1()  function  ?  --->  f1(Any  number  of  PA's , KA)
'''
