#!/usr/bin/env python

import os, shutil
from zipfile import ZipFile, ZIP_DEFLATED

VERSION = "1.0"
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
#execfile(os.path.join(THIS_DIR, '..', 'src', 'Selenium2Library', 'version.py'))

FILES = {
    '': ['rundemo.py', 'README.txt'],
    'testcases': ['valid_login.txt', 'invalid_login.txt','content_check.txt','resource.txt'],
    'demoapp': ['server.py'],
    'demoapp/html': ['index.html', 'welcome.html', 'error.html', 'demo.css', 'file_information.txt', 'file_names.txt', 'file_places.txt']
}

def main():
    cwd = os.getcwd()
    try:
        os.chdir(THIS_DIR)
        name = 'robotframework-selenium2library-%s-demo' % VERSION
        zipname = '%s.zip' % name
        if os.path.exists(zipname):
            os.remove(zipname)
        zipfile = ZipFile(zipname, 'w', ZIP_DEFLATED)
        for dirname in FILES:
            for filename in FILES[dirname]:
                path = os.path.join('.', dirname.replace('/', os.sep), filename)
                print 'Adding:  ', os.path.normpath(path)
                zipfile.write(path, os.path.join(name, path))
        zipfile.close()
        target_path = os.path.join('.', 'dist')
        if os.path.exists(target_path):
            shutil.rmtree(target_path, ignore_errors=True)
        os.makedirs(target_path)
        os.rename(zipname, os.path.join(target_path, zipname))
        print 'Created: ', os.path.abspath(target_path)
    finally:
        os.chdir(cwd)


if __name__ == '__main__':
    main()
