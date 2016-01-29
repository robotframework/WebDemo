#!/usr/bin/env python

from __future__ import print_function

from glob import glob
from os import getcwd
from os.path import abspath, dirname, join
from time import localtime
from zipfile import ZipFile, ZIP_DEFLATED

assert getcwd() == dirname(abspath(__file__))

NAME = 'WebDemo'
ZIP_NAME = NAME + '-%d%02d%02d.zip' % localtime()[:3]
FILES = ['README.rst',
         'demoapp/server.py',
         'demoapp/html/*.html',
         'demoapp/html/*.css',
         'login_tests/*.robot']

with ZipFile(ZIP_NAME, 'w', ZIP_DEFLATED) as zipfile:
    for pattern in FILES:
        for path in glob(pattern):
            print('Adding:  ', path)

            zipfile.write(path, join(NAME, path))
print('Created: ', ZIP_NAME)
