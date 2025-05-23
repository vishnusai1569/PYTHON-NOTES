'''
Write  a  program  to  insert  multiple  rows  into  emp  table

1) How  to  insert  multiple  rows  into  the  table ?  --->  With  executemany()  method

2) Where  is  executemany()  method  defined ?  --->  In  MySqlCursor  class

3) cur . executemany('insert   into  emp  values (%s,%s,%s)' ,  list)
    What  does  the  method  do ?  ---> Inserts  all  the  tuples  present  in  the  list  into  emp  table

4) What  does  first  %s  represent ?  --->  First  element  of  each  tuple  in  the  list
    What  does  2nd  %s  represent ?  --->  2nd  element  of  each  tuple  in  the  list
    What  does  3rd  %s  represent ?  --->  3rd  element  of  each  tuple  in  the  list

5) How  many  rows  are  inserted  if  there  are  four  tuples  in  the  list  ?  --->  4  rows
    What  is  the  result  of  cur . rowcount ? --->  4

6) What  are  the  two  arguments  of  executemany()  method  ?  --->
																			sql  command   and   list  of  tuples  where  each  tuple  is  a  row
'''
import   mysql . connector
try:
	con = mysql . connector . connect(host = 'localhost' , database = 'empdb' , user = 'root' , password = '')
	cur =  con . cursor()
	n = int(input('How  many  rows  would  you  like  to  insert : '))
	list=[]  #  Empty  list
	for  i  in  range(n): #  Executes  loop  'n'  times
			print(f'Employee  {i + 1}')
			empno = int(input('Enter  employee  number : '))  #  Reads  inputs
			ename = input('Enter  employee  name : ')
			sal = float(input('Enter  salary : '))
			list . append((empno , ename , sal))  #   Appends  tuple  to  the  list
	cur . executemany('insert   into  emp  values (%s,%s,%s)' ,  list)  #  Inserts  list of  tuples into  emp  table
	con . commit() #  Insertion  becomes  permanent
	print(cur . rowcount , 'rows  are  inserted')  #  Number  of  rows  inserted
except  mysql.connector.errors.InterfaceError:
	print('Pls  start  mysql')
except  mysql.connector.errors.ProgrammingError  as   msg:
	print(msg)
except mysql.connector.errors.IntegrityError as msg:  #  Executed  when  duplicate  empno  is  inserted
	print(msg)



'''
1) What  does  execute()  method  do  ?  --->  Inserts  a  single  row  into  the  table

2) What  does  executemany()  method  do ? --->  Inserts  multiple  rows  into  the  table
'''