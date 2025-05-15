#  Same  as   prog11c  except  if  statement
def   f1(x  ,  a  =  []):
	if  a ==  []:
		a = []   #   Ref  'a'  points  to  local  list  i.e.  []
	a . append(x)
	print('List  :  '  ,  a)
#  End  of  the  function
print('__defaults__  :  ' , f1 . __defaults__)  #  ([],)
f1(3)  #  'x'  is  3 ,  a   is  default  value  [] , result  is  [3]
print('__defaults__  :  ' , f1 . __defaults__)  #   ([],)
f1(5)  #  'x'  is   5  ,  a   is  default  value  [] , result  is  [5]
print('__defaults__  :  ' , f1 . __defaults__)  #   ([],)
f1(6)   #  'x'  is   6  ,  a   is  default  value  [] , result  is  [6]
print('__defaults__  :  ' , f1 . __defaults__)  #   ([],)
f1(10 , [20])    #  'x'  is   10  ,  a   is    [20] , result  is  [20 , 10]
print('__defaults__  :  ' , f1 . __defaults__)  #   ([],)



'''
1) if  a == []:
	     a = []
    What  does  the  above  if  statement  do ?  --->  Creates  a  local  list  when  2nd  argument  is  not  passed  to  the  function

2) a . append(x)
    What  is  modified  (Local  list  (or)  default  argument  list) ?  --->  Local  list  but  not  default  argument  list

3) Why  is   __defaults__   remains  unchanged ?  --->  When  local  list  and  actual  parameter  are  modified
'''
