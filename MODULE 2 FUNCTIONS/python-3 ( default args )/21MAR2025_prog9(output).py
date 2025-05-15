#  Find   outputs
def   f1():
	#x = x + 5  #  Error  becoz   LV  'x'   is  not  yet  initialized
	pass
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5  #   Creates  LV  with  value  10 + 5 = 15
	print(x) #   Lv  i.e.  15
# End of f2  function
x = 10 #  Gv  
f1()
f2()
print(x)  #  Gv  i.e.  10


'''
15
10
'''
