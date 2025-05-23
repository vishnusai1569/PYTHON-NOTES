'''
Write  a  program  to  print  emp  table  in  sorted  order

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  emp  order  by  {colname}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  colname

3) emp  table ----------------> cursor  object ----------------> tpl ---------> monitor
                          execute()                                  fetchone()             print()
'''
import   mysql . connector  as  mc  #  package  alias
try:
	con = mc  . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')  #  cursor()   method  can  not  be  called  without  having  MySqlConnection  object
	cur =  con . cursor()  #   execute()  method  can  not  be  called  without  having  MySqlCursor  object
	colname = input('Enter column name: ') #  Reads  colname
	cur . execute(F'select * from emp order by {colname}') #  Executes  sql  command  and  stores  results  in  cur  object  on  demand
	print('Emp Number \t Emp Name \t\t Salary')
	while tpl := cur . fetchone():  # Yields  each  tuple  from  the  cursor  until  fetchone()  method  returns  None
		print(F'{tpl[0]:4} \t\t {tpl[1]:20} \t {tpl[2]}') #  All  the  elements  of  tuple
	if   cur . rowcount  ==  -1:  #  Table  is  empty
		print('Num  of rows : 0')
	else:
		print('Num  of rows : ' , cur . rowcount)  #  Number  of  tuples  yielded  from  the  cursor
	cur . close()  #  Optional
	con . close()   #  Optional
except mc . errors . ProgrammingError  as   msg:
        print(msg)
except     mc . errors . InterfaceError:
        print('Pls   strat  mysql')


'''
1) What  does  table  contain  (unsorted  data / sorted  data)  ?  --->  Unsorted  data

2) What  is  yielded  from  the  cursor ?  --->  Sorted  data  due  to  order  by  clause
'''