# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)#<class 'tuple'> (25, 10.8, 'Hyd', True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)#<class 'dict'> {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

