'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  -1
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  46 , 34.8 , False , 95 , -1

sum = 0 + 25 + 10.8 + True + 46 + 34.8 + False + 95

ctr = 0  + 1 + 1 + 1 + 1 + 1 + 1 + 1
'''
try:

    count=0
    sum=0
    while True:
        p=eval(input("Enter input  (-1  to  stop):"))
        if p==-1:
            break
        sum = sum + p
        count = count + 1
    avg=sum/count
    print("average",avg)
except ZeroDivisionError:
    print("1st input is not -1")
except (TypeError,NameError):
    print("input cannot be string")





