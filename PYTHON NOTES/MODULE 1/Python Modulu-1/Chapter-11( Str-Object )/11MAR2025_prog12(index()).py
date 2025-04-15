'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . index('is')  #  4
	while  True:
		print(index) #  4 , 23 , 42 , 46
		index = a . index('is' , index + 1)  #  23 , 42 , 46 , Error
except:
	print('End')



'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error  when  string  is  not  found  (but  not  -1)

Syntax  is  same  as   find()  method
'''
