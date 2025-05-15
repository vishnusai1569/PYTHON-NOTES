'''
1) What  is  the  output  when  input  is  (-10 , -20) ?  --->   Quadrant
2) What  is  the  output  when  input  is  (10 , 0) ?  ---> x - axis
3) What  is  the  output  when  input  is  (0 , -20) ?  ---> y - axis
4) What  is  the  output  when  input  is  (0 , 0) ?  ---> Origin
5) What  is  the  output  when  input  is  (10 , 20 , 30) ?  --->  Not  a  point
6) What  is  the  output  when  input  is  [10 , 20]  ?  ---> Quadrant
7) What  is  the  output  when  input  is  [0 , -25]  ?  ---> y-axis
8) What  is  the  output  when  input  is  ()  ?  ---> Not  a  point
9) What  is  the  output  when  input  is  {10 , 20} ?  ---> Not a  point
10) What  is  the  output  when  input  is  (25,) ?  --->  Not a  point
11) What  is  the  output  when  input  is  {10 : 20} ?  --->  Not a  point
'''
tpl = eval(input('Enter  any  point  in  the  form  of  (x , y) :  '))
match  tpl:
	case  (0 , 0):
		print('Origin')
	case   (0 , y):
		print('y - axis')
	case   (x , 0):
		print('x - axis')
	case   (x , y):
		print('Quadrant')
	case  _:
		print('Not  a  point')


'''
1) Why  is  case  _  executed  when  input  is   set  i.e.  {10 , 20} ? --->  Since  set  is  unordered

2) In  other  words,  {x , y}  can  also  be  represented  as  {y , x}
'''
