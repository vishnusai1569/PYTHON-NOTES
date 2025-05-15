'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
a = input('Enter  any  string :  ')
b = a[0] + a[1:] . replace(a[0] , '*')  #  'b' + 'a**le'
print('Result :  '  ,  b)
