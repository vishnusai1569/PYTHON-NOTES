'''
Write  a  program to  print  binary  file  in  user  understandable  form

 FILE ---------> object --------> monitor
            load()                 disp()
'''
import  pickle
class   emp:
	def   disp(self):
		print(F'{self . empno:4}  \t  {self . ename:10}  \t  {self . sal:5.2f}')
#End of  the  class
def  display(f):
	while   True:  #   Iteation  4
		try:
			obj = pickle . load(f)
			obj . disp()
		except  EOFError:
			break
#  End  of  the  function
try:
	fname = input('Enter  file  name  :   ') #   abc.txt
	f = open(fname , 'rb')
	display(f)
	f . close()
except  FileNotFoundError:
	print(F'File  {fname}  does  not  exist')


'''
class  Emp:
     def   disp(obj):
	        print(obj . empno , obj . ename , obj . sal , sep = '\t')
Can the  classname  be  Emp ?  --->  No  becoz  file  has  emp  class  objects  and
                                                        hence  Emp  class  objects   can  not  be  read  from  the  file
'''