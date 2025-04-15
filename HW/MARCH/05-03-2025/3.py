'''
Write  a  program  to  determine  largest  command  line  input

1)
    py   prog2.py   10     20     30.8    7   40    35.6
    What  is  the  largest  command  line  input ?  --->	40
    What  is  argv ?  ---> ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
    What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6]
    How  to  determine  largest  element  of  list  'a' ?  ---> max(a)  i.e.  40
    What  is  the  result  of  max(argv[1:]) ?  --->  '7'
    What  is  the  issue  with  max(argv[1:])) ?  --->  Largest  string  is  obtained  but  not  largest  number  is  obtained  but  not  largest  number

#done 2) py  prog2.py
    What  is  the  output ?  --->	Pls  send  inputs

3) py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar'
    What  is  the  largest  command  line  input ?  --->	'Vamsi'

4) py   prog2.py   25   'Ten'
    What  is  the  output ?  ---> Inputs  can  not  be  number  and  string

5) Hint1: Use  for  loop

6) Hint2: Use  try  and  except
'''

import sys

argv = sys.argv

if len(argv) == 1:
    print("Pls send inputs")
else:
    a = []
    contains_string = False
    contains_number = False

    for arg in argv[1:]:
        try:
            num = float(arg)  # Convert to float if possible
            a.append(num)
            contains_number = True
        except ValueError:
            contains_string = True

    if contains_number and contains_string:
        print("Inputs can not be number and string")
    else:
        if contains_string:
            print("What is the largest command line input ? --->", max(argv[1:]))
        else:
            print("What is the largest command line input ? --->", max(a))