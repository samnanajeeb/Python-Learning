#Write a Python program to get the Python version you are using
#The python sys module provides functions and variables which are used to manipulate different parts of the Python Runtime Environment.
import sys
print("Python Version")
print(sys.version)
print("Version")
print(sys.version_info)

"""Python defines an in-built module platform that provides system information.
The Platform module is used to retrieve as much possible information about 
the platform on which the program is being currently executed.
Now by platform info, it means information about the device, 
it’s OS, node, OS version, Python version, etc. 
This module plays a crucial role when you want to check whether your program is 
compatible with the python version installed on a particular system or 
whether the hardware specifications meet the requirements of your program"""

import platform
print(platform.python_version())

#Python defines an in-built module platform that provides system information.
import platform
print(platform.python_version_tuple())
print(type(platform.python_version_tuple()))