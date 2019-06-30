#!/usr/bin/env python
#coding=utf-8
import unittest
from baseFindersDatasets import *
from messagesFindersDatasets import *
from pathsFindersDatasets import *
from os import path as ospath
from sys import path as syspath

"""
.py:
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.0"
__status__      = "Development"
__copyright__   = "Copyright 2019, Instituto Superior Técnico (IST)"
__credits__     = [
  "Bruno Oliveira",
  "Carlos Santiago",
  "Jacinto C. Nascimento",
  "Pedro Miraldo",
  "Nuno Nunes"
]

def appendPathFor(pathName):
  varsPath = ospath.join(joinPath, pathName)
  varsAbsPath = ospath.abspath(varsPath)
  syspath.append(varsAbsPath)

basePath = ospath.dirname(__file__)

# The path to the repository "src" folder.
joinPath = ospath.join(basePath, '..')
pathAbsPath = ospath.abspath(joinPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
syspath.append(pathAbsPath)

# The path to the repository "root" folder.
rootPath = ospath.join(basePath, '..', '..', '..')
rootAbsPath = ospath.abspath(rootPath)

appendPathFor('variables')
appendPathFor('methods')

class ComparisonsTest(unittest.TestCase):

  def test_medical_images(self):
    varToTest = 1 + 1
    varResult = 2
    self.assertEqual(varToTest, varResult)

if __name__ == "__main__":
  unittest.main()
