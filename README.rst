
Web testing with Robot Framework and SeleniumLibrary
====================================================

Robot Framework
---------------

Robot Framework is a generic open source test automation framework.

SeleniumLibrary
---------------

SeleniumLibrary is one of the many test libraries that can be used with Robot Framework.

Demo Package
============

To get the demo, you can either download the repository from [GitHub](https://github.com/robotframework/WebDemo/archive/master.zip) or checkout the source code directly from [GitHub](https://github.com/robotframework/WebDemo.git). As a result, you get the ``WebDemo`` directory with ``demoapp`` and ``login_tests`` subdirectories.

Online Example
--------------

Example test cases and generated results are also available online. There is thus no need to download the demo if you are not interested in running it yourself.

Demo Application
================

The demo application is a very simple login page. With user name ``demo`` and password ``mode``, you get into a welcome page, and otherwise, you end up on an error page.

Starting Demo Application
-------------------------

Running tests requires the demo application located under the ``demoapp`` directory to be running. It can be started either by double-clicking the ``demoapp/server.py`` file in a file manager or by executing it from the command line:

```
python demoapp/server.py
```

After the demo application is started, it is available at URL [http://localhost:7272](http://localhost:7272). You can test it manually; valid credentials are ``demo/mode``, and it needs to be running while executing the automated tests.

Running Tests
-------------

The test cases are located in the ``login_tests`` directory. They can be executed using the ``robot`` command:

```
robot login_tests
```

You can also run an individual test case file and use various command line options supported by Robot Framework.

Using Different Browsers
------------------------

The browser that is used is controlled by the ``${BROWSER}`` variable defined in the ``resource.robot`` resource file. Firefox browser is used by default, but that can be easily overridden from the command line.

For more details about the test data syntax and test execution, see the [Robot Framework User Guide](http://robotframework.org/robotframework/#user-guide).

Installation
------------

To install the required dependencies and WebDriverManager globally, follow these steps:

1. Install Python if not already installed.
2. Install Pipenv using pip:

   ```
   pip install pipenv
   ```

3. Navigate to the project directory containing the Pipfile, and run:

   ```
   pipenv install
   ```

   This will create a virtual environment and install all the required dependencies specified in the Pipfile.

4. Install WebDriverManager globally using pip:

   ```
   pip install webdrivermanager
   ```

5. After installing WebDriverManager, you can use it to manage browser drivers. For example, to install Firefox and Chrome drivers and link them to the /usr/local/bin directory on Unix-like systems:

   ```
   webdrivermanager firefox chrome --linkpath /usr/local/bin
   ```

   Note: Ensure that /usr/local/bin is added to your PATH environment variable.

   On Windows, the process is slightly different. You can add the installation directory to your PATH using the following steps:

   - Right-click on My Computer or This PC, select Properties.
   - Select Advanced system settings.
   - Click on the Environment Variables button.
   - Under System Variables, select PATH and click Edit.
   - Click New and paste the installation directory.
   - Click OK several times and restart your computer.

Links
-----

- Robot Framework: http://robotframework.org
- SeleniumLibrary: https://github.com/robotframework/SeleniumLibrary
- Python: http://python.org
- Pip: http://pip-installer.org
