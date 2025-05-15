# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))

'''
([10 , 20] , {30 , 40} , (50 , 60))
<class 'tuple'>
[10 , 20]
<class 'list'>
{30 , 40} can be any order
<class 'set'>
(50 , 60)
<class 'tuple'>
'''


'''
Iteration           x             type(x)
-----------------------------------------
      1                 [10 , 20]       <class  'list'>
      2                {30 , 40}       <class  'set'>
      3                (50 , 60)       <class  'tuple'>
'''
