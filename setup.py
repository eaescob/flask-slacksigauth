from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setup(name='flask_slacksigauth',
      version=find_version('flask_slacksigauth', 'version.py'),
      description='Python Flask adapter for verifying Slack signatures',
      long_description=long_description,
      long_description_content_type='text/x-rst',
      url='https://github.com/eaescob/flask-slacksigauth',
      author='Emilio Escobar',
      author_email='eescobar@gmail.com',
      license='GNU',
      packages=['flask_slacksigauth'],
      install_requires=[
        'flask',
        'pyee',
        'requests',
        'six',
      ],
      zip_safe=False)
