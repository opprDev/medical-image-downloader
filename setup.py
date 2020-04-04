from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf8') as f:
   long_description = f.read()

setup(
   name='MIMBCD-UI',
   use_scm_version={
      'local_scheme': 'no-local-version',
      'version_scheme': lambda version: version.format_with('{tag}')
   },
   setup_requires=['setuptools_scm'],
   description='A medical image downloader',
   long_description=long_description,
   long_description_content_type='text/markdown',
   license='MIT',
   url='https://opprdev.github.io/medical-image-downloader',
   project_urls={
       'Funding': 'https://opencollective.com/oppr',
       'Source': 'https://github.com/opprDev/medical-image-downloader',
       'Tracker': 'https://github.com/opprDev/medical-image-downloader/issues',
   },
   author='',
   author_email='',
   maintainer='',
   maintainer_email='',
   classifiers=[
      'Topic :: Scientific/Engineering :: Medical Science Apps.',
      'Development Status :: 4 - Beta',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Operating System :: MacOS :: MacOS X',
      'Operating System :: POSIX',
      'Operating System :: POSIX :: BSD',
      'Operating System :: POSIX :: Linux',
      'Operating System :: Microsoft :: Windows',
      'Environment :: Console',
      'Intended Audience :: Developers',
      'Intended Audience :: Science/Research',
      'Natural Language :: English'
   ],
   package_dir={'': 'src'},
   packages=find_packages(where='src', include=['mimbcd_ui', 'mimbcd_ui.*']),
   python_requires='~=3.5'
)
