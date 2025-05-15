
# Find  outputs
def   f1():
	try:
		return  10 + '20'  #  Throws  TypeError  due  to   invalid  operands
	except:
		return  20  #  20  is   returned  to  function  call  f1()
	else:
		return  30
print(f1()) # 20