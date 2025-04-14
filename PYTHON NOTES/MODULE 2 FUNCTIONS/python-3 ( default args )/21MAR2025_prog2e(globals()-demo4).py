# Find outputs (Home  work)
def  f1():
	a = 40  # Lv
	b = 50 #   Lv
	c = 60  # Lv
	print(a , b , c) #  Lv's   i.e.  40 <space> 50 <space> 60
	dict = globals() #   {'a' : 10 , 'b' : 20 , 'c' : 30}
	print(dict['a'] , dict['b'] , dict['c']) #  Gv's  i.e.  10  <space>  20  <space>  30
	dict['a'] = 100  #    Modifies  Gv   'a'  to  100
	dict['b'] = 200   #    Modifies  Gv   'b'  to  200
	dict['c'] = 300   #    Modifies  Gv   'c'  to  300
def  f2():
	print(a , b , c) #   Gv's  i.e 100 <space> 200 <space> 300
# End  of  f2  function
a = 10  #  Gv
b = 20  # Gv
c = 30 #   Gv
f1() 
f2()



'''
40   50   60
10    20   30
100  200  300
'''
