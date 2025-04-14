#  Find  outputs (Home  work)
def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  'a'  is  10 , 'b'  is  20 , result  is  30
print(add('Hyder' , 'abad'))  #  'a'  is   'Hyder' , 'b'  is    'abad' , result  is   Hyderabad
print(add(10.8 , 20.6))
print(add(True , False))
print(add(3 + 4j , 5 + 6j))
print(add(25 , 10.8))
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))
print(add(10 , '20'))



'''
1) What  are  the  three  events  in  execution  of  add(10 , 20) ?  --->
	a) add()  function  is  executed  and  10 ,  20  are  passed  to  the  function
	b) 10  and  20  are  copied  to  formal  parameters  'a'  and   'b'
	c) Function  returns  30  which  is  returned  to  the  function  call  add(10 , 20)

2) Finally  add(10 , 20)  is  30

3) int  add(int  a , int  b)
     {
     		return  a +  b;
     }
     What  is  the  drawback  of   'c'  language  function  ?  --->  It  can  add  only  integers  as   'a'  and  'b'  are  integers

4) def   add(a , b):
             return  a + b
    What  is  the  advantage  of  python  function ?  ---> It  can  add  any  type  of  objects
'''
