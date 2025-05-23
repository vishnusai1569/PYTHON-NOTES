'''
Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->  cur . execute(F'insert  into  emp  values  ({empno} ,  '{ename}' , {sal})')

2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string

3)  What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  inputs  for  empno , ename  and  sal

4) What  action  to  be  made  after  insert ?  --->  Call  commit()  method

5) What  does  commit()  method  do ?  --->  Makes  insertion  becomes  permanent

6) What  happens  when  commit()  is  not  called ?  --->  Insertion  is  only  temporary

7) In  other  words,  insertion  does  not  happen

8) Where  is  commit()  method  defined ?  --->  In  MySqlConnection  class

9) cur . execute(F'insert  into  emp  values (25 , "Rama  Rao" , 10000.0)')
    What  is  the  result  of  cur . rowcount ?  --->  1  becoz  only  one  row  is  inserted  into  emp  table

10) Can  a  tuple  be  inserted  into  cur  object ?  --->  No  becoz  it  is  immutable

11) What  happens  when  we  try  to  insert  duplicate  empno ?  --->  Raises  mc . errors . IntegrityError
'''
import mysql . connector as mc
try:
	con = mc . connect(database = 'empdb' , user = 'root' )
	cur = con . cursor()
	while  True:
		try:
			empno  =  eval(input('Enter  Emp  Number : '))  #  Reads  inputs
			empname  =  input('Enter  Emp  Name : ')
			salary  =  eval(input('Enter  Salary : '))
			cur . execute(F"insert  into  emp  values  ({empno} , '{empname}' , {salary})")  #  Inserts  a  row  into  emp  table
			con . commit() # Insertion  becomes  permanent
			print(cur . rowcount , 'row  is  inserted')   #  1  row  is  inserted
		except  mc . errors . IntegrityError as msg:   #   Executed  when duplicate  empno  is  inserted
			print('Row  can  not  be  inserted  as   empno  is  duplicate  :  ' , msg)
		ch = input('Do  you  wish  to  insert  another  row ? (Y / N) : ')
		if  ch  == 'n'   or   ch  == 'N':
				break
	# End  of  the  loop
	cur . close()
	con . close()
except   mc . errors . ProgrammingError as  msg:
        print(msg)
except     mc . errors . InterfaceError:
        print('Pls  start  mysql')