# Find outputs (Home  work)
def  f1():
	global   a #   Treats  'a'  as  Gv  to  f1()  function
	a = 10  # Creates  Gv  with  value  10
	print(a) #   GV  i.e. 10
	a = 20  # Modifies  GV  to  20
def  f2():
	#print(a) #   Error becoz  LV 'a' is  not yet  initialized
	a = 30  #  Creates  LV  with  value  30
	print(a)  #   Lv  i.e.  30
def  f3():
	print(a)  #  Gv  i.e.  20
	globals()['a'] = 40  # Modifies  GV  to  40
# End  of  the  function
f1()
f2()
f3()
print(a)  #  Gv  i.e.  40

'''
10
30
20
40
'''
