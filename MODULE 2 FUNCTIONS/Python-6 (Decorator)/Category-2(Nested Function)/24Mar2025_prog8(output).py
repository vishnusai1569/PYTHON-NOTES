# Find  outputs (Home  work)
def  outer():
	a = 10 #  Lv  of  outer()  function
	b = 20  #  Lv  of  outer()  function
	def   inner():
		nonlocal   a  #  Treats  'a' as  variable  of  outer()  function
		a = 100  #  Modifies  Lv  of  outer()  function  to  100
		b = 200  #   Creates  Lv  of   inner()  function
		print(a , b)  #  100  <space>  200
	# End  of  inner  function
	print(a , b)  #  10  <space>  20
	inner()
	print(a , b)  #  100  <space>  20
#end of outer function
outer()



'''
10      20
100    200
100    20
'''

'''
1) How  many  LV's  are  in  outer()  function ?  --->  Two

2) How  many  LV's  are  in  inner()  function ?  ---> One  i.e.  'b'
'''
