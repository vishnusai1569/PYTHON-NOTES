

'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   student:
	def   get(self):
		self . rno = eval(input('Enter  roll  number : '))
		self . sname = input('Enter  student  name :  ')
		self . gender = input(('Enter  gender (m/f) : '))
		self . m = []
		for  i  in  range(3):
			marks = int(input(F'Enter  marks  of  subject  {i + 1}  :  '))
			self . m . append(marks)
	def   compute(self):
		self . tot = sum(self . m)
		self . avg = self . tot / 3
		if  min(self . m) < 40:
				self . grade = 'Fail'
		elif  self . avg >= 70:
				self . grade = 'Distinction'
		elif  self . avg >= 60:
				self . grade = 'First  class'
		elif  self . avg  >= 50:
				self . grade = 'Second  class'
		else:
				self . grade = 'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,  self . rno)
		print('Student  Name  :  ' , self . sname)
		print('Gender  :  ' ,  self . gender)
		print('Total  Marks  :  ' , self . tot)
		print(F'Average  :  {self . avg:.2f}')
		print('Grade  :  ' , self . grade)
	def   __str__(self):
		return f'{self . rno}  \t {self . sname}  \t  {self . gender}  \t  {self . tot}  \t  {self . avg:.2f}  \t  {self . grade}"
#End  of  the  class
s = student()
s . get()
s . compute()
s . disp()
print(s)




#  Object  's'  --->  rno = 25 , sname = 'Rama Rao' , gender = 'm' , m = [52,48,55] , total = 155 , average = 51.66 , grade = '2nd  class'


'''
Can  Fail  be  handled  at  the  end ?  --->  No  and  it  should  be  handled  only  at  the  begining
'''