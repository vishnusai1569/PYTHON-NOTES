# end  argument  demo  program
a , b , c = 10 , 20 , 30
print(a , end = '\t') # 10 <tab>  <same  line>
print(b , end = '\t')  #  20 <tab>  <same  line>
print(c) #   30 <next  line>
print('Bye') #  Bye  <next  line>
#print(a , last = '\t') #  Error  becoz  last  is  invalid  argument  for  print()  function



'''
1) What  is  the  default  end ? --->  '\n'

2) Can  end  be  modified  ?  --->  Yes  with  end  argument  of  print()  function

3) What  does  end = 'delimeter'  do ?  --->  Modifies  end  to  the  specified  delimeter

4) How  many  lines  of  outputs  is  generated  when  the  above  program  is  executed ?  --->  2
'''
