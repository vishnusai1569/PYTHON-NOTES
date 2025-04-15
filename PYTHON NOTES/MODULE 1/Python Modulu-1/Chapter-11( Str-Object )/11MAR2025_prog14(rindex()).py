'''  (Home  work)
rindex()   method  demo  program

Modify  following  program  with  rindex()  method

Hint: Use   try  and  except
'''
try:
	a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
	index = a . rindex('is')
	while  True:
		print(index)
		index = a . rindex('is' , 0 , index)
except:
	print('End')


'''
rindex()  method
--------------------
It  is  same  as   rfind()  method  except  that  it  throws  error   but  not  -1  when  string  is  not  found
'''



'''
Note:
1) Which  methods  search  from  left  to  right ?  --->


find()  and  index()  methods
    Which  methods  search  from  right  to  left  ?  --->


	rfind()  and  rindex()  methods

2) Which  methods  return  -1  when  string  is  not  found ? --->


find()  and  rfind()
     Which  methods  throw  error  when  string  is  not  found ? --->


	 index()  and  rindex()
'''
