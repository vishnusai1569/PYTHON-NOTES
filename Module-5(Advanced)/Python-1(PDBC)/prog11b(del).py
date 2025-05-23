'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
'''
import  mysql . connector as mc
try:
	con  =  mc . connect(database = 'empdb' , user = 'root')
	cur  =  con . cursor()
	cond = input('Enter condition: ')
	cur . execute(F'delete from emp where {cond}')  #  Deletes  all  the  rows  of  emp  table  which  satisfy  the  condition
	con . commit()  #  Deletion  becomes  permanent
	print(F'{cur . rowcount}  rows Deleted')  #  Number  of   rows   deleted
	con . close()
	cur . close()
except mc . errors . ProgrammingError  as   msg:
	print(msg)
except     mc . errors . InterfaceError:
	print('Pls  start  mysql')