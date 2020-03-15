from itertools import chain, repeat

from test.mimbcd_ui.sample import studiesIndex_whenDownloaded, studiesIndex_whenDownloaded_withEmptyStudyList, \
    study_whenDownloaded, study_whenDownloaded_withEmptySeriesList


def sideEffect():
    return chain(
        [studiesIndex_whenDownloaded],
        repeat(study_whenDownloaded)
    )

def sideEffect_withEmptyStudyList():
    return chain(
        [studiesIndex_whenDownloaded_withEmptyStudyList]
    )

def sideEffect_withEmptySeriesList():
    return chain(
        [studiesIndex_whenDownloaded],
        repeat(study_whenDownloaded_withEmptySeriesList)
    )