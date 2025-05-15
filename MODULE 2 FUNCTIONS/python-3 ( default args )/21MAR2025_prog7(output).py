# Find  outputs (Home  work)
def   f1():
	a = 20 #   Lv
	print(a)  # Lv  i.e.  20
def  f2():
	#print(a)  #  Error  becoz  LV  'a'  is not  yet  initialized
	#a += 1  #   a = a + 1   --->  Error  becoz  LV  'a'  on  rhs  is  not  yet  initialized
	pass
# End of the function
a = 10  # Gv 
print(a)  #  Gv  i.e. 10
f1()
a += 1  #  Increments  Gv  i.e.  11
f2()
print(a) #   Gv  i.e.  11

'''
10
20
11
'''
