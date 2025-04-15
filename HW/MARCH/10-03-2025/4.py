'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a.rfind('city')
while  index != -1:
	print(index)
	index = a.rfind('city',0,index)
print('End')