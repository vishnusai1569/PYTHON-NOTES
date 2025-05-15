# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:   #  Not  executed becoz  loop  is  broken
	print('else  suite')
#End   of  the  loop
print('Outside  loop')


'''
1
Sec
Hello
2
Sec
Hello
3
Outside  loop
'''
