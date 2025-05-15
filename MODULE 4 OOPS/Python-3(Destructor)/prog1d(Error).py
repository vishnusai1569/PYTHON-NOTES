# Identify  Error (Home  work)
class   c1:
	def  __del__(self , x):
		print('destructor : ' , x)
a = c1()
a . __del__(25)  #  Executes  destructor  and   x  is  25
#  Error becoz  arg  is  not  passed  for  destructor


'''
1) Can  destructor  have  an  argument ?  --->  Yes  for  explicit  call  and  throws  error   when  destructor
                                                                         is  executed  automatically

2) Why  automatic  execution  throws  error ?  --->  Since  arg  can  not  be  passed  for  automatic  executionn

3) What  is  the  issue  when  constructor  returns  non-None ?  --->  Object  creation  throws  an  error
'''