'''  (Home  work)
index()  method  demo  program

Modify  the  following  program  with  index()  method

Hint: Use   try  and  except
'''
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . index('is')
	while  index != -1:
		print(index)
		index = a .index('is' , index + 1)
	print('End')
except ValueError:
	print("substring not found")




'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error  when  string  is  not  found  (but  not  -1)

Syntax  is  same  as   find()  method
'''