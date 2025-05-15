#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__) # ([],)
f1(3) #  'x'  is  3 ,  'a'  is   default  value   []   and  result  is [3]
print('__defaults__  :  ' , f1.__defaults__) # ([],)
f1(4 , [1 , 2 , 3]) # 'x'  is  4 ,  'a'  is  [1 , 2 , 3]    and  result  is [1 , 2 , 3 , 4]
print('__defaults__  :  ' , f1.__defaults__)# ([],)
f1(4) # 'x'  is  4 ,  'a'  is   default  value   []   and  result  is [4]
print('__defaults__  :  ' , f1.__defaults__)# ([],)
f1(40 , [10 , 20 , 30]) #  'x'  is  40 ,  'a'  is   [10 , 20 , 30]  and  result  is [10 , 20 , 30 , 40]
print('__defaults__  :  ' , f1.__defaults__)# ([],)
f1(5) # 'x'  is  5 ,  'a'  is   default  value   []   and  result  is [5]
print('__defaults__  :  ' , f1.__defaults__)# ([],)
f1([6 , 7 , 8]) # # 'x'  is  [6 , 7 , 8] ,  'a'  is   default  value   []   and  result  is [[6 , 7 , 8]]
print('__defaults__  :  ' , f1.__defaults__)# ([],)
