# Find  outputs
def   f1(x ,  a  =  []):
	a . append(x)
	print('List  :  '  ,  a)
#End  of  the  function
print('__defaults__ : ' , f1 . __defaults__)  #  ([],)
f1(3) #   'x'  is  3 ,  'a'   is  default  value  []  , Result  is  [3]
print('__defaults__ : ' , f1 . __defaults__)  #   ([3],)
f1(5)  #   'x'  is  5 ,  'a'   is  default  value  [3]  , Result  is  [3 , 5]
print('__defaults__ : ' , f1 . __defaults__)  #  ([3 , 5],)
f1(6)  #   'x'  is  6 ,  'a'   is  default  value  [3 , 5]  , Result  is  [3 , 5 , 6]
print('__defaults__ : ' , f1 . __defaults__)  #  ([3 , 5 , 6],)
f1(10 , [20])  #   'x'  is  10 ,  'a'   is  [20]  , Result  is  [20 , 10]
print('__defaults__ : ' , f1 . __defaults__)  #  ([3 , 5 , 6],)



'''
1) When  is  __defaults__  modified ?  --->  As  soon  as  default  argument  is  modified  by  the  function

2) How  is  __defaults__  modified  when  default  argument  is  modified  ?  ---> Since  they  point  to  same  object

3) When  is  __defaults__  remains  unchanged  ?  --->  When  actual  parameter  is  modified

4) What  is  the  use  of  __defaults__ ?   --->  Default  values  are  fetched  from  __defaults__
'''
