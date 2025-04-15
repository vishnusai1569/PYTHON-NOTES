'''(Home  work)
rfind()  method  demo  program

Modify  following  program  with  rfind()  method
'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
index = a . rfind('is' , 0 , len(a))  #   46
while  index != -1:
	print(index) #  46 , 42 , 23 , 4
	index = a . rfind('is' , 0 , index - 1)  #   -1
print('End')  #  End



'''
rfind()  method
-------------------
1) What  does  str1 . rfind(str2 , x , y)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  y - 1  downto  x
																			  i.e. right  to  left

2) What  does  str1 . rfind(str2)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  len(str1) - 1  downto  0
																     i.e. right  to  left

3) What  does  str1 . rfind(str2 , x)  do ?  --->  Returns  index  of  str2  in  str1   between  indexes  x  to  len(str1) - 1
														                  i.e.  left  to  right

4) How  many  arguments  can  rfind()  method  take ?  --->  1 (or) 3  but  not  2

5) What  is  the  issue  with  two  arguments ?  --->  Method  searches  from  left  to  right  even  though  it  is  rfind()  method

6) What  does  rfind()  method  return  (+ve  (or)  -ve  index) ?  --->  +ve  index  even  though  search  is  from  right  to  left

7) What  does  rfind()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1

Note:
    Method  call	    Boundaries  of  search       rfind()  method  returns
    -------------------------------------------------------------------------------------------------
             1                    length - 1  downto  0                 46

			 2                   45  downto  0                            42

		     3					 41  downto  0                             23

		     4                   22  downto  0                            4

		     5                   3  downto  0                              -1
'''
