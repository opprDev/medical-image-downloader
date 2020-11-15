from collections import namedtuple
from json import loads
from mi.constant import MI_STUDIES_URL

DICOM_FILE_EXTENSION = '.dcm'
INSTANCES_DIRECTORY = '/instances/'
JSON_FILE_EXTENSION = '.json'


def format_json(response):
  return loads(response, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))


def format_study_url(patient_id):
  return MI_STUDIES_URL + patient_id + JSON_FILE_EXTENSION


def format_dicom_file_url(source_dicom_server_url, image_id):
  return source_dicom_server_url + INSTANCES_DIRECTORY + image_id


def format_destination_path(destination_directory, dicom_file_name):
  return destination_directory + "/" + dicom_file_name + DICOM_FILE_EXTENSION
