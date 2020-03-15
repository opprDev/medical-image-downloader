#!/usr/bin/env python
# coding=utf-8

"""
main.py: When creating a Python module, it is common to make
         the module execute some functionality (usually contained
         in a main function) when run as the entry point of
         the program.
"""

from mimbcd_ui import download_all
from paths import MIMBCD_UI_ORTHANC_URL

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


def main():
  download_all(source_dicom_server_url=MIMBCD_UI_ORTHANC_URL, destination_directory='downloads/')


if __name__ == '__main__':
  main()
