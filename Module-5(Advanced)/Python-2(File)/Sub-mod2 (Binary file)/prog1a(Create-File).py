'''
Write  a  program  to  create  a  binary  file  with  employee  objects

keyboard  ------->  object   ---------> File
                   get()                   dump()
'''
import  pickle
class  emp:
	def  get(self):
		self . empno = eval(input('Enter Emp no  : '))
		self . ename = input('Enter Emp name : ')
		self . sal = eval(input('Enter Salary : '))
#end of the class
def   create(f):
	e = emp()  #   Empty  object
	while  True:
		e . get()  #   Reads  emp  data  into  object  'e'
		pickle . dump(e , f)  #  Writes  object  'e'  to  the  file  in  encrypted  form
		ch = input('Do  you  wish  to  enter  another  record (y / n) ? :   ')
		if  ch == 'n'  or  ch == 'N':
			break
	# End  of  while  loop
	print(F'File  {f . name}  is  created')
# End  of  the  function
fname = input('Enter  file  name :  ')  #  Reads  filename
f = open(fname , 'wb')  #  Opens  the  file
create(f)
f . close()   # Closes  the file


'''
Open  the  file  and  observe  that  file  is  encrypted
'''