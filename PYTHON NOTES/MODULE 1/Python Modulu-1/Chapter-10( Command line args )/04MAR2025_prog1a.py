# Command  line  arguments  demo  program
from  sys   import   argv
print(argv)   #  ['prog1a.py' , '25' , 'Rama  Rao' , '10000.0' , 'm' , 'True']
print(type(argv)) #    <class  'list'>
for  i  in   range(len(argv)):
	print(F'argv[   {i}   ]  :  {argv[i]} ')
print('argv  list  without  filename  :  ' ,  argv[1:])  #  #  ['25' , 'Rama  Rao' , '10000.0' , 'm' , 'True']
print('Number  of  inputs :  ' ,  len(argv) - 1)



'''
py   prog1a.py   25     'Rama  Rao'   10000.0     m    True
            0           1              2                 3           4       5
'''