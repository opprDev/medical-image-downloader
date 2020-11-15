from unittest.mock import Mock
from itertools import chain, repeat
from test.mi.sample import studiesIndex_whenDownloaded, studiesIndex_whenDownloaded_withEmptyStudyList, \
    study_whenDownloaded, study_whenDownloaded_withEmptySeriesList

returnValue_whenDownloadStudiesIndex = Mock()
returnValue_whenDownloadStudiesIndex.read = Mock(return_value=studiesIndex_whenDownloaded)

returnValue_whenDownloadStudiesIndex_withEmptyStudyList = Mock()
returnValue_whenDownloadStudiesIndex_withEmptyStudyList.read = Mock(return_value=studiesIndex_whenDownloaded_withEmptyStudyList)

returnValue_whenDownloadStudy = Mock()
returnValue_whenDownloadStudy.read = Mock(return_value=study_whenDownloaded)

returnValue_whenDownloadStudy_withEmptySeriesList = Mock()
returnValue_whenDownloadStudy_withEmptySeriesList.read = Mock(return_value=study_whenDownloaded_withEmptySeriesList)

def sideEffect():
    return chain(
        [returnValue_whenDownloadStudiesIndex],
        repeat(returnValue_whenDownloadStudy)
    )

def sideEffect_withEmptyStudyList():
    return chain(
        [returnValue_whenDownloadStudiesIndex_withEmptyStudyList]
    )

def sideEffect_withEmptySeriesList():
    return chain(
        [returnValue_whenDownloadStudiesIndex],
        repeat(returnValue_whenDownloadStudy_withEmptySeriesList)
    )
