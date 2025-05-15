# fromkeys()  method  demo  program
tpl = ('R' , 'G' , 'B' , 'Y')
a = dict . fromkeys(tpl)  #  Returns  a  dictionary  where  keys  are  elements of  tuple  and  values  are None's
print(a)  #  {'R' : None , 'G' : None , 'B' : None , 'Y' : None}
print(type(a)) #  <class  'dict'>
b = dict . fromkeys(tpl , 25)    #  Returns  a  dictionary  where  keys  are  elements of  tuple  and  values  are  25's
print(b)  #    {'R' : None , 'G' : None , 'B' : None , 'Y' : None}



'''
fromkeys()   method
------------------------
1) What  does  fromkeys(sequence)  do ? --->
										Returns  a  dictionary  where  keys  are  elements  of  sequence  and  values  are  None's

2) In  other  words,   fromkeys()  method  converts  seqeunce  to  dictionary

3) What  does  fromkeys(sequence , x)  do ? --->
													Returns  a  dictionary  where  keys  are  elements  of  sequence  and  all  values  are  'x'

4) Why  is  fromkeys()  method  called  thru  classname  dict ?  --->  Since  it  is  a  static  method  of  dict  class

Note:
Every  method  of  dict  class  is  non-static  except  fromkeys()  method
'''
