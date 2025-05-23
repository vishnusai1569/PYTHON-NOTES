#  Find  outputs  (Home  work)
import  re
m = re . search('^learn' , 'Learning Python is simple' , re . IGNORECASE)
if  m:  #  True  :  Match  is  a  non-empty  object
	print('String  starts  with' , m . group())  #   String  starts  with Learn
else:
	print('String  does  not  start  with  learn')
m = re . search('Simple$' , 'Learning Python is simple' , re . IGNORECASE)
if   m:  #  True  :  Match  is  a  non-empty  object
	print('String  ends  with ' , m . group())  #  String  ends  with  simple
else:
	print('String  does  not  end  with  Simple')