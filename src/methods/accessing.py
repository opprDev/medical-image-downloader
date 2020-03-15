#!/usr/bin/env python
# coding=utf-8

"""
DownloadAllTestCase.py: To access both servers, i.e., CornerstoneDemo and Orthanc,
              we need to provide feature for that. Or even methods for that.
              The purpose of this file is to aggregate all methods for the
              purpose and provide feature levels for developers.
"""

import json
import urllib.request

from base import *
from messages import *
from paths import *

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


def download_all(source_dicom_server_url, destination_directory):
  """
  Downloading all medical images from your main server
  that are stored on a DICOM server.
  """
  dicom_file_counter = 10000000
  study_list_fp = urllib.request.urlopen(MIMBCD_UI_STUDY_LIST_URL).read()
  study_list = json.loads(study_list_fp)
  for patient_position in range(len(study_list['studyList'])):
    print(HORIZONTAL_DOUBLE_LINE)
    patient_id = study_list['studyList'][patient_position]['patientId']
    study_url = MIMBCD_UI_STUDIES_URL + patient_id + JSON_FILE_EXTENSION
    study_fp = urllib.request.urlopen(study_url).read()
    study = json.loads(study_fp)
    print(study)
    for _ in range(len(study)):
      series_list = study['seriesList']
      for series_position in range(len(series_list)):
        series_number = series_list[series_position]['seriesNumber']
        instance_list = series_list[series_position]['instanceList']
        for image_position in range(len(instance_list)):
          dicom_file_counter = dicom_file_counter + 1
          image_id = instance_list[image_position]['imageId']
          print(ADDRESSING_IMAGE_ID, image_id, OF_THE_SERIES_NUMBER, series_number)
          dicom_file_url = source_dicom_server_url + INSTANCES_DIRECTORY + image_id
          destination_path = destination_directory + str(dicom_file_counter) + DICOM_FILE_EXTENSION
          urllib.request.urlretrieve(dicom_file_url, destination_path)
    print(HORIZONTAL_DOUBLE_LINE)
