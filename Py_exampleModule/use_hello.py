import os
print(os.getcwd())

# Ensure that your current working directory is the folder in which the module scripts are stored.
# os.chdir('/users/david/documents/github/exercises/Py_testModule')

import hello
hello.world()
hello.spiel()

from hello import noHello
noHello()

# Note that it doesn't work to attempt to import a module that is in a sub-folder of the current working directory
import secretModule
secretModule.secretFunction() # doesn't work (and you'll have to kill the terminal)


# For modules in sub-folders, the working directory needs to be changed
os.getcwd()
os.chdir('/users/david/documents/github/References-and-Illustrations/Py_testModule/secretModule')
import secretModule 
secretModule.secretFunction() # This works fine (after a fresh terminal opened)
