import urllib.request
from mimbcd_ui.util.format import format_json


def download_json(source_url):
  response = urllib.request.urlopen(source_url).read()
  return format_json(response)


def download_file(destination_path, source_url):
  urllib.request.urlretrieve(source_url, destination_path)
