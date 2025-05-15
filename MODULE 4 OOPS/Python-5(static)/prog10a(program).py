'''
Write  a  program  to  print  only  static  variables  but  not  environment  variables  of   classname . __dict__

Hint:  Use  startswith()  and  endswith()  methods
'''
class  c1:
	x = 1
	y = 2
	z = 3
#  End  of  the  class
a = {}
b = c1 . __dict__
for  key  in   b:
	if  not  key . startswith('__')  and  not  key . endswith('__'):
		a[key] = b[key]
print('static  variables  of  class  c1 :  '  ,  a)