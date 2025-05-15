# Can  dictionary  be  enumerated ?   (Home  work)
import   time
def  disp(e):
	while  True:
		try:
			print(next(e))
			time . sleep(1)
		except:
			break
	print()
a = {'Empno'  :  25 , 'Emp Name'  :  'Rama Rao' , 'Sal' : 10000.0}
b = enumerate(a . keys()) # Keys  are  enumerated
disp(b)   #  (0,'Empno' )  <next  line>  (1,'Emp Name')  <next  line>  (2, 'Sal')  <next  line>
c = enumerate(a . values())   #  Values  are  enumerated
disp(c) # (0, 25)  <next  line>  (1,'Rama Rao')  <next  line>  (2, 10000.0)  <next  line>
d = enumerate(a . items())   #  tuples  are  enumerated
disp(d)  #   (0, ('Empno', 25))  <next  line> (1, ('Emp Name', 'Rama Rao'))  <next  line>  (2, ('Sal', 10000.0))  <next  line>
f = enumerate(a , start = 5) # Keys  are  enumerated
disp(f)  #  (0,'Empno' )  <next  line>  (1,'Emp Name')  <next  line>  (2, 'Sal')  <next  line>


'''
1) Can  dictionary  be  enumerated  ?  --->  Yes  even  though  it  is  not  indexed

2) How  is  dictionary enumerated  when  dictionary  is  not  indexed ?  --->
																							They  are  enumerated  indexes  but  not  dict  indexes

3) Is  next(dictionary)  valid ?  ---> No  becoz  next()  function  demands  an  iterator  but  dictionary  is  not  an  iterator
'''