#!/usr/bin/env python
# coding=utf-8

from baseFindersDatasets import *
from messagesFindersDatasets import *
from pathsFindersDatasets import *
import os
import sys
import time
import json, urllib.request

"""
.py:
"""

__author__ = "Francisco Maria Calisto"
__maintainer__ = "Francisco Maria Calisto"
__email__ = "francisco.calisto@tecnico.ulisboa.pt"
__license__ = "MIT"
__version__ = "1.0.2"
__status__ = "Development"
__copyright__ = "Copyright 2019, Instituto Superior Técnico (IST)"
__credits__ = [
    "Bruno Oliveira",
    "Carlos Santiago",
    "Jacinto C. Nascimento",
    "Pedro Miraldo",
    "Nuno Nunes"
]

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

time_stamp = str(int(time.time()))


def getMedicalImages(folderToSave, mainServer, dicomServer):
    '''
    Downloading all medical images from your main server
    that are stored on a DICOM server.
    '''
    image_counter = 10000000
    dataStudyList = urllib.request.urlopen(mainServer).read()
    outputStudyList = json.loads(dataStudyList)

    patient_file_on_server = outputStudyList['studyList'].map(lambda patient: lnk004 + patient['patientId'] + ext102)
    output_studies = patient_file_on_server.map(lambda f: json.loads(urllib.request.urlopen(f).read()))
    series_list = output_studies.map(lambda output_study: convertToSeriesAndPrintFields(output_study))

    for series in series_list:
        series_number = series['seriesNumber']
        instance_list = series['instanceList']
        for instance in instance_list:
            process_instance(dicomServer, folderToSave, image_counter, instance, series_number)
        print(c010)


def process_instance(dicomServer, folderToSave, image_counter, instance, seriesNumber):
    image_counter += 1
    imageId = instance['imageId']
    print(msg004, imageId, msg005, seriesNumber)
    dcmUrl = dicomServer + imageId
    dcmFileName = folderToSave + fn015 + image_counter + ext103
    urllib.request.urlretrieve(dcmUrl, dcmFileName)


def convertToSeriesAndPrintFields(study):
    seriesList = study['seriesList']
    print(msg001, study['patientId'])
    print(msg002, study['internalId'])
    print(msg003, study['studyId'])
    return seriesList
