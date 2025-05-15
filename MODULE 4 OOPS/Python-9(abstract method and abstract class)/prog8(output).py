# Find outputs
from  abc  import *
class   database(ABC):
	@abstractmethod
	def  connect(self):
		pass
	@abstractmethod
	def  disconnect(self):
		pass
'''
Who  should  implement  connect()  and  disconnect()  methods ?  ---> Every  child  class  of  database
'''
class   oracle(database):
	def  connect(self):
		print('Connecting  to  oracle  database')
	def disconnect(self):
		print('Disconnecting  from  oracle  database')
class  mysql(database):
	def  connect(self):
		print('Connecting to mysql database')
	def  disconnect(self):
		print('Disconnecting from mysql database')
#end of the class
try:
	s = input('Enter class name (oracle , mysql  or  database) : ')
	classname = eval(s)
	a = classname()
	a . connect()
	a . disconnect()
except:
	print('Invalid  classname')


'''
1) What  does  eval('oracle')  do ?  --->  Converts  string  'oracle'  to  class  name  oracle
    What  does  eval('mysql')  do ?  --->  Converts  string  'mysql'  to  class  name  mysql
    What  does  eval('database')  do ?  ---> Converts  string   'database'  to  class  name  database
    What  does  eval('sybase')  do ? ---> Throws  error  becoz  there  is  no  sybase  class

2) What  does  oracle()  do ?  ---> Creates  oracle  class  object
     What  does  mysql()  do ?  --->  Creates  mysql  class  object
     What  does  database()  do ?  ---> Throws  error  becoz  database  is  an  abstract  class  with  abstract  methods
'''