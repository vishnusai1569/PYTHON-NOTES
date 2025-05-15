#  extend()  method  demo  program
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . extend(b)  # Appends  elements  of  list 'b'  to  list  'a'
print(a) #   [10,20,30,40,50,60,70]
print(len(a)) #  7
a . extend('Hyd')   # Appends  characters  of  'Hyd' to  list  'a'
print(a) #   [10,20,30,40,50,60,70,'H','y','d']
print(len(a)) #  10
#a . extend(25)  #  Error  becoz  25  is  not  a  sequence



'''
extend()  method
---------------------
1) What  does  extend(sequence)  do ?  --->  Appends  elements  of  sequence  to  the  list  but  not  the  sequence

2) Is  extend(non-sequence)  valid ? ---> No  becoz  argument  should  be  sequence  only
'''
