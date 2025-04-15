# Which  is  a  better  approach  to  read  string  input ?
a = input('Enter  any  string  :  ')  #    Hyd
print(len(a))  #  3
print(a)  # Hyd
b = eval(input('Enter   any  string  : '))  #   'Hyd'
print(len(b))  # 3
print(b) #  Hyd



'''
1) What  is  the  issue  with  eval(input())  for  string  input ?  --->  Input  string  has  to  be   in  quotes

2) What  is  the  advantage  of  input()  function  for  string  input ?  --->  Input  string  should  not  be  in   quotes

3)  Input      input()   reads     eval(input())  returns
   --------------------------------------------------------------------------------
	  Hyd            'Hyd'                 eval('Hyd')  converts  'Hyd'  to  object  Hyd

     'Hyd'           "   'Hyd'  "        eval("   'Hyd'  ")   is   'Hyd'
'''
