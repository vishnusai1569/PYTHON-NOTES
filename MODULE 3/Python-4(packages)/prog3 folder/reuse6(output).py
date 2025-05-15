# Save  in  any  file  of  cwd
import   p1 #  Executes  __init__  module  of   package  p1
import  p1 . mod1  #  Does not  execute  __init__  module  of   package  p1  as  it  is  already  executed
from   p1   import  mod1  #  Does not  execute  __init__  module  of   package  p1  as  it  is  already  executed 0
from   p1 . mod1  import   * #  Does not  execute  __init__  module  of   package  p1  as  it  is  already  executed
import  p1 . __init__   #  Does not  execute  __init__  module  of   package  p1  as  it  is  already  executed

'''
__init__   module  of  package  p1  is  executed
__init__   module  of  package  p1.__init__  is  executed
'''