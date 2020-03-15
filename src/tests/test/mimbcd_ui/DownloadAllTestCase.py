#!/usr/bin/env python
# coding=utf-8

"""
DownloadAllTestCase.py: Testing comparisons for our set of methods and files.
"""

from unittest import TestCase
from unittest.mock import call, patch

import test.mimbcd_ui.mock.json.loads
import test.mimbcd_ui.mock.urllib.request.urlopen
from mimbcd_ui import download_all
from paths import MIMBCD_UI_STUDY_LIST_URL, MIMBCD_UI_ORTHANC_URL

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


@patch('urllib.request.urlopen', return_value=test.mimbcd_ui.mock.urllib.request.urlopen.returnValue)
@patch('urllib.request.urlretrieve')
class DownloadAllTestCase(TestCase):
  @patch('json.loads', side_effect=test.mimbcd_ui.mock.json.loads.sideEffect())
  def test_whenDownloadMedicalImages_thenInvokeUrlopenFourTimes(self, mock_loads, mock_urlretrieve, mock_urlopen):
    self.urlopen_called_four_times(mock_urlopen)

  @patch('json.loads', side_effect=test.mimbcd_ui.mock.json.loads.sideEffect())
  def test_whenDownloadMedicalImages_thenInvokeUrlretrieveSeveralTimes(self, mock_loads, mock_urlretrieve, mock_urlopen):
    download_all(
      source_dicom_server_url=MIMBCD_UI_ORTHANC_URL,
      destination_directory='downloads/'
    )
    mock_urlretrieve.assert_has_calls([
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000001.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000002.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000003.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000004.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000005.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000006.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000007.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000008.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000009.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000010.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000011.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000012.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000013.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000014.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000015.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000016.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000017.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000018.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000019.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000020.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000021.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000022.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000023.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000024.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000025.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000026.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000027.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000028.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000029.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000030.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000031.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000032.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000033.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000034.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000035.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000036.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000037.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000038.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000039.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000040.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000041.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000042.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000043.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000044.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000045.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000046.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000047.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000048.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000049.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000050.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000051.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000052.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000053.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000054.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000055.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000056.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000057.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000058.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000059.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000060.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000061.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000062.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000063.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000064.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000065.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000066.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000067.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000068.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000069.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000070.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000071.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000072.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000073.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000074.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000075.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000076.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000077.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000078.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000079.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000080.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000081.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000082.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000083.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000084.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000085.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000086.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000087.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000088.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000089.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000090.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000091.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000092.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000093.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000094.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000095.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000096.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000097.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000098.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000099.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000100.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000101.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000102.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000103.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000104.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000105.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000106.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000107.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000108.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000109.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000110.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000111.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000112.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000113.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000114.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000115.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000116.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000117.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000118.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000119.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000120.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000121.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000122.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000123.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000124.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000125.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000126.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000127.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000128.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000129.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000130.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000131.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000132.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000133.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000134.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000135.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000136.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000137.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000138.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000139.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000140.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000141.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000142.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000143.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000144.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000145.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000146.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000147.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000148.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000149.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000150.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000151.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000152.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000153.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000154.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000155.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000156.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/dd03786b-6cc667d1-a65fa0e9-34101126-6f82ca59/file', 'downloads/10000157.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/ae407aac-af2c66a3-5801a6c9-ffff4ae9-06496953/file', 'downloads/10000158.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/062ce5a8-0d015abb-73f65ae3-f95d55e8-9cbdfcb6/file', 'downloads/10000159.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/6f6f0dc7-db7a6fa0-f3e46a80-8bcda478-194bcf11/file', 'downloads/10000160.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/e0551a96-ccf93766-a2d57ddf-361c8462-46b8b196/file', 'downloads/10000161.dcm'),
      call('http://breastscreening.isr.tecnico.ulisboa.pt:8450/instances/88653231-d6fba822-1af594af-e6f5b30d-dd1ab7f2/file', 'downloads/10000162.dcm')
    ])

  @patch('json.loads', side_effect=test.mimbcd_ui.mock.json.loads.sideEffect_withEmptyStudyList())
  def test_whenDownloadMedicalImages_withEmptyStudyList_thenInvokeUrlopenOnce(self, mock_loads, mock_urlretrieve, mock_urlopen):
    download_all(
      source_dicom_server_url=MIMBCD_UI_ORTHANC_URL,
      destination_directory='downloads/'
    )
    mock_urlopen.assert_called_once_with(MIMBCD_UI_STUDY_LIST_URL)

  @patch('json.loads', side_effect=test.mimbcd_ui.mock.json.loads.sideEffect_withEmptyStudyList())
  def test_whenDownloadMedicalImages_withEmptyStudyList_thenDoNotInvokeUrlretrieve(self, mock_loads, mock_urlretrieve, mock_urlopen):
    self.urlretrieve_not_called(mock_urlretrieve)

  @patch('json.loads', side_effect=test.mimbcd_ui.mock.json.loads.sideEffect_withEmptySeriesList())
  def test_whenDownloadMedicalImages_withEmptySeriesList_thenInvokeUrlopenOnce(self, mock_loads, mock_urlretrieve, mock_urlopen):
    self.urlopen_called_four_times(mock_urlopen)

  @patch('json.loads', side_effect=test.mimbcd_ui.mock.json.loads.sideEffect_withEmptySeriesList())
  def test_whenDownloadMedicalImages_withEmptySeriesList_thenDoNotInvokeUrlretrieve(self, mock_loads, mock_urlretrieve, mock_urlopen):
    self.urlretrieve_not_called(mock_urlretrieve)

  def urlopen_called_four_times(self, mock_urlopen):
    download_all(
      source_dicom_server_url=MIMBCD_UI_ORTHANC_URL,
      destination_directory='downloads/'
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
      destination_directory='downloads/'
    )
    mock_urlretrieve.assert_not_called()
