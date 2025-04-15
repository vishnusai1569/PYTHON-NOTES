# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()
print(b)#dict_values(['Hyd', 'Sec', 'Cyb', 'Pune'])
print(type(b))
for  x   in   b:
	print(x)

"""
Hyd
Sec
Cyb
Pune
"""