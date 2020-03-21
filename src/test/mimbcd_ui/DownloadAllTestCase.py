from unittest import TestCase
from mimbcd_ui import download_all
from unittest.mock import call, patch
from mimbcd_ui.constant import MIMBCD_UI_ORTHANC_URL, MIMBCD_UI_STUDY_LIST_URL

import test.mimbcd_ui.mock.urllib.request.urlopen


@patch('urllib.request.urlretrieve')
class DownloadAllTestCase(TestCase):
  @patch('urllib.request.urlopen', side_effect=test.mimbcd_ui.mock.urllib.request.urlopen.sideEffect())
  def test_whenDownloadMedicalImages_thenInvokeUrlopenFourTimes(self, mock_urlopen, mock_urlretrieve):
    self.urlopen_called_four_times(mock_urlopen)

  @patch('urllib.request.urlopen', side_effect=test.mimbcd_ui.mock.urllib.request.urlopen.sideEffect())
  def test_whenDownloadMedicalImages_thenInvokeUrlretrieveSeveralTimes(self, mock_urlopen, mock_urlretrieve):
    download_all(
      source_dicom_server_url=MIMBCD_UI_ORTHANC_URL,
      destination_directory='medical_images'
    )
    mock_urlretrieve.assert_has_calls([
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'medical_images/10000001.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'medical_images/10000002.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'medical_images/10000003.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'medical_images/10000004.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'medical_images/10000005.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'medical_images/10000006.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'medical_images/10000007.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'medical_images/10000008.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'medical_images/10000009.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'medical_images/10000010.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'medical_images/10000011.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'medical_images/10000012.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'medical_images/10000013.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'medical_images/10000014.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'medical_images/10000015.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'medical_images/10000016.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'medical_images/10000017.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'medical_images/10000018.dcm'),
    ])

  @patch('urllib.request.urlopen', side_effect=test.mimbcd_ui.mock.urllib.request.urlopen.sideEffect_withEmptyStudyList())
  def test_whenDownloadMedicalImages_withEmptyStudyList_thenInvokeUrlopenOnce(self, mock_urlopen, mock_urlretrieve):
    download_all(
      source_dicom_server_url=MIMBCD_UI_ORTHANC_URL,
      destination_directory='medical_images'
    )
    mock_urlopen.assert_called_once_with(MIMBCD_UI_STUDY_LIST_URL)

  @patch('urllib.request.urlopen', side_effect=test.mimbcd_ui.mock.urllib.request.urlopen.sideEffect_withEmptyStudyList())
  def test_whenDownloadMedicalImages_withEmptyStudyList_thenDoNotInvokeUrlretrieve(self, mock_urlopen, mock_urlretrieve):
    self.urlretrieve_not_called(mock_urlretrieve)

  @patch('urllib.request.urlopen', side_effect=test.mimbcd_ui.mock.urllib.request.urlopen.sideEffect_withEmptySeriesList())
  def test_whenDownloadMedicalImages_withEmptySeriesList_thenInvokeUrlopenOnce(self, mock_urlopen, mock_urlretrieve):
    self.urlopen_called_four_times(mock_urlopen)

  @patch('urllib.request.urlopen', side_effect=test.mimbcd_ui.mock.urllib.request.urlopen.sideEffect_withEmptySeriesList())
  def test_whenDownloadMedicalImages_withEmptySeriesList_thenDoNotInvokeUrlretrieve(self, mock_urlopen, mock_urlretrieve):
    self.urlretrieve_not_called(mock_urlretrieve)

  def urlopen_called_four_times(self, mock_urlopen):
    download_all(
      source_dicom_server_url=MIMBCD_UI_ORTHANC_URL,
      destination_directory='medical_images'
    )
    mock_urlopen.assert_has_calls([
      call(MIMBCD_UI_STUDY_LIST_URL),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8982/src/studies/7.json'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8982/src/studies/0.json'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8982/src/studies/Case1.json')
    ])

  def urlretrieve_not_called(self, mock_urlretrieve):
    download_all(
      source_dicom_server_url=MIMBCD_UI_ORTHANC_URL,
      destination_directory='medical_images'
    )
    mock_urlretrieve.assert_not_called()
