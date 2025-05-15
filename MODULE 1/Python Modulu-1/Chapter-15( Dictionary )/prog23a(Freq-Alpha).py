'''
(Home  work)
Write  a program  to  determine  frequency  of  each  alphabet  in  the  string   in   alphabetical  order  (ignoring  the  case)

Let  input  be   RamA raO
What  is  the  output ?  --->  {'A' : 3 , 'M' : 1 , 'O' : 1 , 'R' : 2}  in  alphabetical  order

Hint: Use  get()  method


1) a = { }

2) a['R'] = a . get('R' , 0) + 1 =  0 + 1 = 1
    What  does  a['R']  =  1  do ?  ---> Appends  'R' : 1  to  dictionary  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 1}

3) a['A'] = a . get('A' , 0) + 1 =  0 + 1 = 1
    What  does  a['A']  =  1  do ?  --->  Appends  'A' : 1  to  dictionary  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 1 , 'A' : 1}

4) a['M'] = a . get('M' , 0) + 1 =  0 + 1 = 1
    What  does  a['M']  =  1  do ?  ---> 	Appends  'M' : 1  to  dictionary  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 1 , 'A' : 1 , 'M' : 1}

5) a['A'] = a . get('A' , 0) + 1 =  1 + 1 = 2
    What  does  a['A']  =  2  do ?  --->  Modifies  value  of  'A'  to  2   in  dictionary  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 1 , 'A' : 2 , 'M' : 1}

6) a['R'] = a . get('R' , 0) + 1 =  1 + 1 = 2
    What  does  a['R']  =  2  do ?  --->  Modifies  value  of  'R'  to  2   in  dictionary  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 2 , 'A' : 2 , 'M' : 1}

7) a['A'] = a . get('A' , 0) + 1 =  2 + 1 = 3
    What  does  a['A']  =  3  do ?  --->  Modifies  value  of  'A'   to   3  in  dictionary  'a'
    What  is  dictionary  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1}

8) a['O'] = a . get('O' , 0) + 1 =  0 + 1 = 1
    What  does  a['O']  =  1  do ?  --->  Appends  'O' : 1  to  dictionary  'a'
    What  is  dictionary  'a' ?  ---> {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}

9) Finally  what   is  dict  'a' ?  --->  {'R' : 2 , 'A' : 3 , 'M' : 1 , 'O' : 1}
'''
a = input('Enter  mixed  case  string : ')
b = sorted(a . upper())
c = { }
for  ch  in   b:
	if  ch . isalpha():
		c[ch] = c . get(ch , 0) + 1
# End  of  for  loop
print(c)




'''
Let  input  be  RamA  raO
1) What  does  object  'a'  contain ?  --->  'RamA  raO'

2) What  is  object  'b' ?   --->  [' ' , 'A' , 'A' , 'A' ,  'M' , 'O' , 'R' , 'R']

3)   ch    c . get(ch , 0)                  c[ch]                                dict  'c'
    ---------------------------------------------------------------------------------------------
                                                                                                 { }
       ' '           -----                         -----------                            {}
       'A'   c . get('A' , 0) = 0       c['A'] = 0 + 1 = 1                   {'A' : 1}
       'A'   c . get('A' , 0) = 1       c['A'] = 1 + 1 = 2                   {'A' : 2}
       'A'   c . get('A' , 0) = 2       c['A'] = 2 + 1 = 3                  {'A' : 3}
       'M'   c . get('M' , 0) = 0      c['M'] = 0 + 1 = 1                  {'A' : 3 , 'M' : 1 }
       'O'   c . get('O' , 0) = 0      c['O'] = 0 + 1 = 1                   {'A' : 3 , 'M' : 1 , 'O' : 1 }
       'R'   c . get('R' , 0) = 0       c['R'] = 0 + 1 = 1                   {'A' : 3 , 'M' : 1 , 'O' : 1  , 'R' : 1}
       'R'   c . get('R' , 0) = 1        c['R'] = 1 + 1 = 2                   {'A' : 3 , 'M' : 1 , 'O' : 1  , 'R' : 2}
'''
