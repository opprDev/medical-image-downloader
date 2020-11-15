import os
import sys
from mi import download_all
from mi.constant import MI_ORTHANC_URL

assert len(sys.argv) == 2, """Invalid command usage.
Correct usage: download_medical_images <destination-directory>
Example: download_medical_images ./medical_images
"""
destination_directory = sys.argv[1]

assert not os.path.exists(destination_directory) or os.path.isdir(destination_directory), destination_directory + """ is not a directory.
Correct usage: download_medical_images <destination-directory>
Example: download_medical_images ./medical_images
"""

assert not os.path.exists(destination_directory) or len(os.listdir(destination_directory)) == 0, """Directory not empty.
We wouldn't like to affect any directory that has already content.
Please, keep in mind this is just a demo. Have fun! :)
"""
os.makedirs(destination_directory, exist_ok=True)

download_all(
  source_dicom_server_url=MI_ORTHANC_URL,
  destination_directory=destination_directory
)
