from itertools import chain, repeat

import sample


def sideEffect():
    return chain(
        [sample.studiesIndex_whenDownloaded],
        repeat(sample.study_whenDownloaded)
    )

def sideEffect_withEmptyStudyList():
    return chain(
        [sample.studiesIndex_whenDownloaded_withEmptyStudyList]
    )

def sideEffect_withEmptySeriesList():
    return chain(
        [sample.studiesIndex_whenDownloaded],
        repeat(sample.study_whenDownloaded_withEmptySeriesList)
    )