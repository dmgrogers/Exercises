# Can we call a module that is contained in a parent folder?
# Yes, as long as the working directory is correct

import os
os.getcwd()
os.chdir('/users/david/documents/github/python/testModule')

import hello
hello.world()