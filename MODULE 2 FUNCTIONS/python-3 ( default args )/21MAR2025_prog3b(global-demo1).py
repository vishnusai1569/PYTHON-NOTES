# global  keyword  demo  program (Home  work)
def    f1():
	x = 20  #   Lv
	print(x)  #  LV  i.e.  20
def   f2():
	global  x   #  Treats  'x'  as  GV  to f2()  function
	x = 30  #   Modifies  Gv  to  30
	print(x)  #  Gv  i.e.  30
	x += 1  #  Increments  GV  i.e. 31
def   f3():
	global  y   #  Treats  'y'  as  GV  to f3()  function
	y = 40  #   Creates  GV  with  value  40
	print(y)  #  Gv  i.e.  40
	y += 1  #  Increments  GV  i.e. 41
def   f4():
	x = 50  #   Creates  a  LV  with  value  50
	#global   x  #  Error  becoz  there  is  already  LV  with  name  'x'
#  End  of  the  functions
x = 10 #   Gv
print(x)  #  Gv  i.e.  10
x += 1  #  Increments  Gv  i.e.  11
f1()
print(x)  #  Gv  i.e.  11
f2()
print(x)  #  Gv  i.e.  31
x += 1   #  Increments  Gv  i.e.  32
f3()
print(y)  #  Gv  i.e.  41
f4()
print(x)  #   GV  i.e.  32

'''
10
20
11
30
31 
40
41 
32
 '''
