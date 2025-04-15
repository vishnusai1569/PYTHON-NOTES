'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

import time
def generator(x, y):
    while x <= y:
        yield x
        x += 1
for num in generator(10, 20):
    print(num)
    time.sleep(2)