# hex()  function  demo  program
print(hex(25))   #  Converts  decimal  number  to  hexa  decimal  number   i.e.  0X19
print(hex(0B10101111010111))   #  Converts  binary   number  to  hexa  decimal  number   i.e.  0X2BD7
print(hex(0O6247))    #  Converts  octal   number  to  hexa  decimal  number   i.e.    0XCA7



'''
hex()  function
------------------
1) What  does  hex(x)  do ?  --->  Converts  object  'x'  to  hexa-decimal  number  where
								                     'x'  can  be  binary / decimal / octal  number

2) Conversion  of  decimal  number  to  hexa  decimal  number
    ---------------------------------------------------------------------
		    Number      Quotient     Remainder
			  25                1                   9
			   1                  0                  1
    Remainders  in  the  reverse  order   --->  19

3) Conversion  of  binary  number  to  hexa  decimal  number  (2  ^ 4 =    16)
    ---------------------------------------------------------------------
	     8   4   2   1		8   4   2   1		8   4   2   1		8   4   2   1  --->  Weights
	     0   0   1   0	    1   0    1   1       1    1   0   1		0   1    1   1
			     2                     B                      D                     7

4) Conversion  of  octal  number  to  binary  number  (2 ^ 3 =  8)
    -----------------------------------------------------------
	    4   2   1		4   2   1		4   2   1	    	4   2   1	  --->  Weights
	    1    1   0    0   1   0     1   0   0        1    1   1    ---> binary  number

    Conversion  of  binary  number  to  hexa  decimal  number  (2  ^ 4 =  16)
    --------------------------------------------------------------------
	    8   4   2   1		8   4   2   1		8   4   2   1  --->  Weights
	    1   1    0   0        1   0    1   0      0   1    1   1
		       C                       A                     7
'''
