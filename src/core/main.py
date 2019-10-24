#!/usr/bin/env python
#coding=utf-8

"""
main.py: When creating a Python module, it is common to make
         the module execute some functionality (usually contained
         in a main function) when run as the entry point of
         the program.
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "0.1.2"
__status__      = "Development"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
__credits__     = [
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

import os
import sys

from os import path

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinPath = os.path.join(basePath, '..')
pathAbsPath = os.path.abspath(joinPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathAbsPath)

# Appending variables path
varsPath = os.path.join(joinPath, 'variables')
varsAbsPath = os.path.abspath(varsPath)
sys.path.append(varsAbsPath)
sys.path.insert(0, varsAbsPath)

# Importing available variables
from base import *
from messages import *
from paths import *

# Appending methods path
methodsPath = os.path.join(joinPath, 'methods')
methodsAbsPath = os.path.abspath(methodsPath)
sys.path.append(methodsAbsPath)
sys.path.insert(0, methodsAbsPath)

# Importing available methods
from accessing import *

# Appending tests path
testsPath = os.path.join(joinPath, 'tests')
testsAbsPath = os.path.abspath(testsPath)
sys.path.append(testsAbsPath)
sys.path.insert(0, testsAbsPath)

# Importing available tests
from comparisons import *

def main():
  dwnldMainServImgStorOnDicomServ(pth003, lnk003, lnk005)

if __name__ == '__main__':
  main()

# ==================== END File ==================== #
