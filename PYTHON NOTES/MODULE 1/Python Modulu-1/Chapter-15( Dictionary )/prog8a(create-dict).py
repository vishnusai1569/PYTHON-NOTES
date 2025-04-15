'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
n = int(input("How many Employees ? : "))
a = { }
for  i  in  range(n):
	ename = input('Enter Emp Name : ')
	sal = float(input('Enter Salary : '))
	a[ename] = sal
# End  of  for  loop
print(a)
