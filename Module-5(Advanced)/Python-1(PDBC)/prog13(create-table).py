'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->
								cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->
																			Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
import   mysql . connector
try:
	con = mysql . connector . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')
	cur =  con . cursor()
	table = input('Enter name of the table: ')
	sql = f'create  table  {table}(rollno  int  primary  key , sname  char(20) ,  marks  float)'
	cur . execute(sql)  #   Creates  a  table
	print(table , 'table  created')
	cur . close()
	con . close()
except  mysql.connector.errors.InterfaceError:
	print('Pls  start  mysql')
except  mysql.connector.errors.ProgrammingError  as   msg:  #   Executed  when  table  already  exists
	sql = f'drop  table  {table}'
	cur . execute(sql)   #  Deletes  table
	print(table,'table  is  deleted')
	sql=f'create  table  {table}(rollno  int  primary  key , sname  char(20) ,  marks  float)'
	cur . execute(sql) #  Creates  a  table  with  same  name
	print(table,'table created')



'''
1) When  is  commit()  mandatory ? --->   For  DML  commands  (Data  manipulation  language)

2) What  are  the  three  DML  commands ?  --->  insert , delete  and  update

3) When  is  commit()  not  required ?  --->  For  DDL  commands  (Data  definition  language)  and  select  command

4) What  are  DDL  commands ?  ---> Create  table , drop  table , alter  table  and  so  on
'''