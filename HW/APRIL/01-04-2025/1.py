
'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  retrieve  elements
'''
def f1(a, b):
    yield f'sum :{a + b}'
    yield f'Differnece :{a - b}'
    yield f'Product :{a * b}'
    if b != 0:
        yield f'Division :{a / b}'
    else:
        yield "Division by zero is not allowed"
num1=int(input("enter the first no:"))
num2=int(input("enter the first no:"))
for result in f1(num1, num2):
    print(result)