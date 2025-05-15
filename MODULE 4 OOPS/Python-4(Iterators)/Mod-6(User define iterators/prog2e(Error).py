# Identify  Error
class   c6:  #  c6  is  neither  iterable  nor  iterator  (There  is  no  __iter__()  nor  __next__()  method)
        def   iter(self):
                return   reversed([10 , 20 , 15 , 18])
        def  next(self):
                print('next  method')
# End  of  the  class
a  =  c6() #   Empty  object
print(dir(c6)) #   ['iter' , 'next'  , Ev's]
'''
for  x  in  a: #   Error :  'a'  is  not  iterable   object
        print(x)
while  True:
	print(next(a))  #  Error :  'a'  is not  an  iterator
'''
a . next()  #  Executes  next()  method   of  class   c6