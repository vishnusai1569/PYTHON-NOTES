# float()  function  demo  program
print(float(25)) #  Converts  25  to  25.0
print(float(True)) #  Converts   True   to   1.0
print(float(False)) #  Converts   False   to   0.0
print(float('92'))  #  Converts   '92'   to   92.0
print(float('36.4'))  #  Converts   '36.4'   to   36.4
print(float('0075'))  #  Converts   '0075'  to   75.0
print(float(0B1010101)) #  Converts  binary   number  to   decimal  number  i.e.   64 + 16 + 4 + 1 = 85.0
print(float(0O6247))  #  Converts  octal  number  to   decimal  number  i.e.  6 * 8 ^ 3 + 2 * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0 = 3239.0
print(float(0XA7B9))  #  Converts  hexa  decimal   number  to   decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937.0
#print(float(3 + 4j))  #   Error  becoz  complex  number  can  not  be  converted  to  float
#print(float('Ten'))   #   Error  becoz  'Ten'  can  not  be  converted  to  float



'''
float()   function
--------------------
1) What  does  float(x)  do  ?  --->  Converts  object  'x'  to  float

2) Conversion  of  binary  number  to  decimal  number
    -------------------------------------------------------------
           64   32   16   8   4   2   1  --->  Weights
	        1     0     1    0    1   0   1    ---->   64 + 16 + 4 + 1 = 85.0

3) Conversion  of   octal  number  to  decimal  number
     ------------------------------------------------------------
          512   64   8    1  --->  Weights
	       6       2   4    7  --->  6 * 512 + 2 * 64 + 4 * 8 + 7 * 1 = 3239.0

4) Conversion  of  hexa  decimal  number  to  decimal  number
     ---------------------------------------------------------------------
           4096   256   16    1  --->  Weights
             A        7      B     9   --->  10 * 4096 + 7 * 256 + 11 * 16 + 9 * 1 = 42937.0

5) How  to  convert  '25.8'   to   25 ?  --->  int(float('25.8'))

6) Is  int('25.8')  valid ?  --->  No  becoz  string  float  can  not  be  converted  to  integer
'''
