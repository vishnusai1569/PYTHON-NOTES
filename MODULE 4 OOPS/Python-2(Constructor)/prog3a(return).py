# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
#a = c1()  #  Error  due  to  return  25  in  the  constructor
b = c2()  #   Executes  constructor of  class  c2
print(b) #  Type   and  address  of   object  'b'
print(b . __init__())  #   Executes  constructor of  class  c2  which  returns  None
c = c3()   #   Executes  constructor of  class  c3
print(c . __init__())  #   Executes  constructor of  class  c2  which  returns  None


'''
c2  class  constructor
Type   and  address  of   object  'b'
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None
'''



'''
1) What  can  constructor  return ?  --->  Nothing  except  None

2) Where  is  None  returned  to ?  --->  Constructor  call  when  it  is  called  explicitly  and
															    ignored  when  it  is  automatically  executed

3) How  to  prevent  object  creation ?  --->  Return  any  object  other  than  None  in  constructor
'''