# Find outputs  (Home  work)
import  time
a = ['Rama Rao' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Manohar' , 'Vamsi']
f = filter(lambda  x  :   len(x) >= 5  , a) #  Creates  an  empty  filter  object
while   True:
	try:
		print(next(f))  #  Rama Rao  <next  line>  Rajesh  <next  line>  Kiran  <next  line>  Manohar  <next  line>  Vamsi <next  line>
		time . sleep(1)
	except:
		break


'''
1) How  to  define  regular  function  instead  of  lambda  function ?  --->  def  f1(x):
																													   return  len(x) >= 5

2) How  to  create  filter  object  with  regular  function  ?  --->  f = filter(f1 , a)
'''