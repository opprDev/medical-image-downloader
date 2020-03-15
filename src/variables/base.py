#!/usr/bin/env python
# coding=utf-8

"""
base.py: All basic variables are presented here.
"""

import logging

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
  "Nuno Nunes",
  "Duarte Figueirôa"
]

logging.basicConfig(format='%(message)s')
log = logging.getLogger()

# Set a severity threshold to one above:
# CRITICAL, ERROR, WARNING, INFO, DEBUG
#
# see:
#
# https://docs.python.org/3/library/logging.html
levelNameToSet = 'CRITICAL'
level = logging.getLevelName(levelNameToSet)
log.setLevel(level)

log.debug('MODE: debug')
log.info('MODE: info')
log.warning('MODE: warning')
log.error('MODE: error')
log.critical('MODE: critical')

TEXT_FILE_EXTENSION = '.txt'
DICOM_FILE_EXTENSION = '.dcm'
JSON_FILE_EXTENSION = '.json'
