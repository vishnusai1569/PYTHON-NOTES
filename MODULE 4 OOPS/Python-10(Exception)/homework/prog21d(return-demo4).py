
# Find  outputs
def   f1():
	try:
		pass
	except:  # Skipped  due  to  no  error
		return  20
	else:  #  Executed  :   try  suite  is  not  raising  an   error
		return  30  #  30  is   returned   to  function  call  f1()
print(f1()) # 30