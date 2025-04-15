''' (Home  work)
Write  a  program  to  convert  a  string  to  dictionary

Let  input  be   "Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m"

What  is  the  output ?  --->  {Emp no : 25 , Emp name  :  Rama Rao , sal : 10000.0 , gender : m}

Hint :  Use  split()  method  twice
'''
a = input('Enter  string  with  arg1 = value1 , arg2 = value2 , arg3 = value3 , ....  :  ')  #   Emp no = 25 , Emp name = Rama  Rao , sal = 10000.0 , gender = m
b = a . split(',')  #  ['Emp no = 25' , 'Emp name = Rama  Rao' , 'sal = 10000.0' , 'gender = m']
c = {}
for  x  in  b:  #   x is  'Emp  name = Rama  Rao'
	y = x . split('=')  #  ['Emp  name' , 'Rama  Rao']
	c[y[0]] = y[1]  #  c['Emp  name'] = 'Rama  Rao'  --->  {'Emp  no' : '25' , 'Emp name' , 'Rama  Rao'}
	print(c)
# End  of  for  loop
print(c)



'''
1) What  is  object  'b' ? --->  ['EmpNo=25' , 'EmpName=Rama Rao' ,  'Sal=10000.0' ,  'Gender=M']

2)   x                                             y                                        y[0]                  y[1]                   dictionary  c
--------------------------------------------------------------------------------------------------------------------------------
      'EmpNo=25'                    ['EmpNo' , '25']                     'EmpNo'           '25'                  {'EmpNo' : '25'}
      'EmpName=Rama Rao'     ['EmpName' , 'Rama Rao']     'EmpName'       'Rama  Rao'     {'EmpNo' : '25' , 'EmpName' : 'Rama Rao'}
      'Sal=10000.0'                  ['Sal' , '10000.0']                  'Sal'                  '10000.0'        {'EmpNo' : '25' , 'EmpName' : 'Rama Rao' , 'Sal' : '10000.0'}
      'Gender=M'                     ['Gender' , 'M']                      'Gender'           'M'                   {'EmpNo' : '25' , 'EmpName' : 'Rama Rao' , 'Sal' : '10000.0' , 'Gender' : 'M'}
'''
