'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
a = input('Enter Mixed Case String : ')
a = sorted(a . upper())
b = { }
for  ch  in   a:
       if  ch  in   'AEIOU':
                b[ch] = b . get(ch , 0) + 1
# End  of  for  loop
print(b)
