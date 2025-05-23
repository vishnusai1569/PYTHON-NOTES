'''
Write  a  program  to  print  user  input  table  with  next()  function

1) How  to  call  execute()  method ?  --->  cur . execute(F'select  *  from  {table}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the   table  name

3) What  does  next(cur)  do ?  --->  Yields  the  next  tuple  of  cursor  object

4) What  does   next()  function  do  when  end  of   the  cursor  is  reached ?  --->  Throws StopIteration  error

5) emp  table ----------------> cursor  object -----------------> tpl ---------> monitor
                          execute()                                   next()                  print()
'''
import   mysql . connector   as   mc
try:
	con = mc . connect(database = 'empdb' , user = 'root')
	cur = con . cursor()
	table_name = input('Enter   table  name :  ')
	cur . execute(F'select  *  from  {table_name}')
	print('Emp  Number \t Emp  Name \t Salary')
	while  True:
		try:
			tpl = next(cur)  #  Yields  next  tuple  of  the  cursor
			print(F'{tpl[0]:4} \t\t {tpl[1]:10} \t {tpl[2]:.2f}')
		except  StopIteration:  #  Executed when  there  are  no  more  tuples
			break
	#  End  of  while  loop
	if   cur . rowcount == -1:
		print('Number  of  tuples :  0')
	else:
		print('Number  of  tuples :  ' , cur . rowcount)
	cur . close()
	con . close()
except   mc . errors . ProgrammingError  as  msg:
	print(msg)
except    mc . errors . InterfaceError:
	print('Pls  start  mysql')


'''
What  is  the  alternative  to  next(cur)  ?  --->  cur . __next__()
'''