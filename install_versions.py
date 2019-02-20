#!/usr/bin/python

import os
import platform

initial_version = platform.python_version()
os.system("pyenv install 3.7.1")
os.system("pyenv install 2.7.1")

os.system("pyenv local 3.7.1")
os.system("pyenv virtualenv python3")

os.system("pyenv local 2.7.1")
os.system("pyenv virtualenv python2")

os.system("pyenv local {}".format(initial_version))
