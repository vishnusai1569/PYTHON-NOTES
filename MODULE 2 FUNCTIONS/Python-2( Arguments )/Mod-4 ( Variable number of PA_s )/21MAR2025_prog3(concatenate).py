'''
Gift : 100
Write  a  function  to  concatenate  strings  passed  from  the  function  call ? (Home  work)
'''
def  concat(*a):
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
	try:
		return ' '.join(a)
	except:
		return  'Pass  strings  from  the  function  call'
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))   #   Tuple  of  3  strings  is  passed to  the  function  and  the  result  is  Sankar Dayal Sarma
print(concat('Hyd', 'Is', 'Green', 'City'))   #   Tuple  of  4  strings  is  passed to  the  function  and  the  result  is   Hyd Is Green City
print(concat('Python', 'Is', 'A', 'Great', 'Language')) # Tuple  of  5  strings  is  passed to  the  function  and  the  result  is  Python Is A Great Language
print(concat())   #  Empty  tuple   is  passed to  the  function  and  the  result  is  empty  string
print(concat('Python'))   #   Tuple  of  sinlge  string  is  passed to  the  function  and  the  result  is   Python
print(concat(1, 2, 3))  #   Tuple  of  3   integers  is  passed to  the  function  and  the  result  is   Pass  strings  from  the  function  call



'''
a = (1 , 2 , 3)
What  is  the  issue   with  ' ' . join(a)  ?  --->   It  is  not  tuple  of  strings  and   hence  can  not  be  joined
'''
