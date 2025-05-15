# R  string  demo  program  (Home  work)
a = 'Hyd is \n green \t city'
print(a)  #  Hyd is <next line> green <tab> city
b =  R'Hyd is \n green \t city'
print(b)  # Hyd is  \n green \t city
c = 'Hyd is  \\n green \\t city'
print(c)  # Hyd is  \n green \t city



'''
1) What  are  the  two  ways  to  print  \n ?  --->  print(R'\n')
                                                                                  and
																			 print('\\n')

2) What  does  print('\n') do  ?  --->  Moves  to  next  line  twice  but  does  not  print  \n

3) What  are  the  two  ways  to  print  \t ?  --->  print(R'\t')
                                                                                 and
																	          print('\\t')

4) What  does  print('\t')  do ?  --->  Generates  a   tab  but  does  not  print  \t

5) What  does  R  string  do ?   --->  Does  not  treat  \n  as  new  line  characeter
																			and
													     \t  is  not  treated  as  tab  character

6) What  does  F  stand  for  in   F  string  ? ---> Format  string
    What  does  R  stand  for  in  R  string  ? --->	Raw  string

7) Are  'R'  and  'r'  same ? --->  Yes
'''
