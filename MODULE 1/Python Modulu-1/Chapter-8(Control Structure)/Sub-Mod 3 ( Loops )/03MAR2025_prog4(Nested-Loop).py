#  Nested  Loop  demo  program
for  i  in  range(1 , 4):  # i = 3
	for  j  in  range(1 , 5): #  j = 1
			print(i ,  j)  #
	print('Hello')
print('Bye')


'''
1 <space>  1
1 <space>  2
1 <space>  3
1 <space>  4
Hello
2 <space>  1
2 <space>  2
2 <space>  3
2 <space>  4
Hello
3 <space>  1
3 <space>  2
3 <space>  3
3 <space>  4
Hello
Bye
'''

'''
1) What  is  a  nested  loop ?  ---> A  loop  inside  another  loop

2) If  outer  loop  is  executed  'm'  times  and  inner  loop  is  executed  'n'  times,
    How  many  times  are  statements  of  inner  loop  executed  ?  --->  m * n  times
    How  many  times  are  statements  of  outer  loop  executed  ?  --->  m  times
    How  many  times  are  statements  outside  the  loop  executed  ?  --->	Just  Once

3) Which  loop  is  executed  faster ?  ---> Inner  loop
    Which  loop  is  executed  slower ?  ---> Outer  loop

4) Digital  clock
    ----------------
	 for  h  in  range(24):
		 How  many  times  are  statements  executed ?  ---> 24  times
		 for  m  in  range(60):
			 How  many  times  statements  are  executed ?  --->  24 * 60  times
			 for  s  in  range(60):
					How  many  times  statements  are  executed ?  --->  24 * 60 * 60  times

5) Why  is  seconds  inner  most  loop ?  --->  Since  it  is  incremented   for  every  second
 	 Why  is  minutes  outer  loop ?  --->  Since  it  is  incremented  for  every  60  seconds
	 Why  is  hours  outer  most  loop ?  --->  Since  it  is  incremented  for  every  3600  seconds
'''
