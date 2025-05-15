#  Is  input(no-args)  valid ?  --->  Valid  but  not  recommended
x = input() #  Reads  string  input
print(type(x))#  <class  'str'>
print(x) #  User  input



'''
1) What  is  the  advantage  of  input('prompt  message')  ? --->  Message  is  prompted  before  user  types  input

2) What  is  the  issue  with  input(No  args) ? --->  User  does  not  know  what  input  to  enter  becoz  message  is  not  prompted

3) Hence  avoid  input(No  args)
'''
