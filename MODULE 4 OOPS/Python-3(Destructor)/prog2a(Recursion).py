# Find  outputs (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		b = c1()
    #  Executes same  class  destructor  before  object  'b'  is  lost  which  leads  to  recursion  (infinite  recursion)
a = c1()
#  Executes  destructor before  object  'a'  is  lost


'''
destructor
destructor
destructor
destructor
destructor
and so  on
'''

'''
1) Where  can  object   be  created ?  --->  Any  where  in  the  program  except  inside  constructor  and  destructor

2) What  is  the  dis-advantage  with  object  creation  in  destuctor ?  --->  Infinite  recursion
'''