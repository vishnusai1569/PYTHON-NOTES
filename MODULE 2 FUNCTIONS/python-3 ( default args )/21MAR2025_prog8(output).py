# Find outputs (Home  work)
def  f1():
	a = 20 #   Creates LV  with  value  20
	#global   a # error  becoz  there is already local varible  with  name  'a'
	print(a)  #  Lv  i.e.  20
	print(globals()['a'])  #  Gv  i.e.  11
	a = 30  #   Modifies  Lv  to  30
	globals()['a'] = 40  #   Modifies   Gv  to  40
#  End  of  f1()   function
a = 10  #  Gv
print(a)  # Gv  i.e.  10
a += 1  # Increments  Gv  i.e.  11
f1()
print(a) #   Gv  i.e.  40

'''
10
20
11
40
'''
