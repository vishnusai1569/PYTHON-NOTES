'''
Write  a  program  to  print  cursor  with  fetchall()  method

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                       execute()                               fetchall()                    for  loop                print()
'''
import    mysql . connector  as  mc
try:
	con  =  mc . connect(database = 'empdb' , user = 'root')
	cur = con . cursor()
	cur . execute('select * from emp')
	list = cur . fetchall()  #  Yields  all  the  tuple  of  cursor  cursor  into  a  list
	print('Emp Number \t Emp Name \t Salary')
	for   tpl   in   list:  #  Iterates  list  i.e.  each  tuple  of  the  list
		print(F'{tpl[0] :4}  \t\t {tpl[1] :10} \t  {tpl[2]: .2f} ')
	print('Number  of  tuples  : ' , len(list))
	cur . close()
	con . close()
except mc . errors . ProgrammingError  as   msg:
	print(msg)
except     mc . errors . InterfaceError:
	print('Pls  start  mysql')