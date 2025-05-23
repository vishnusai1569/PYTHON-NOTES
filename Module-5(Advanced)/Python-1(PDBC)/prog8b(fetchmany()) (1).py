'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
import  mysql . connector as mc
try:
	con  =  mc . connect(database = 'empdb' , user = 'root')
	cur  =  con . cursor()
	cur . execute('select  *  from  emp')
	n  =  int(input('How many rows ?  :  '))
	if n == 0:
		print('Number  of   tuples  :  0')
	else:
		list  =  cur . fetchmany(n)  #  Yields  first  'n'  tuples  of  the  cursor  into  a  list
		print('Emp Number \t Emp Name \t Salary')
		for   tpl   in  list:   #  Iterates  list  i.e. Each  tuple  of  the   list
			print(F'{tpl[0] :4}  \t\t {tpl[1] :10} \t  {tpl[2] : .2f} ')
		print('Number  of   tuples  fetched :  ' , len(list))
	con . close()
	cur . close()
except   mc . errors . InternalError:   # Executed when  all  the  tuples  of  the  cursor  are  not yielded
	pass
except mc . errors . ProgrammingError  as   msg:
	print(msg)
except     mc . errors . InterfaceError:
	print('Pls  start  mysql')