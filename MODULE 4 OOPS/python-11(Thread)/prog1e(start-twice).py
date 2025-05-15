# Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
child . start()  #  Error :  child  thread  is  already  started


'''
1) Is  it  possible  to  start  already  started  thread ?  --->   No

2) How  many  times  can  a  thread  be  started  ?  --->  Just  once
'''