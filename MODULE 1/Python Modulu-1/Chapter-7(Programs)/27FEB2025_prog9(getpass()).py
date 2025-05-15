#  getpass()  function  demo  program
import  getpass
usr = input('User  Name  :  ')  #Scott
pwd =  getpass . getpass('Password  :  ') #   Tiger
print('Logging  in   ... ')
print('User  name  :  ' , usr)
print('Password  :  ' , pwd)


'''
getpass()  function
----------------------
1) What  does  getpass()  function  do  ?  --->  Reads  a  string  without  echo

2) In  other  words,  user  input  is  not  visible  on  the  screen

3) How  is  getpass()  function  different  from  input()  function  ?  --->  input()  function  reads  a  string  with  echo  but
																												   getpass()  function  reads  a  string  without  echo

4) When  is  getpass()  function  recommended ?  --->  To  read  sensitive  data  such  as  password

5) In  other  words,  user  name  can  be  echoed  but  not  password

6) Where  is  getpass()  function  defined ?  --->  In  getpass  module
'''
