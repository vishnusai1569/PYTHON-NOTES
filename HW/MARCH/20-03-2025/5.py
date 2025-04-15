#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a  :  (10, 20, 30)   	   b  :  40
f1(50 , b = 60)#a  :  (50,)   	   b  :  60
f1(b = 70)#a  :  ()   	   b  :  70
#f1(b = 10 , a = (20 , 30 , 40))#error
#f1(b = 10 , (20 , 30 , 40))#error
#f1()##missing keyword arg

#f1(10 , 20 , 30 ,(10 , 20 , 30))#error
#f1(10 , 20 , 30 ,40)#error b is missing
#f1(25)#b is missing
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a  :  (10, 20, 30)   	   b  :  (10, 20, 30)

