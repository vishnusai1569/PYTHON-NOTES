# Find  outputs
def   f1():
	try:
		return  10    #  10  is  returned  to   function  call  f1()  and  moves  out  of  the  function
	except: #  Skipped  due  to  no  error
		return  20
	else:  #  Skipped  due  to   return  10
		return  30
print(f1()) # 10

'''
Both   except  and  else  suites  are  not  executed  due  to   return  10
'''