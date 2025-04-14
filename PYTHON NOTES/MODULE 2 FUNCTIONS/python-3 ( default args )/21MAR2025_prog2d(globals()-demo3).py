# Find  outputs (Home  work)
def  f1():
	x = 20 #   Lv
	print(x) #  Lv  i.e.  20
	print(globals()['x']) #   Error  becoz  GV  'x'  does  not  exist  i.e.  {}['x']  throws error
# End  of  the  function
f1() 



'''
1) Which  variable  is  accessed  when  there  is  no  LV  ?  --->  GV

2) Which  variable  is  accessed  when  there  is  no  GV  ?  --->  Error
'''
