'''
Write  a  program  to  print  emp  table  of  database  with  for  loop

emp  table -------------> cursor  object  -----------> monitor
                    execute()                              for  loop
'''
import   mysql . connector #  Automatically  executes  __init__  module  of  connector
try:
	con = mysql . connector . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')  #  Connects  to  database
	cur =  con . cursor()  #  Creates  MySqlCursor  object
	cur . execute('select  *  from  emp') #   Executes  sql  command  and  stores   results  in  cur  object  on  demand
	print(cur . rowcount) #   -1  :  object cur  is  empty
	for  x  in   cur:#   'x'  is  each  tuple  of  object  cur
		print(x)  #  Each  tuple
		print(cur . rowcount)  #   Number  of   tuples  fetched
	cur . close()  #  Optional
	con . close() #  Optional
except   mysql.connector.errors.InterfaceError:
	print('Pls  start  mysql')
except   mysql.connector.errors.ProgrammingError  as  msg:
	print(msg)



'''
Steps:
1) Connect  to  database  with  connect()  function

2) Create  MySqlCursor  object  using   MySqlConnection  object

3) Copy  contents  of  emp  table  to  cursor  object  with  execute()  method

4) Print  cursor object  with  for  loop
'''