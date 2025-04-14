#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x
		x +=  1
# End of  generator
g = f1()
print('Begin')  # Begin
print(*g)   #  Waiting  time  (or)  memory  error  due to   too  many  elements  in   generator 
print('End') # End
