# Medical Image Downloader

<img src="https://github.com/mida-project/meta/blob/master/banners/dataset-samples_1000x250.png?raw=true" />

[![MIT](https://flat.badgen.net/github/license/opprDev/medical-image-downloader)](https://github.com/opprDev/medical-image-downloader/blob/master/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/opprDev/medical-image-downloader?style=flat-square)](https://github.com/opprDev/medical-image-downloader/commits/master)
[![OpenCollective](https://opencollective.com/oppr/backers/badge.svg?style=flat-square)](#backers)
[![OpenCollective](https://opencollective.com/oppr/sponsors/badge.svg?style=flat-square)](#sponsors)
[![Gitter](https://img.shields.io/gitter/room/gitterHQ/gitter.svg?style=flat-square)](https://gitter.im/opprTeam)
[![Status](https://flat.badgen.net/github/status/opprDev/medical-image-downloader)](https://circleci.com/gh/opprDev/medical-image-downloader)
[![Twitter](https://flat.badgen.net/twitter/follow/opprGroup)](https://twitter.com/opprGroup)

The presented repository has the source code for the "[Medical Imaging Downloader for CornerstoneJS and Orthanc](https://medium.com/oppr/medical-imaging-downloader-for-cornerstonejs-and-orthanc-d08c3a508d9b)" medium story. It represents the set of scripts to download medical images from a [WADO](https://www.medicalconnections.co.uk/tags/WADO) server and [PACS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1718393/). For the purpose, we are using lightweight [JavaScript](https://www.javascript.com/) library for displaying medical images in a web browser, called [CornerstoneJS](https://cornerstonejs.org/). To store and retrieve the medical images, we are using the [Orthanc](https://www.orthanc-server.com/) server as a standalone [DICOM](https://www.dicomlibrary.com/) server. The scripts are reading from the [WADO](https://www.medicalconnections.co.uk/tags/WADO) server, linking the image paths to the [PACS](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1718393/) to retrieve the images from here and download it to a local folder. In other words, the code will know where are the images from the [`prototype-cornerstone`](https://github.com/MIMBCD-UI/prototype-cornerstone/) sample, retrieving the images stored at a [Orthanc](https://www.orthanc-server.com/) server.

## Table of contents

* [Prerequisites](#Prerequisites)
* [Usage](#Usage)
* [Roadmap](#Roadmap)
* [Contribution](#Contribution)
* [Acknowledgements](#Acknowledgements)
* [License](#License)

## Prerequisites

The following list is showing the required dependencies for this project to run locally:

* [Git](https://git-scm.com/) or any other Git or GitHub version control tool
* [Python](https://www.python.org/) (3.5 or newer)

Here are some tutorials and documentation, if needed, to feel more comfortable about using and playing around with this software:

* Python: [Tutorial](https://docs.python.org/3/tutorial/index.html)
* Git: [Tutorial](https://git-scm.com/docs/gittutorial)
* GitHub: [Quick Tutorial](https://guides.github.com/activities/hello-world/)

## Usage

### Installation

At this point, the only way to install this software is manual. Eventually, this will be accessible through [pip](https://pypi.org/project/pip/) or any other package manager, as mentioned on the [roadmap](#Roadmap).

Nonetheless, this kind of installation is as simple as cloning this repository. Virtually all Git and GitHub version control tools are capable of doing that. Through the console, we can use the command below, but other ways are also fine.

```bash
git clone https://github.com/opprDev/medical-image-downloader.git
```

Optionally, the mi module/directory can be installed into the designated Python interpreter by moving it into the site-packages directory at the respective Python directory.

### Demonstration

Please, feel free to try out our demo. It is a script called download_medical_images.py at the src/demo directory. It can be used as follows:

```bash
python download_medical_images.py ./medical_images
```

Just keep in mind this is just a demo, so it does nothing more than downloading medical images to an arbitrary destination directory if the directory does not exist or does not have any content. Also, we did our best to make the demo as user-friendly as possible, so, above everything else, have fun! 😁

## Roadmap

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3172/badge)](https://bestpractices.coreinfrastructure.org/projects/3172)

We need to follow the repository goal, by addressing the thereby information. Therefore, it is of chief importance to scale this solution supported by the repository. The repository solution follows the best practices, achieving the [Core Infrastructure Initiative (CII)](https://bestpractices.coreinfrastructure.org/en/projects/3172) specifications.

## Contribution

This project exists thanks to all the people who [contribute](CONTRIBUTING.md). We welcome everyone who wants to help us improve this downloader. Here are some suggestions:

### As an issuer

Either as something that seems missing or any need for support, just open a [new issue](https://github.com/opprDev/medical-image-downloader/issues/new). Regardless of being a simple request or a fully-structured feature, we will do our best to understand them and, eventually, solve them.

### As a developer

We like to develop, but we also like collaboration. You could ask us to add some feature... or you could want to do it yourself and fork this repository. Maybe even do some side-project of your own. If the latter ones, please let us share some insights about what we currently have.

We do [TDD](https://en.wikipedia.org/wiki/Test-driven_development). In short, we first identify which are the behaviors this downloader should have and encode it using [unittest](https://docs.python.org/3/library/unittest.html) and [unittest.mock](https://docs.python.org/3/library/unittest.mock.html), and then implement our code in the most recent stable version of Python and, possibly, refactor it. This is more than optional, of course, but you would have at your disposal our test suite to make you more comfortable about changing our code. You could even add more unit tests.

The textual illustration below shows the folder and file structure of our source code, along with their respective description.

```
medical-image-downloader/
  mi/
    download_all.py: File with the main method to download all DICOM files from the Orthanc server
    constant.py: File with constants
    util/
      api.py: File with API-related utility methods
      format.py: File with formatting utility methods
      url.py: File with URL-related utility methods
  test/mi/
    download_all_test.py: A test case of download_all.py
    mock/: Folder with mocks and their respective parameters, grouped by the module they are mocking
    sample/: Folder with all samples, in python, as an output of mocks
  demo/
    download_medical_images.py: Command/Script to execute download_all.py
```

We also follow CI/CD practices through [GitHub Actions](https://github.com/features/actions). Here are our workflows:

* push_commit.yml - When pushing a commit to GitHub, test the downloader and evaluate code quality;
* create_pull_request.yml - When creating a pull request, publish a package of the downloader into the testing environment of PyPI, to evaluate how the package will eventually be presented on the real PyPI;
* publish_release.yml - When publishing a release, publish a package of the downloader into PyPI.

Use them as you see fit. Just don't forget to credit us if you publish a fork of this downloader. :grin:

## Acknowledgements

### Author

* Francisco Maria Calisto [ [Website](http://www.franciscocalisto.me/) | [ResearchGate](https://www.researchgate.net/profile/Francisco_Maria_Calisto) | [GitHub](https://github.com/FMCalisto) | [Twitter](https://twitter.com/FMCalisto) | [LinkedIn](https://www.linkedin.com/in/fmcalisto/) ]

* Luís Ribeiro Gomes

### Contributors

* Bruno Oliveira
* Carlos Santiago
* Duarte Figueirôa
* Jacinto C. Nascimento
* Pedro Miraldo
* Nuno Nunes

### Special Thanks

A special thanks to [Chris Hafey](https://www.linkedin.com/in/chafey/), the propelling person of [CornerstoneJS](https://cornerstonejs.org/), who also developed the [cornerstoneDemo](https://github.com/chafey/cornerstoneDemo). Not forgetting the three supporters of the [CornerstoneJS](https://cornerstonejs.org/) library, [Aloïs Dreyfus](https://www.linkedin.com/in/alois-dreyfus), [Danny Brown](http://dannyrb.com/) and [Erik Ziegler](https://www.npmjs.com/~swederik). We also would like to give a special thanks to [Erik Ziegler](https://www.npmjs.com/~swederik) who support several [issues](https://groups.google.com/forum/#!forum/cornerstone-platform) during this path.

### Supporters

Thank you to all our backers and sponsors! 🙏

#### Backers

<a href="https://opencollective.com/oppr/contribute/backer-11217/checkout" target="_blank">
<img src="https://opencollective.com/oppr/backers.svg">
</a>

#### Sponsors

<a href="https://opencollective.com/oppr/contribute/sponsor-11218/checkout" target="_blank">
<img src="https://opencollective.com/oppr/sponsors.svg">
</a>

Our organization is a non-profit organization. However, we have many expenses across our activity. From infrastructure to service expenses, we need some money, as well as help, to support our team and projects.

<a href="https://opencollective.com/oppr" target="_blank">
<img src="https://opencollective.com/oppr/tiers/donate.svg" width="160">
</a>

<br/>

<a href="https://www.patreon.com/oppr" target="_blank">
<img src="https://c5.patreon.com/external/logo/become_a_patron_button.png" width="160">
</a>

## License

Copyright &copy; 2019 [oppr](https://oppr.io)

The [`medical-image-downloader`](https://github.com/opprDev/medical-image-downloader) repository is distributed under the terms of [MIT](LICENSE) license and the present information is covered by this. You are free to make changes and use this in either personal or commercial projects. Attribution is not required, but it is welcomed. A little "Thanks!" (or something to that effect) would be much appreciated.
