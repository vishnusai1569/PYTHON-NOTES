#  Variable  number  of  arguments  demo  program
def   f1(*t):  #  't'  is  tuple  due  to   *
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of   4  args  is  passed  to  the  function
f1()   #  Empty  tuple  is  passed  to  the  function
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})  #  Tuple  of 3  args  is  passed  to  the  function
f1('Hyd')  #  Tuple  of   single  arg  is  passed  to  the  function
tpl = (100 , 200 , 150)
f1(tpl)  #  Nested  tuple   is  passed  to  the  function
#f1(t = (10 , 20 , 30))  #  Error  due  to  ka



'''
(10,20,15,18)
<class  'tuple'>
4

()
<class  'tuple'>
0

([10 , 20] , (30 , 40 , 50) , {80 , 60 , 90 , 70})
<class  'tuple'>
3

('Hyd',)
<class  'tuple'>
1

((100 , 200 , 300),)
<class  'tuple'>
1
'''
