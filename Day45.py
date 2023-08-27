"""
if __name__ == "__main__"
This idion is a common pattern that
we use in python script to determine
whether the script is being run 
directly or being imported as a module
into another script
"""

import test as t

t.welcome()
"""
Without if __name__ == "__main__"
output:
hey welcome to the python world
hey welcome to the python world

why two output:
one calling from this file and other
from the test fie
-------------------------------------------
with if __name__ == "__main__"
output:
hey welcome to the python world
test -- (check test file you will understand)
-----------------------------------------------
why single output:
since we not running the test file 
directly so it will check if __name__
not equal to "__main__" it will not
call from test file as we are importing
test file
"""

print(__name__)
"""
Here output will be:
__main__

but if we import test file and
print __name__ in test file
and call from other file 
by importing output will be
test 
it means test is not main file
"""