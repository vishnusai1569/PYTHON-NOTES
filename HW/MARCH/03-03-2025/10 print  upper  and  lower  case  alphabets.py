'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
1) chr(65) =  'A'
    chr(90) = 'Z'
    chr(97) =  'a'
    chr(122) = 'z'

2) What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character

3) ord('A') =  65
    ord('Z') = 90
    ord('a') =  97
    ord('z') =  122

4) What  does  ord()  function  do ?  --->  Converts  character  to  unicode  value

5) Hint:  Use  two  for  loops
'''

for i in range(65,91):
    print(chr(i),end=" ")
    i+=1
print("")
for i in range(92,98):
    print(chr(i),end=" ")
    i+=1
print()
for i in range(97,123):
    print(chr(i),end=" ")
    i+=1