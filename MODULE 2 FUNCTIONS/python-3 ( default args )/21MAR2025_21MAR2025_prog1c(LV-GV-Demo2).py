# Find  outputs (Home  work)
def   f1():
	a = 20  # Lv
	print(a)  # Lv  i.e.  20
	a += 1 #  Lv is  incremented  by   i.e.  21
#End  of  the  function
a = 10 #  Gv
print(a) #  Gv  i.e. 10
a += 1  # Gv  is  incremented   by  1  i.e.  11
f1()
print(a) #  Gv  i.e.  11


''''
10
20
11
'''

'''
1) Can  a  function  access  LV  of  a  different  function ?  --->  No  becoz  it  is  not  visible

2) Can  statements  outside  the  function  access  LV  of  a  function ?  --->  No  becoz  it  is  not  visible

3) In  other  words,  statements  outside  the  function  can  access  only  GV
'''
