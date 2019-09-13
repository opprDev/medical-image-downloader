# Medical Image Downloader

<img src="https://github.com/mida-project/meta/blob/master/banners/dataset-samples_1000x250.png?raw=true" />

[![MIT](https://flat.badgen.net/badge/license/MIT/blue)](https://github.com/opprDev/medical-image-downloader/blob/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/python?style=flat-square)](https://pypi.org/)
![Last commit](https://img.shields.io/github/last-commit/opprDev/medical-image-downloader?style=flat-square)
[![HitCount](http://hits.dwyl.io/opprDev/medical-image-downloader.svg)](http://hits.dwyl.io/opprDev/medical-image-downloader)
[![OpenCollective](https://opencollective.com/oppr/backers/badge.svg?style=flat-square)](#backers)
[![OpenCollective](https://opencollective.com/oppr/sponsors/badge.svg?style=flat-square)](#sponsors)
[![Gitter](https://img.shields.io/gitter/room/gitterHQ/gitter.svg?style=flat-square)](https://gitter.im/opprTeam)
[![Status](https://flat.badgen.net/github/status/opprDev/medical-image-downloader)]()

The presented repository has the source code for the "[Medical Imaging Downloader for CornerstoneJS and Orthanc](https://medium.com/oppr/medical-imaging-downloader-for-cornerstonejs-and-orthanc-d08c3a508d9b)" medium story. It represents the set of scripts to download medical images from a [WADO](https://www.medicalconnections.co.uk/tags/WADO) server and [PACS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1718393/). For the purpose, we are using lightweight [JavaScript](https://www.javascript.com/) library for displaying medical images in a web browser, called [CornerstoneJS](https://cornerstonejs.org/). To store and retrieve the medical images, we are using the [Orthanc](https://www.orthanc-server.com/) server as a standalone [DICOM](https://www.dicomlibrary.com/) server. The scripts are reading from the [WADO](https://www.medicalconnections.co.uk/tags/WADO) server, linking the image paths to the [PACS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1718393/) to retrieve the images from here and download it to a local folder. In other words, the code will know where are the images from the [`prototype-cornerstone`](https://github.com/MIMBCD-UI/prototype-cornerstone/) sample, retrieving the images stored at a [Orthanc](https://www.orthanc-server.com/) server.

<a href="https://www.patreon.com/oppr" target="_blank">
<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

## Pre-Requisites

The following list is showing the set of dependencies for this project. Please, install and build in your machine the recommended versions.

List of dependencies for this project:

- [Git](https://git-scm.com/) (>= [2.20](https://raw.githubusercontent.com/git/git/master/Documentation/RelNotes/2.20.1.txt))

- [Python](https://www.python.org/) (>= [3.5](https://docs.python.org/3/))

## Instructions

The instructions are as follows. We assume that you already have knowledge over [Git](https://git-scm.com/) and [GitHub](https://github.com/). If not, please follow this [support](https://guides.github.com/activities/hello-world/) information. Any need for support, just open a [New issue](https://github.com/opprDev/medical-image-downloader/issues/new).

### Clone

To clone the hereby repository follow the guidelines. It is easy as that.

1.1. Please clone the repository by typing the command:

```
git clone https://github.com/opprDev/medical-image-downloader.git
```

1.2. Get inside of the repository directory:

```
cd medical-image-downloader/
```

1.3. For the installation and running of the source code, follow the next steps;

### Install

The installation guidelines are as follows. Please, be sure that you follow it correctly.

2.1. Run the following command to install the [library](https://pip.pypa.io/en/stable/user_guide/) set using [pip](https://pypi.org/project/pip/):

```
pip install -r requirements.txt
```

2.2. Follow the next step;

### Run

The running guidelines are as follows. Please, be sure that you follow it correctly.

3.1. Run the sample using the following command:

```
python3 src/core/main.py
```

3.2. Enjoy our source code!

### Notebooks

You can also run a Notebook to watch some of our `models` chart plots. For this goal we are using the well known [Jupyter Notebook](http://jupyter.org/) web application. To run the [Jupyter Notebook](http://jupyter.org/) just follow the steps.

4.1. Get inside our project directory:

```
cd src/notebooks/
```

4.2. Run [Jupyter Notebook](http://jupyter.org/) application by typing:

```
jupyter notebook
```

> If you have any question regarding the [Jupyter Notebook](http://jupyter.org/) just follow their [Documentation](http://jupyter.org/documentation). You can also ask for help close to the [Community](http://jupyter.org/community).

## Information

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3172/badge)](https://bestpractices.coreinfrastructure.org/projects/3172)

We need to follow the repository goal, by addressing the thereby information. Therefore, it is of chief importance to scale this solution supported by the repository. The repository solution follow the best practices, achieving the [Core Infrastructure Initiative (CII)](https://bestpractices.coreinfrastructure.org/en/projects/3172) specifications.

### License

Copyright © 2019 [oppr](https://oppr.io)

The [`medical-image-downloader`](https://github.com/opprDev/medical-image-downloader) repository is distributed under the terms of [MIT](LICENSE) license and the present information is covered by this. You are free to make changes and use this in either personal or commercial projects. Attribution is not required, but it is welcomed. A little "Thanks!" (or something to that affect) would be much appreciated.

### Acknowledgements

A special thanks to [Chris Hafey](https://www.linkedin.com/in/chafey/), the propelling person of [CornerstoneJS](https://cornerstonejs.org/), who also developed the [cornerstoneDemo](https://github.com/chafey/cornerstoneDemo). Not forgetting the three supporters of the [CornerstoneJS](https://cornerstonejs.org/) library, [Aloïs Dreyfus](https://www.linkedin.com/in/alois-dreyfus), [Danny Brown](http://dannyrb.com/) and [Erik Ziegler](https://www.npmjs.com/~swederik). We also would like to give a special thanks to [Erik Ziegler](https://www.npmjs.com/~swederik) who support several [issues](https://groups.google.com/forum/#!forum/cornerstone-platform) during this path.

### Authors

- [Francisco Maria Calisto](http://www.franciscocalisto.me/) [[ResearchGate](https://www.researchgate.net/profile/Francisco_Maria_Calisto) | [GitHub](https://github.com/FMCalisto) | [Twitter](https://twitter.com/FMCalisto) | [LinkedIn](https://www.linkedin.com/in/fmcalisto/)]

## Sponsors

<a href="https://opencollective.com/oppr" target="_blank">
<img src="https://opencollective.com/oppr/tiers/backer.svg" width="220">
</a>
