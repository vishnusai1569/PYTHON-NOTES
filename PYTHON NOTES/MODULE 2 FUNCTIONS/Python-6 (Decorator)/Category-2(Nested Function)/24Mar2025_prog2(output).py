# Find  output(Home  work)
def    f1(a):  #  'a'  is  30
	def   f2():
		return  10  #  10  is   returned  to  function  call  f2()
	# End  of  f2  function
	return  f2() + 20 +  a  #   10 + 20 + 30 = 60  is   returned  to  function  call  f1(30)
# End  of  f1  function
print(f1(30))  # 60
