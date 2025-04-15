'''
Write  a  program  to  replace  every  occurance  of  first  character  in  the  string  with  '*'  except  first  character

Let  input  be  'babble'
What  is  the  output ?  --->  ba**le

Hint : Use  replace()  method
'''
k=input("enter the string:")
if len(k)>0:
    first=k[0]
    result=first+k[1:].replace(first,'*')
print(result)
