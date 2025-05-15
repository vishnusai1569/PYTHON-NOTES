# Find  outputs
def   f1():
	try:
		return  10 + '20'  #   raises  TypeError
	except:
		return  10 + 20 #   30
print(f1())  #  print(30)
