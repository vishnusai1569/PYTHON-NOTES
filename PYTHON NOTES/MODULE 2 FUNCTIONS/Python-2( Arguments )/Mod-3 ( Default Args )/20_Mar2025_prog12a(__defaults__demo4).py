# Find  outputs (Home  work)
def   f1(x , a = []):
	a . append(x)
	print('List :  ' ,  a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__) # ([],)
f1(3) #  'x'  is  3 ,  'a'  is   default  value   []   and  result  is [3]
print('__defaults__  :  ' , f1.__defaults__) # ([3],)
f1(4 , [1 , 2 , 3]) #   'x'  is  4 ,  'a'  is   [1 , 2 , 3],   and  result  is [1 , 2 , 3 , 4]
print('__defaults__  :  ' , f1.__defaults__) # ([3] ,)
f1(9) #  'x'  is  9 ,  'a'  is   default  value   [3]   and  result  is [3 , 9]
print('__defaults__  :  ' , f1.__defaults__)  #  ([3 , 9],)
f1(40 , [10 , 20 , 30])   #   'x'  is  40 ,  'a'  is   [10 , 20 , 30],   and  result  is [10 , 20 , 30 , 40]
print('__defaults__  :  ' , f1.__defaults__) #  ([3 , 9],)
f1(5) #  'x'  is  5 ,  'a'  is   default  value   [3 , 9]   and  result  is [3 , 9 , 5]
print('__defaults__  :  ' , f1.__defaults__)  #   ([3 , 9 , 5],)
f1([6 , 7 , 8])   #  'x'  is  [6,7,8] ,  'a'  is   default  value   [3 , 9 , 5]   and  result  is [3 , 9 , 5 , [6 , 7 , 8]]
print('__defaults__  :  ' , f1.__defaults__)  #   ([3 , 9 , 5 , [6 , 7 , 8]],)



'''
1) When  is  __defaults__  automatically  modified ?  --->  As  soon  as  function  modifies  default  argument

2) When  is   __defaults__  unchanged ?  --->  When  function  modifies  actual  parameter  (or)  local  list
'''
