# Find  outputs(Home  work)
class  c1:
        def     __init__(self):
                print('Object  is  created  at  address  :  ' , id(self))
        def     __del__(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#End of the class
list = [c1() , c1() , c1()]  #   Executes  constructor  thrice  becoz  3  objects  are  created
del  list  #   Executes  destructor  thrice   before  the  3  objects  are  lost  in  reverse order

'''
Object  is  created  at  address  : address of 1st c1 class  object
Object  is  created  at  address  : address of 2nd c1 class  object
Object  is  created  at  address  : address of 3rd c1 class  object
Object  at  address  address of  3rd  c1 class  is  lost
Object  at  address  address of 2nd c1 class  is  lost
Object  at  address  address of 1st  c1 class  is  lost
'''


'''
1) What  are  the  five  events  for  del   list ?  --->
    a) List  reference  is  deleted
    b) List  is  also  lost  becoz  there  is  no  reference  to  the  list
    c) List  class  destructor(i.e. empty  destrcutor)  is  executed  before  list  is  lost
    d) The  three  c1  class  objects  are  also  lost  in  reverse  order  becoz  they  have  no  references
	e) Destructor  is  executed  before  each  object  is  lost

2) What  is  the  order  in  which  objects  are  lost  when  they  are  independent  objects ?  --->  Same  order
																										i.e.  The  order  in  which  they  were  created
																												Eg:   a = c1()
																												        b = c1()
																												        c = c1()

3) What  is  the  order  in  which  objects  are  lost  when  it  is  list   of  objects ?  --->  Reverse  order  of  creation
																																		    Eg:  list = [c1() , c1() , c1()]
'''