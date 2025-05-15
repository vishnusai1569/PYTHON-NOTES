'''
Write  a  program  to  print  distinct  vowels  of  the  string  using  filter.
Input  is  string  and  output  is  set
'''
s = input('Enter  mixed  case   string  :  ') . upper()
f = filter(lambda  ch : ch  in   'AEIOU' ,  s)
print(set(f))



'''
1) What  does  set(f)  do ?  ---  All  the  vowels   of  string  's'   are  stored  in  filter  object  'f'   and
											      converted  to  set

2) Let  input  be  Rama  Rao,
    What  does  filter  object  'f'  contain ?  --->  'A'   'A'   'A'   'O'
    What  does  set  object  contain ?  --->  {'A' , 'O'}
'''