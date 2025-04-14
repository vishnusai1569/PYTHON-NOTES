# Find  outputs(Home  work)
'''
def   add(a = 10 , b , c):  #  Error  due  to  non-default  arg  after  default  arg
        pass
'''
def   add( * , a = 10 , b , c ):  #   Non-default  arg  is  permitted  after  default  arg  due  to  *
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) #  a = 30  , b = 40 , c  = 50  and  result  = 120
print(add(b = 60 , c = 70)) # a is default  value  10 , b = 60 , c = 70  and  result  =   140
print(add(c = 80 , b = 90 , a = 100)) # a is 100  , b is 90 ,  c is 80  and  result = 270
#print(add(c = 25 , a = 43)) # error  becoz  arg  is  not  passed  for  'b'
#print(add(1 , 2 , 3)) # error due  to  pa's
'''
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):  # error  due  to  non-default   'c'  after  default  arg  b = 10
		pass
'''

'''
What  are  the  two   advantages  of  *  in  the  function  header ?  ---> 1) Argument  should  be  KA's  only
												   2) Non-default  arguments  and  default  arguments  can  be  in  any  order
'''
