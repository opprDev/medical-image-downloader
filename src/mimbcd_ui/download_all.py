from mimbcd_ui.util.api import download_study_list, download_study, get_series_list, download_dicom_file


def download_all(source_dicom_server_url, destination_directory):
  for count, image_id in enumerate(list_all_image_id_from_mimbcd_ui()):
    download_dicom_file(source_dicom_server_url, destination_directory, count, image_id)


def list_all_image_id_from_mimbcd_ui():
  for study_without_series in download_study_list():
    study = download_study(study_without_series)
    for _ in range(len(study)):
      for series in get_series_list(study):
        for instance in series.instanceList:
          print('Addressing the Image ID', instance.imageId, 'of the Series number', series.seriesNumber)
          yield instance.imageId
