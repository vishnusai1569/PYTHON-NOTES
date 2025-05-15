prog1(output).py

from  random  import  *
print(random())  #  random  number  between  0 (excluded)  and   1 (excluded)  --->  0.5
print(randint(1 , 100))  #  random   integer  number  between  1 (included)  and   100 (included)  --->   72
print(uniform(1 , 100))  #  random  float  number  between  1 (excluded)  and   100 (excluded)  --->   35.6
print(randrange(10)) #  random  number  between  0 (included)  and   10 (excluded)  --->    7
print(randrange(1 , 11))  #  random  number  between  1 (included)  and   11 (excluded)  --->     3
print(randrange(1 , 11 , 2))  #  random  number  between  1 (included)  and   11 (excluded)   in  steps  of  2  --->   9
list = [10 , 20 , 15 , 12 , 18]
print(choice(list))  #  random  element  of   list  i.e.  15
print(choice('RAJESH'))  #  random  char  of   string  i.e.  J
set  =  {10 , 20 , 30 , 40}
#print(choice(set))  #   Error :  set  is  not  indexed



'''
1) What  does  random(No-Args)  do ? --->  Returns  random  float  number  between  0  and  1(Excluding  0  and  1)

2) What  does  randint(x , y)  do ? --->  Returns  random  integer  number  between  x  and  y (both  inclusive)

3) What  does  uniform(x , y)  do ? --->  Returns   a  random  float  number  between  x  and  y (both  exclusive)

4) What  does  randrange(x)  do ?  ---> Returns  random  integer  number  between  0  and  x  - 1 (Both  inclusive)
    What  does  randrange(x , y)  do ?  --->
												Returns  random  integer  number  between  x  and  y - 1 (Both  inclusive)  in  steps  of   1
    What  does  randrange(x , y , z)  do ? ---> Returns  random  integer  number  between  x  and  y - 1  in  steps  of  'z'

5) What  does  choice(sequence)  do ? ---> Returns  a  random  element  of  the  sequence

6) Is  choice(set)  valid ?  --->
									No  becoz  argument  can  be  any  sequence  except  set  and  dictionary  as   they  are  not  indexed
'''