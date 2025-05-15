# Find outputs (Home  work)
def  f1():
	global  a  #  Treats  'a'  as  GV  to  f1()  function
	a = 20 #   Modifies  GV  to  20
	print(a) #  Gv  i.e.  20
	print(globals()['a'])  #  Gv  i.e.  20
	a = 30  #   Modifies  GV  to  30
# End of the function
a = 10  #  Gv
print(a) #  Gv  i.e.  10
f1()
print(a) #   30

'''
10
20
20
30
'''
