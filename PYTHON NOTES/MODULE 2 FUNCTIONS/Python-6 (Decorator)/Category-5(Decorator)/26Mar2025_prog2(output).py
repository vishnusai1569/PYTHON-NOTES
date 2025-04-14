# Find  outputs(Home  work)
def   decor(fun):#  fun  is  wish
	print(fun . __name__)  #  wish
	def    inner(name):  #  name  is  'Java'
		if   name  == 'Python':
			print('Hello' , name) #   Hello  <space>  Python
		else:
			fun(name)  #  wish('Java')
	return  inner  #  Returned  to  function  call  decor(wish)
@decor  #   wish = decor(wish)  --->  wish =  inner  --->  wish  points  to  inner() function
def    wish(name): #  name  is  'Java'
        print('Hi' , name) #   Hi  <space>  Java
# End  of  the  function
wish('Python')  #   inner('Python')
wish('Java') #  inner('Java')


'''
wish
Hello  Python
Hi  Java
'''


'''
What  are  the  outputs  without  decoration ?  --->   Hi  Python
																		           Hi  Java
'''
