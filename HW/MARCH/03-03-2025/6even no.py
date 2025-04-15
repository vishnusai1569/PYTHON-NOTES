'''
(Home  work)
Write  a  program  to  print  first  20  even  numbers  with  while  loop

1) What  are  the  first  20  even  numbers ?  --->  2 , 4 , 6 , 8 , ....   40

2) What  is  printed  in  general ?  --->  2 * i  where  i  varies  from  1  to  20

3) Use  while  loop
'''


num = int(input("Enter the number of even numbers to print: "))
count = 0
i = 2
while count < num:
    print(count,i)
    i += 2
    count += 1

