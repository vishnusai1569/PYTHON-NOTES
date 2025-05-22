# Write  a  program  to  create  a   csv   file
import   csv
def   create(f):
	w = csv . writer(f)  #   Returns  writer  object
	w . writerow(['EMP NO' , 'EMP NAME' , 'SALARY'])  # Writes  column  headings  to  the  file
	n = eval(input('How Many Employees ? :   '))  #
	for  i  in  range(n):
		empno = eval(input('Enter Employee No : '))
		ename = input('Enter Employee Name : ')
		sal = eval(input('Enter Employee Salary : '))
		w . writerow([empno , ename, sal])  #  Writes  a  row  of  3  values  to  the   file
	# End  of  for  loop
	print(F'File  {f . name}  is  created')
# End  of  the  function
fname = input('Enter   filename  :   ')  #  Reads  filename
f = open(fname , 'w' , newline = '')  #  Opens  file  in  write  mode  and  newline  is  modified  to  ''
create(f)
f . close()  #  Closes  the  file


'''
1) Where  is  csv  file  usually  opened ?  --->   In  microsoft-excel

2) Can  csv  file   be  opened  in  editor  like  notepad  ?  --->
																	Yes  but  commas  are  automatically  inserted  between  the  values
'''