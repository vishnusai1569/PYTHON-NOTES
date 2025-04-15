for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

'''
1
sec
hello
2
sec
hello
3
4
sec
hello
5
sec
hello
6
7
sec
hello
outside loop
'''