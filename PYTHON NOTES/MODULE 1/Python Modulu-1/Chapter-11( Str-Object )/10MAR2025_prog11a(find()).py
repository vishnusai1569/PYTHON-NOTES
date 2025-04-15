# find()  method  demo  program
# a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
# index = a . find('is')   #   Index  of  first  'is'  in  object  'a'  i.e. 4
# while  index != -1:  #  Repeat  until  there is  no 'is'
# 	print(index) #    Index  of  each  'is'  in  object  'a'
# 	index = a . find('is' , index + 1)  #   Index  of  next  'is'
# print('End')

# a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
#
# index = a.rfind('is')  # Start from the last occurrence of 'is'
#
# while index != -1:
#     print(index)
#     index = a.rfind('is', 0, index)  # Search for 'is' before the current index
#
# print('End')

a = 'Hyd   is   green   city'  #  There   are   3  spaces  between  the  words
print(a . split())
print(a . split(' '))



'''
find()  method
------------------
1) What  does  str1 . find(str2  , x , y)  do ?  ---> Returns  index  of  str2  in  str1  between  indexes  x  and  y - 1
    What  does  str1 . find(str2  , x)  do ?  ---> Returns  index  of  str2  in  str1  between  indexes  x  and  len(str1) - 1
    What  does  str1 . find(str2)  do ?  ---> Returns  index  of  str2  in  str1  between  indexes  0  and  len(str1) - 1

2) How  many  arguments  can  find()  method  take ?  ---> 1 , 2  (or)  3

3) What  does  find()  method  do  if  str2  is  not  in  str1 ?  --->  Returns  -1

4) What  is  the  similarity  between  find()  method  and  'in'  operator ?  --->
																								Both  of  them  search  for  a  string  in  another  string

5) What  is  the  difference  between  find()  method  and   'in'  operator ?  --->
																	in  operator  returns  True / False  but  find()  method  returns  index

Note:
     Method  call	   Search  from  index      find()  method  returns
    -------------------------------------------------------------------------------------------------
             1                           0                                    4

		    2							 5                                    23

			3							 24                                  42

			4							 43                                  46

			5							 47                                  -1
'''
