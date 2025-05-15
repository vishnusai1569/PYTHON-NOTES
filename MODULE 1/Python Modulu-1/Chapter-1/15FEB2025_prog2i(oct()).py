# oct()  function  demo  program
print(oct(195))  # Converts   decimal  number  to octal   number  i.e.   0O303
print(oct(0B10101110010))   # Converts  binary   number  to octal   number  i.e.   0O2562
print(oct(0xA7B9))   # Converts  hexa  decimal  number  to octal   number  i.e.   0O123671



'''
oct()  function
-----------------
1) What  does  oct(x)  do ?  --->  Converts  object  'x'  to  octal  number  where  
								                    'x'  can  be  binary / decimal / hexa-decimal  number

2) Conversion  of  decimal  number  to  octal  number
     -----------------------------------------------------------
          Number      Quotient     Remainder
	       195               24                3
	        24                 3                 0
	         3                  0                 3
    Remainders  in  the  reverse  order   --->  303

3) Conversion  of binary  number  to  octal  number  (2  ^  3 =  8)
    ----------------------------------------------------------
	    4   2   1		4   2   1		4   2   1	    	4   2   1  --->  Weights
	    0   1   0     1   0   1     1   1   0         0   1   0
		     2              5              6                  2   --->  octal  number

4) Conversion  of  hexa  decimal  number  to  binary  number (2 ^ 4 = 16)
     --------------------------------------------------------------------
	     8   4   2   1		8   4   2   1		8   4   2   1		8   4   2   1  --->  Weights
	     1    0   1   0      0    1   1   1       1    0   1   1       1    0   0   1   --->  Binary  number

    Conversion  of  binary  number  to  octal  number  (2 ^  3  =   8)
    ----------------------------------------------------------
	    4   2   1		4   2   1		4   2   1	    	4   2   1	    	4   2   1	    	4   2   1
	    0   0   1		0   1   0 	0   1    1        1   1    0        1    1   1         0   0   1
		     1               2             3                  6                   7                  1
'''
