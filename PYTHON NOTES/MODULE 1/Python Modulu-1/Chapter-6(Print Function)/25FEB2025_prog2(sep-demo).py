# sep  argument  demo  program  (Home  work)
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c , sep = ',')    #  25 , 10.8 , Hyd
print(a , b , c , sep = '\t') #   25  <tab> 10.8  <tab>  Hyd
print(a , b , c , sep = '---')  #  25  --- 10.8 ---  Hyd
print(a , b , c , sep = '\n')  #  25  <next  line>  10.8 <next  line>  Hyd
print(a , b , c) #   25  <space>  10.8  <space>  Hyd
#print(a , b , c , separator = ':')  #  Error  becoz  separator  is  an  invalid  arg  to  print()




'''
1) What  is  the  default  separator  for  print()  function ?  --->  Space

2) Can  separator  be  modified  ? --->  With  sep  argument  of print()  function

3) What  does  sep = 'delimeter'  do ?  --->  Modifies  the  separator  to  the  specified  delimeter

4) print(object , sep = ' , ')
    Is  sep  argument  required  in  the  above  print()  function ?  ---> No  becoz  single  object  is  being  printed

5) When  is  sep  argument  required  in  print()  function  ?  --->  When  more  than  one  object  is  being  printed

6) What  is  the  separator  between  hours , minutes  and  seconds ?  --->  ':'  i.e.  sep = ':'
    What  is  the  separator  between  date , month  and  year ?  --->  '-'  (or) '/'  (or)  '.'
'''
