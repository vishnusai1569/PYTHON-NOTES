'''
Write  a  program  to  determine  bill  amount  and  input  is  units

Units                                                      Cost
------------------------------------------------------------
First  100  units(0 - 99)					Rs. 3.00 / unit

Next  100  units(100 - 199)				Rs. 3.50 / unit

Next  200  units(200 - 399)				Rs. 4.00 / unit

Next  300  units(400 - 699)				Rs. 4.50 / unit

Above  700  units(>= 700)				Rs. 5.00 / unit
---------------------------------------------------------------
Let  units  be  1200
What  is  the  bill  amount ? --->  100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  500 * 5.00

Hint:  Use  match  ...  case   but  not  if ... else
'''
units = int(input('Enter  units :   '))  #  1200
match  units // 100:
	case  0:  #  units  between  0  and  99
				cost = units * 3.00
	case  1:   #  units  between  100  and  199
				cost =  100 * 3.00 + (units - 100) * 3.50
	case  2 | 3:   #  units  between  200  and  399
				cost = 100 * 3.00 + 100 * 3.50 + (units - 200) * 4.00
	case  4 | 5 | 6:  #  units  between  400  and  699
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 +  (units - 400) * 4.50
	case  _:   #  units >= 700
				cost = 100 * 3.00 + 100 * 3.50 + 200 * 4.00 + 300 * 4.50 +  (units - 700) * 5.00
print('Bill  amount  :  ' , cost)


'''
1) What  is  the  issue  with  match  units: ?  ---> Too  many   values  in  each  case

2) What  is  the   advantage  of  units // 100 ?  --->  Boundaries  are  reduced

3) How  is   units  0  to  99   reduced  to ?  --->  0
    How  is   units  100  to  199   reduced  to  ?  ---> 1
    How  is   units  200  to  399   reduced  to ?  --->  2  and  3
    How  is   units  400  to  699   reduced  to ?  --->  4 , 5  and  6
    How  is   units >= 700 reduced  to ?  --->  _
'''
