#!/usr/bin/env python
#coding=utf-8

"""
main.py: When creating a Python module, it is common to make
         the module execute some functionality (usually contained
         in a main function) when run as the entry point of
         the program.
"""

__author__      = "Francisco Maria Calisto, Bruno Oliveira"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.3"
__status__      = "Development"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
__credits__     = [
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

from os import path as ospath
from sys import path as syspath
# from accessingFindersDatasets import *
# from baseFindersDatasets import *
# from messagesFindersDatasets import *
# from pathsFindersDatasets import *
# from comparisonsFindersDatasets import *

def appendPathFor(pathName):
  testsPath = ospath.join(joinPath, pathName)
  testsAbsPath = ospath.abspath(testsPath)
  syspath.append(testsAbsPath)
  syspath.insert(0, testsAbsPath)

basePath = ospath.dirname(__file__)
# The path to the repository "src" folder.
joinPath = ospath.join(basePath, '..')
pathAbsPath = ospath.abspath(joinPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
syspath.append(pathAbsPath)

appendPathFor('variables')
appendPathFor('methods')
appendPathFor('tests')

from accessingFindersDatasets import *

def main():
  getMedicalImages(pth003, lnk003, lnk005)

if __name__ == '__main__':
  main()

# ==================== END File ==================== #
