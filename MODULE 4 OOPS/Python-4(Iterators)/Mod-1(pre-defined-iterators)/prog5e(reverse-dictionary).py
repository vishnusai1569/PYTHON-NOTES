'''
Gift
Write  a  program  to  reverse  a  dictionary ?

Let  input  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}
What  is  the  output  ?  --->  {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}

Hint:  Use  reversed  iterator
'''
a = eval(input("Enter a dictionary :  "))
print('Reverse  dictionary  :  ' ,  dict(reversed(a . items())))



'''
Let  'a'  be  {'Empno' : 25 , 'Emp Name' : 'Rama  Rao' , 'Sal' : 10000.0}

1) What  does  a . items()  return ?  --->  dict_items([('Empno' , 25) , ('Emp Name' , 'Rama Rao') , ('Sal' , 10000.0)])

2) What  happens  when  dict_items  object  is  reversed ?  --->  ('Sal' , 10000.0)  ('Emp  Name' , 'Rama  Rao')   ('Empno' , 25)

3) What  does  dict(b)  return ?  --->   {'Sal' : 10000.0 , 'Emp  Name' :  Rama  Rao' , 'Empno' : 25}
'''