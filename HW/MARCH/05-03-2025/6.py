'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> a . sort()
    How  to  sort  list  'a'  in  descending  order  ?  --->  a . sort(reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  --->  Pls  don't  send  number  and  string  inputs  together
'''


import sys

args = sys.argv[1:]  # Exclude script name

numbers = []
try:
    for i in args:
        numbers.append(eval(i))
    numbers.sort()
    print("assending order",numbers)
    numbers.sort(reverse = True)
    print("desending order",numbers)
except (ValueError,TypeError):
    print("enter the integer values")xc


