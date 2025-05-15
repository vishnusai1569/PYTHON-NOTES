

# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		#b = c1()   #  Executes  same  constructor  and  leads  to  recursion
# End  of  class
a = c1()  #  Executes  constructor  of  class  c1



'''
1) Where  can  object  be  created ?  ---> Any  where  in  the  program  except  in  constructor

2) What  is  the  issue  when  object  is  created   inside  the   constructor ? ---> Infinite  recursion
'''