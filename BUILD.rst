Instructions to create releases
===============================

1. Test that everything works::

     robot login_tests

2. Regenerate log and report if needed using the command documented in wiki.
   Same command as above.

3. Move regenerated log and report to
   https://bitbucket.org/robotframework/robotframework.bitbucket.org/src/master/WebDemo/
   to make them visible online.

4. Generate a new download package::

     ./package.py

5. Upload the download package to https://bitbucket.org/robotframework/webdemo/downloads
