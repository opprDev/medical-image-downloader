#!/usr/bin/env python
#coding=utf-8

"""
comparisons.py: Testing comparisons for our set of methods and files.
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
import json
import sys
import requests
import unittest

from os import path
from pprint import pprint
from time import gmtime, strftime

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
joinPath = os.path.join(basePath, '..')
pathAbsPath = os.path.abspath(joinPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(pathAbsPath)

# The path to the repository "root" folder.
rootPath = os.path.join(basePath, '..', '..', '..')
rootAbsPath = os.path.abspath(rootPath)

# Appending variables path.
varsPath = os.path.join(joinPath, 'variables')
varsAbsPath = os.path.abspath(varsPath)
sys.path.append(varsAbsPath)

# Appending methods path.
modsPath = os.path.join(joinPath, 'methods')
modsAbsPath = os.path.abspath(modsPath)
sys.path.append(modsAbsPath)

# Importing ALL available variables
from base import *
from messages import *
from paths import *

class ComparisonsTest(unittest.TestCase):

  # TODO
  def test_medical_images(self):
    varToTest = 1 + 1
    varResult = 2
    self.assertEqual(varToTest, varResult)

if __name__ == "__main__":
  unittest.main()

# ==================== END File ==================== #
