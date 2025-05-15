
#  Difference  between  init()    and  __init__()   methods (Home  work)
class c1:
    def  __init__(self):
        print('Constructor')
        self . x = 10
        self . y = 20
class c2:
    def  init(self):
        print('Method')
        self . x = 30
        self . y = 40
a = c1()  #  Object  is  initilaized  with  x = 10 , y = 20  by constructor
print(a . __dict__) #   {'x' : 10 , 'y' : 20}
b = c2()   #  Empt  object
print(b . __dict__)  #  { }
b . init() #  Object  is  initilaized  with  x = 30 , y = 40  by  the method
print(b . __dict__) #   {'x' :30 , 'y' : 40}

'''
Constructor
{'x': 10, 'y': 20}
{}
Method
{'x': 30, 'y': 40}
'''


'''
1) Is  init()  a  method  or  constructor ?  --->   A  method

2) Is  init()  executed  automatically  ?  --->  No  and  it  needs  to  be  called  explicitly

3) What  is   __init__()  called  ?  --->  Constructor

4) What  is  the  advantage  of  constructor ?  --->  It  is  automatically  executed  as  soon  as   object  is  created
'''