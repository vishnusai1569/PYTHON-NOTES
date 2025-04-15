'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->	[20 , 30 , 40]

2) Both  input  and  output  are  lists
'''

a,b=eval(input("enter the list 1:")),eval(input("enter the list 2:"))
c,d=set(a),set(b)
print(list(k:=c.intersection(d)))

