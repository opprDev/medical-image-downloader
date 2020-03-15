from .constant import MIMBCD_UI_STUDY_LIST_URL, MIMBCD_UI_STUDIES_URL

import json
import urllib.request

HORIZONTAL_DOUBLE_LINE = "=============================="
ADDRESSING_IMAGE_ID = "Addressing the Image ID"
OF_THE_SERIES_NUMBER = "of the Series number"

TEXT_FILE_EXTENSION = '.txt'
DICOM_FILE_EXTENSION = '.dcm'
JSON_FILE_EXTENSION = '.json'

INSTANCES_DIRECTORY = '/instances/'


def download_all(source_dicom_server_url, destination_directory):
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
