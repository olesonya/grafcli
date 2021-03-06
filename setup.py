#!/usr/bin/env python3
import os
from subprocess import check_output
from setuptools import setup, find_packages

# Version management by:
# http://blogs.nopcode.org/brainstorm/2013/05/20/pragmatic-python-versioning-via-setuptools-and-git-tags/

version_py = os.path.join(os.path.dirname(__file__), 'grafcli', 'version.py')

try:
    version_git = check_output(["git", "describe", "--tags"]).rstrip().decode()
except:
    with open(version_py, 'r') as fh:
        version_git = open(version_py).read().strip().split('=')[-1].replace('"','')

version_msg = "# Do not edit this file, pipeline versioning is governed by git tags"
with open(version_py, 'w') as fh:
    fh.write(version_msg + os.linesep + "__version__=" + version_git)


setup(name='grafcli',
      version=version_git,
      description='Grafana CLI management tool',
      author='Milosz Smolka',
      author_email='m110@m110.pl',
      url='https://github.com/m110/grafcli',
      packages=find_packages(exclude=['tests']),
      scripts=['scripts/grafcli'],
      data_files=[('/etc/grafcli', ['grafcli.conf.example'])],
      install_requires=['climb>=0.3.2', 'pygments', 'requests'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3.4',
          'Topic :: System :: Systems Administration',
      ])
