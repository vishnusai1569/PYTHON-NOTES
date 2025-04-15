# split()  method demo program
a = '15-Aug-1947'
b = a . split('-')   #  Divides  string  into  list  of  strings  based  on   '-'  delimeter
print(b) #   ['15' , 'Aug' , '1947']
print(type(b)) #   <class  'list'>
for   x  in   b: #  x  is  each  element  of  list  'b'
	print(x) #  15  <next  line>  Aug  <next  line>  1947  <next  line>


'''
split()  method
------------------
1) What  does  split()  method  do ? --->  Divides  a  string  into  list  of  strings  based  on  delimeter

2) What  is  the  input  and  output  of  split()  method ? ---> Input  is  string  and  output  is  list  of  strings

3) What  is  the  argument  of  split()  method ?  --->  Delimeter  string

4) Is  split(No  args)  valid  ? --->  Yes  and  default  delimeter  is  white  space

5) What  is  white  space ?  --->  ' ' , '\n'  and  '\t'

6) In  other  words,  split(No  args)  divides  string  based  on  three  delimeters

7) '15-Aug-1947' . split('-')
     What  does  above  method  do  ? ---> Divides  date  string  into  [date , month , year]
'''
