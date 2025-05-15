#  Find  outputs  (Home   work)
def   f1():
	x = 10 #  Lv  of f1()
	def  f2():
		nonlocal   x  #  Treats  'x'  as  variable  of  f1()
		def  f3():
			nonlocal   x  #  Treats  'x'  as  variable  of  f1()
			print(x)  #  10
		f3()
	f2()
f1()
