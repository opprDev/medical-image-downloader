from mimbcd_ui.constant import MIMBCD_UI_STUDY_LIST_URL
from mimbcd_ui.util.format import format_study_url, format_dicom_file_url, format_destination_path
from mimbcd_ui.util.url import download_json, download_file


def download_study_list():
  study_list = download_json(MIMBCD_UI_STUDY_LIST_URL)
  return study_list.studyList


def download_series_list(study_without_series):
  print('==============================')
  patient_id = study_without_series.patientId
  study_url = format_study_url(patient_id)
  study = download_json(study_url)
  print(study)
  return study.seriesList


def download_dicom_file(source_dicom_server_url, destination_directory, count, image_id):
  dicom_file_url = format_dicom_file_url(source_dicom_server_url, image_id)
  destination_path = format_destination_path(destination_directory, str(10000001 + count))
  download_file(destination_path, dicom_file_url)
