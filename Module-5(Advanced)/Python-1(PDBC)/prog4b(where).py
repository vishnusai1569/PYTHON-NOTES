'''
Write  a  program  to  print  emp  table  based  on  user  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  condition  from  the  user

3) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                         execute()                                 fetchone()              print()

'''
import   mysql . connector   as   mc  #  package  alias
try:
	con = mc . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')  #  Conects  to  database  and  returns  MySqlConnection  object
	cur =  con . cursor()  #  Returns  MySqlCursor  object
	cond = input('Enter  any  condition : ')  # Reads  the  condition
	cur . execute(F'select * from emp where {cond}')  #    # Executes  sql  command  and  results  are  stored  in  object  on  demand
	print('Emp Number \t Emp Name \t\t Salary')
	while tpl := cur . fetchone():  # Yields  each  tuple  of  the  cursor   until  there  are  no  more  tuples
		print(F'{tpl[0]:4} \t\t {tpl[1]:20} \t {tpl[2]}')   #  Prints  each  element  of  the  tuple
	if   cur . rowcount  ==  -1:  # Table  is  empty
		print('Number   of  tuples  : 0')
	else:
		print('Number  of  tuples  : ' , cur . rowcount)  #  Number  of  tuples  yielded
	cur . close()  #  Optional
	con . close()  # Optional
except  mc . errors . ProgrammingError as  msg:
	print(msg)
except  mc . errors . InterfaceError:
	print('Pls  start  mysql')