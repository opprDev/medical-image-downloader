#!/usr/bin/env python
#coding=utf-8

"""
paths.py: All paths for the project.
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
  "Nuno Nunes",
  "Duarte Figueirôa"
]

import os
import json
import sys
import requests

from os import path

# The current folder path.
basePath = os.path.dirname(__file__)

# The path to the repository "src" folder.
srcPath = os.path.join(basePath, '..')
srcAbsPath = os.path.abspath(srcPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(srcAbsPath)

# The path to the repository "src" folder.
repoPath = os.path.join(basePath, '..', '..')
repoAbsPath = os.path.abspath(repoPath)
# Add the directory containing the module to
# the Python path (wants absolute paths).
sys.path.append(repoAbsPath)

# The path to the repository "root" folder. Mainly,
# this will put us at the `Git` folder level.
rootPath = os.path.join(basePath, '..', '..', '..')
rootAbsPath = os.path.abspath(rootPath)
sys.path.append(rootAbsPath)

# Appending methods path.
methsPath = os.path.join(srcPath, 'methods')
methsAbsPath = os.path.abspath(methsPath)
sys.path.append(methsAbsPath)

# Appending tests path.
testsPath = os.path.join(srcPath, 'tests')
testsAbsPath = os.path.abspath(testsPath)
sys.path.append(testsAbsPath)

# ============================== #
#             DATASETS           #
# ============================== #

# Path to the Dataset Folders
pathToAnno = os.path.join(rootAbsPath, 'dataset-annotations', 'dataset', '')

# Path to the Dataset Folders
pathToMaFi = os.path.join(rootAbsPath, 'dataset-matfiles', 'dataset', '')

# Path to the Dataset Folders
pathToPtnt = os.path.join(rootAbsPath, 'dataset-patients-metadata', 'dataset', '')

# Path to the Dataset Folders
pathToPart = os.path.join(rootAbsPath, 'dataset-partial-annotations', 'dataset', '')

# Path to the Dataset Folders
pathToMaPa = os.path.join(rootAbsPath, 'dataset-mamo-patients', 'dataset', '')

# Path to the Dataset Folders
pathToDIma = os.path.join(rootAbsPath, 'dataset-dicom-images', 'dataset', '')

# ============================== #
# ============================== #

# ============================== #
#       FILE & Folder NAMES      #
# ============================== #

pth001 = '/src/'
pth002 = '/instances/'
pth003 = 'downloads/'

# Chance URL for your own viewer
lnk002 = 'http://breastscreening.isr.tecnico.ulisboa.pt:8982' + pth001
lnk003 = lnk002 + 'studyList.json'
lnk004 = lnk002 + 'studies/'
# Chance URL for your own DICOM server
lnk005 = 'http://breastscreening.isr.tecnico.ulisboa.pt:8450' + pth002

# ============================== #
# ============================== #

# ==================== END File ==================== #
