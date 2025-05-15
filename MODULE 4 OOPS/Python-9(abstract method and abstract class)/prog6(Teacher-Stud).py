#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from  abc  import  *
class  person(ABC):
	def   get(self):
		self . number = int(input('Enter  number  :  '))   # How  to   read  number
		self . name = input('Enter  name :  ')  #  How  to   read  name
		self . age = int(input('Enter  age :  ')) #  How  to   read   age
		self . gender = input('Enter  gender :  ')   # How  to   read   gender
	def   disp(self):
		print(self . number , self . name , self . age , self . gender , sep = '\t' , end = '\t')  #  How  to  print  number , name , age , gender  in  same  line  separated  by  tab
	@abstractmethod
	def   compute(self):
                pass
'''
1) Why  is  compute()  an  abstract  method ?  --->  No  idea  what  to  calculate

2) What  is  the  advantage  of  writing  ABC ?  --->  Every  child  class  should  implement  compute()  method

3) What  happens  if  at  least  one  child  class  does  not  implement  compute()  method  ?  --->
																										That  child  class  object  can  not  be  created
'''
class  student(person):
	def  get(self):
		super() . get()  #  How  to  read   number , name , age , gender
		self . m = []
		for  i  in  range(3):  #  How  to  read  marks  of  3  subjects  into  list
				marks = int(input(F'Enter  marks  for  subject  {i + 1}  :  '))
				self . m . append(marks)
	def  compute(self):
		self . tot = sum(self . m)  #  How  to  calculate  total  marks
		self . avg = self . tot / 3  #  How  to  calculate  average  marks
	def  disp(self):
		super() . disp()  #  How  to  print  number , name , age , gender
		print(self . tot , self . avg , sep = '\t')  #  How  to  print  total  and  average  in  same  line separated  by  tab
class  teacher(person):
	def   get(self):
		super() . get()  #  How  to  read  number , name , age  and  gender
		self . sub = input('Enter  subject :  ')   # How  to  read   subject
		self . sal = float(input('Enter  salary  :  '))  #  How  to  read   salary
	def   compute(self):
		da = 0.50 * self . sal #   50%  of  salary
		hra = 0.20 * self . sal  #   20%  of  salary
		self . gp =  self . sal + da + hra  #  How  to  calculate  grosspay  and  store  the  result  in  object (grosspay  is  sal + da + hra)
		pf = min(0.08 * self . gp , 400)  #  8%  of  grosspay  but  a  max  of  400
		if  self . gp < 10000:
				tax = 0.10 * self . gp  #  10%  of  grosspay  if  grosspay is  < 10000  and  15%  otherwise
		else:
				tax = 0.10 * 10000 + 0.15 * (self . gp - 10000)
		self . np =  self . gp - pf - tax   #  How  to  calculate  netpay  and  store  the  result  in  object  (netpay  is  grosspay - pf - tax)
	'''
	What  are  da , hra , pf  and  tax ?  --->  Local  variables of  compute()  method
	'''
	def   disp(self):
		super() . disp() # How  to  print  number , name , age , gender
		print(self.sub , self.sal , self.gp , self.np , sep = '\t') # How  to  print  subject , salary , grosspay , netpay  in  same  line   separated  by  tab
# End  of  class
def  menu():
	print('1. Teacher')
	print('2. Student')
	print('3. Exit')
# End  of  the  function
a = []
i = 0
menu()
ch = eval(input('Enter choice : '))  #  2
while  ch < 3:  #  Repeat  until  input  is  3
	if   ch == 1:
		a . append(teacher())  #  How  to  append  teacher  object  to  list  'a'
	else:
		a . append(student())  #  How  to  append  student  object  to  list  'a'
	a[i] . get()  #  How  to  read  inputs  into  object
	a[i] . compute()   # How  to  store   results  in  object
	i += 1   #  How  to  move  to  next  index  --->  4
	menu()
	ch = eval(input('Enter choice : '))  #  3
#end of loop
print('Teachers')
#How  to  print  all  teacher  objects
for   x  in  a:  # 'x' is  each  object  of  list   'a'
	if  isinstance(x , teacher):
		x . disp()
print()
print('Students')
#How  to  print  all  student  objects
for   x  in  a:  # 'x' is  each  object  of  list   'a'
	if  isinstance(x , student):
		x . disp()
print('Good  Bye')