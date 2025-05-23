'''
Repeat  prog8b(fetchmany)  but  validate  input
i.e. Print  a  msg  when  input > number  of  tuples

Hint:  Use  fetchmany()  method
'''
import  mysql . connector as mc
try:
	con  =  mc . connect(database = 'empdb' , user = 'root')
	cur  =  con . cursor()
	cur . execute('select * from emp')
	n  =  int(input("How many rows ? : "))  #   3
	list  =  cur . fetchmany(n)
	if  n < 1  or  n > cur . rowcount:
		print('Invalid input')
	else:
		print('Emp Number \t Emp Name \t Salary')
		for   tpl   in  list:
			print(F'{tpl[0] :4}  \t\t {tpl[1] :10} \t  {tpl[2] : .2f} ')
		print('Number  of   tuples  :  ' , len(list))
	con . close()
	cur . close()
except   mc . errors . InternalError:
	pass
except mc . errors . ProgrammingError  as   msg:
	print(msg)
except     mc . errors . InterfaceError:
	print('mysql is not running in the background')