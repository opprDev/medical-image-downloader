FROM python:3.8 as builder
RUN pip install gitpython setuptools wheel twine
RUN pip install --no-cache-dir -r requirements.txt
RUN python setup.py sdist bdist_wheel
RUN pip install dist/*.tar.gz
RUN pip uninstall gitpython setuptools wheel twine

FROM python:3.8
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
CMD ["python3", "-c", "import mi, os; mi.download_all(os.environ['MI_ORTHANC_URL'] if 'MI_ORTHANC_URL' in os.environ else mi.constant.MI_ORTHANC_URL, '/out')"]