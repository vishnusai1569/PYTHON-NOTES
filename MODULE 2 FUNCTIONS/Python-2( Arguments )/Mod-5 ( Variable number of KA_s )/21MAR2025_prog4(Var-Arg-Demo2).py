#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 10   <tab> b : (20 , 30 , 40)
f1(50 , 60) # a : 50  <tab>  b : (60,)
f1(70) # a : 70   <tab>  b : ()
f1(a = 80) # a : 80   <tab>  b : ()
#f1(b = (10 , 20 , 30) , a = 40) # error as var arg parameter cannot be a ka
f1() # a : 25   <tab>  b : ()
#f1(a = 10 , (20 , 30 , 40)) # error  due  to  pa  after  ka
#f1(25 , b = (10 , 20 , 30)) # error as var arg parameter cannot be a ka
#f1(25 , a = (10 , 20 , 30))  #   Errror  becoz  arg  is  passed  for  'a'  twice
f1((10 , 20 , 30) , 10 , 20 , 30)   #  a :  (10 , 20 , 30)  <tab>  b : (10 , 20 , 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)   #  error  due  to  pa  after  ka



'''
def   f1(a = 25  , *b):
        pass

1) f1(PA , KA)
    Is  the  above  function  call  valid ?  --->  No  becoz  'b'  can  not  be  KA  as  it  is  var-arg  parameter

2) f1(PA , PA)
    Is  the  above  function  call  valid ?  ---> Yes

3) f1(KA , PA)
    Is  the  above  function  call  valid ?  --->  No  becoz  PA  can  not  be  after  KA

4) What  is  the  final  conclusion ?  --->


Argument  before  var-arg  parameter  should  be  PA  only
'''
