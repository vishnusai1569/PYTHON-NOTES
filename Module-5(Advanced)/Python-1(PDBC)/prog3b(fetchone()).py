'''
Write  a  program  to  print  emp  table  of  the  database  with  fetchone()   method

emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                     execute()                                 fetchone()             print()
'''
import   mysql . connector   as   mc  #  Package alias
try:
	con = mc . connect(database = 'empdb' , user = 'root')  #  Connects  to  database  and   returns  MySqlConnection  object
	cur = con . cursor()  #  Returns  MySqlCursor  obect
	cur . execute('select * from emp') #  Executes  sql  command  and  stores  results  in  object cur  on  demand
	print('Emp Number \t Emp Name \t\t Salary')
	while  tpl  :=  cur . fetchone():  #  Yields each  tuple  of  the  cursor  until  there  are no  more  tuples
		print(F'{tpl[0]}  \t\t  {tpl[1]} \t\t {tpl[2]}')  #  Prints  elements  of  tuple
	if   cur . rowcount == -1:  #  Table  is  empty
		print('Number  of  tuples :  0')
	else:
		print('Number  of  tuples :  ' , cur . rowcount)  #  Number  of   tuples  yielded  from  the cursor
	cur . close()  # Optional
	con . close() #  Optional
except   mc.errors.InterfaceError:
	print('Pls  start  mysql')
except  mc.errors.ProgrammingError  as  msg:
	print(msg)


'''
1) What  is  the  result  of  tpl :=  cur . fetchone()  ?  --->  That  tuple  yielded  from  the  cursor

2) while  tpl = cur . fetchone():
	What  is  the  issue  with  the  above  while  loop ? --->
														while  throws  error  as  the  result  of  condition  is  neither  True  nor  False
'''