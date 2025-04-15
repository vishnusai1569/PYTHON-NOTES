# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]
del  list

"""
Object  is  created  at  address  :   4333742336
Object  is  created  at  address  :   4335716944
Object  is  created  at  address  :   4335717264
Object  at  address  4335717264  is  lost 
Object  at  address  4335716944  is  lost 
Object  at  address  4333742336  is  lost 
"""