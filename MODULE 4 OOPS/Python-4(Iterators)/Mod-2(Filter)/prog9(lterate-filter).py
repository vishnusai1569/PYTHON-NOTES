# How  to  print  fliter  object  in  different  ways ?
import   time
a = [10 , 15 , 20 , 17 , 18 , 19 , 26]
f = filter(lambda  x  :  x  %  2  ==  0 , a)
print('Iterate  filter  object  with   next   function')
while  True: # How  to iterate  filter  object  with  next()  function
	try:
		print(next(f))   #  10  <next  line>     20  <next  line>  18  <next  line>  26  <next  line>
		time . sleep(1)
	except:
		break
print('Iterate  filter  object  with   for  loop')
for x in filter(lambda  x  :  x  %  2  ==  0 , a) : # How  to iterate  filter  object  with  for  loop
	print(x)   #  10  <next  line>     20  <next  line>  18  <next  line>  26  <next  line>
	time . sleep(1)
print('Unpacking  filter  object :  ' , *filter(lambda  x  :  x  %  2  ==  0 , a)) #  10  <space>     20  <space>  18  <space>  26  <next  line>
print('filter  object  in  the  form  of  list  :  ' , list(filter(lambda  x  :  x  %  2  ==  0 , a)))  #    [10,20,18,26]