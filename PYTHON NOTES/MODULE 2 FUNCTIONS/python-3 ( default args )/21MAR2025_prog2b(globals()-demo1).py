# Find  outputs  (Home  work)
def   f1():
	a = 20 #  Lv
	print(a) #   Lv  i.e.  20
	dict = globals()  #  {'a' : 11}
	print(dict['a'])  #   Gv  i.e.  11
	a = 30 # Modifies LV  to  30
	dict['a'] = 40  #  Modifies   Gv  to  40
#  End  of  f1()  function
a = 10 #  Gv
print(a) #  Gv  i.e. 10
a += 1  # Gv  is  incremented  by  1  i.e.  11
f1() 
print(a) #  Gv  i.e. 40


'''
10
20
11
40
'''



'''
1) How  to  distinguish  LV  and  GV  when  they  have  got  same  name ?  --->
												LV  is  accessed  by  LV  name  and  GV  is  accessed  by  globals()['GV  name']

2) globals()['a'] =  40
    What  is  modified ?  --->  GV  'a'

3) In  other  words,  modifying  dictionary  is  as  good  as  modifying  GV  becoz  they  refer  to  same  variable  
'''
