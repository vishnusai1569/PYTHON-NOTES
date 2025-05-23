'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->   cur . execute(F'update  emp  set  {cname}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->Read  cname  and  cond
'''
import  mysql . connector as mc
try:
	con  =  mc . connect(database = 'empdb' , user = 'root')
	cur  =  con . cursor()
	cond = input('Enter condition: ')
	cname = input('Enter column name = value: ')
	cur . execute(F'update emp set {cname} where {cond}')  #  Modifies  rows  of  emp  table   based  on  user  inputs
	con . commit()  #  Updation  becomes  permanent
	print(F'{cur . rowcount}  rows Updated')  #  Number  of  rows  updated
	con . close()
	cur . close()
except mc . errors . ProgrammingError  as   msg:
	print(msg)
except     mc . errors . InterfaceError:
	print('Pls  start  mysql')