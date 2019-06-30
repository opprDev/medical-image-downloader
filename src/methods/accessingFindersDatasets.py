#!/usr/bin/env python
#coding=utf-8

"""
.py:
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.0.2"
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
import csv
import time
import json, urllib.request

import pandas as pd

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
from baseFindersDatasets import *
from messagesFindersDatasets import *
from pathsFindersDatasets import *

time_stamp = str(int(time.time()))

def dwnldMainServImgStorOnDicomServ(folderToSave, mainServer, dicomServer):
  '''
  Downloading all medical images from your main server
  that are stored on a DICOM server.
  '''
  image_counter = 10000000
  dataStudyList = urllib.request.urlopen(mainServer).read()
  outputStudyList = json.loads(dataStudyList)
  for ptnt in range(len(outputStudyList['studyList'])):
    print(c010)
    patientIdToCompare = outputStudyList['studyList'][ptnt]['patientId']
    pntFileOnServer = lnk004 + patientIdToCompare + ext003
    dataStudies = urllib.request.urlopen(pntFileOnServer).read()
    outputStudies = json.loads(dataStudies)
    print(outputStudies)
    for study in range(len(outputStudies)):
      #patientId = outputStudies[study]['patientId']
      #internalId = outputStudies[study]['internalId']
      #stydyId = outputStudies[study]['studyId']
      seriesList = outputStudies['seriesList']
      #print(msg001, patientId)
      #print(msg002, internalId)
      #print(msg003, stydyId)
      for serie in range(len(seriesList)):
        seriesNumber = seriesList[serie]['seriesNumber']
        instanceList = seriesList[serie]['instanceList']
        for instance in range(len(instanceList)):
          image_counter = image_counter + 1
          imageId = instanceList[instance]['imageId']
          print(msg004, imageId, msg005, seriesNumber)
          dcmUrl = dicomServer + imageId
          dcmFileName = folderToSave + str(image_counter) + ext002
          urllib.request.urlretrieve(dcmUrl, dcmFileName)
    print(c010)

# ==================== END File ==================== #