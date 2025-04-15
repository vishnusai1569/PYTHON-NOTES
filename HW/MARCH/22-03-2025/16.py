#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
a = [f1 , f2]
for  x  in  a:
	     x()

#a = [def   f1():  print('Hyd') ,  def   f2():  print('Sec')]error
print(a)
a = [f1() , f2()]
print(a)
