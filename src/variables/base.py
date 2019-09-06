#!/usr/bin/env python
#coding=utf-8

"""
base.py: All basic variables are presented here.
"""

__author__      = "Francisco Maria Calisto"
__maintainer__  = "Francisco Maria Calisto"
__email__       = "francisco.calisto@tecnico.ulisboa.pt"
__license__     = "MIT"
__version__     = "1.2.2"
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

import logging

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

# This MESSAGES will not reach the Humans.
log.debug('MODE: debug')
log.info('MODE: info')
log.warn('MODE: warn')
log.error('MODE: error')
log.critical('MODE: critical')

## Citizens of Earth, your planet will be removed NOW!

tot001 = 'total'

birads_1 = 1
birads_2 = 2
birads_3 = 3
birads_4 = 4
birads_5 = 5

ext001 = '.txt'
ext002 = '.dcm'
ext003 = '.json'

# ==================== END File ==================== #
