# Find  outputs
def   f1():
	try:
		return  10  #  finally  suite  is  executed  before  10  is   returned
	except:
		return   20
	else:
		return  30
	finally:
		return  40  #  40  is   returned  to  function  call  f1()
print(f1()) #   40