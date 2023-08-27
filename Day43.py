"""
Virtual Environment in Python:
-----------------------------
A virtual environment is a tool used
to isolate specific python environment
on a single machine, allow you to work
on multiple project with different 
package version

step1:create the virtual enviroment
      python3 -m venv myenv

step2:activate the virtual environemtn
      source myenv/bin/activate

step3:Deactivate the virtual environment
      deactivate

Now you can install whatever you want
it will not affect your local machine

try: pip3 install pandas
"""
import pandas as pd

print(pd.__version__)

"""
Inside your virtual environment 
you will be able to see panda version
but if it is not installed in local
you will not be able to see

output:
    1.inside virtual environment
      2.0.3
    2.outside virtual environment
      ModuleNotFoundError: No module named 'pandas'
"""


"""
requirement.txt

To create requirement.txt file
with all the packages installed

use command --
pip freeze >requirement.txt

It will create the requirement.txt file
that you can use later


command ---
pip freeze --list all the packages installed
             and their version


command --
pip install -r requirements.txt

this command will read requirement.txt and
install all the packages with required
version in the virtual environment
or wherever is required
"""
