#Find  outputs (Home  work)
a = 10  #   GV
def   f1():
	b = 40  #   Lv  
	print('a : ' , a)  #  GV  i.e.  11
	print('b : ' , b)  #  Lv  i.e  40
	print('c : ' , c)  #   Gv  i.e.  31
	print()
# End  of  f1()  function
b = 20  #  Gv
def    f2():
	a = 50  #  Lv
	print('a : ' , a) #   Lv  i.e.  50
	print('b : ' , b)  #  Gv i.e.  22
	print('c : ' , c)  #  Gv  i.e.  32
# End  of  f2()  function
c = 30  #  Gv
print('a : ' , a) #  Gv  i.e.  10
print('b : ' , b) #  Gv  i.e. 20
print('c : ' , c) #  Gv  i.e.  30
print()
a +=  1 #  Gv  is  incremented  by  1  i.e.  11
b +=  1 #  Gv  is  incremented  by  1  i.e.  21
c +=  1  #  Gv  is  incremented  by  1  i.e.  31
f1() 
a +=  1  #  Gv  is  incremented  by  1  i.e.  12
b +=  1 #  Gv  is  incremented  by  1  i.e.  22
c +=  1 #  Gv  is  incremented  by  1  i.e.  32
f2() 
print('Bye') # Bye



''''
a : 10
b : 20
c : 30
a : 11
b : 40
c : 31
a : 50
b : 22
c : 32
Bye
'''


'''
1) Which   variable  is  accessed  when  LV  and  Gv  got  have  same  name ? --->  LV

2) Which  variable  is  accessed  when  there  is  no  LV  in  the  function ?  ---> GV
'''
