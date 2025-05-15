# Find outputs (Home  work)
def  f1():
	global   a #  Treats  'a'  as  Gv  to  f1()  function
	a = 10  #   Creates  GV  with  value  10
	print(a) #  Gv  i.e.  10
	a = 20  #  Modifies  GV  to  20
def  f2():
	global  a  #  Treats  'a'  as  Gv  to  f2()  function
	print(a) # GV  i.e.  20
	a = 30   #  Modifies  GV  to  30
def  f3():
	print(a)  #   Gv  i.e.  30
	globals()['a'] = 40    #  Modifies  GV  to  40
# End  of  the  function
f1()
f2()
f3()
print(a)  #  Gv  i.e.  40

'''
10
20
30
40
'''
