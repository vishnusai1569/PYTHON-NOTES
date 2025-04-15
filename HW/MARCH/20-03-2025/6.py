#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a  :  10  	  b  :  (20, 30, 40)  	  c  :  50
f1(60 , 70 , c = 80)#a  :  60  	  b  :  (70,)  	  c  :  80
f1(90 , c = 100)#a  :  90  	  b  :  ()  	  c  :  100
#f1(a = 1 , 2 , c = 3)#pak follows kwa
#f1(1 , 2 , 3)#error 1 value is missing
