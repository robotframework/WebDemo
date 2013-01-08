# Introduction

[Robot Framework] (http://robotframework.org) is a generic test automation
framework and
[SeleniumLibrary] (http://code.google.com/p/robotframework-seleniumlibrary)
is one of the many
[test libraries] (http://code.google.com/p/robotframework/wiki/TestLibraries)
that can be used with it. In addition to showing how the `SeleniumLibrary`
works, this demo introduces the basic Robot Framework test data syntax, how
tests are executed, and how logs and reports look like.

# Preconditions

To be able to execute the demo, both
[Robot Framework] (http://code.google.com/p/robotframework/wiki/Installation)
and
[SeleniumLibrary] (http://code.google.com/p/robotframework-seleniumlibrary/wiki/InstallationInstructions)
need to be installed. Notice that in addition to [Python] (http://python.org)
required by Robot Framework, you need to have [Java] (http://java.com) 1.5
or newer to run Selenium Server.

If you do not have time or interest to install everything, you can still
take a look at the test cases and generated logs and reports online.


# Downloading and executing the demo

The demo is available on the
[download page] (http://code.google.com/p/robotframework-seleniumlibrary/downloads/list). Latest version is XXX. It requires Robot Framework 2.6.

After downloading and unzipping the package, you should have all the
files in a directory `robotframework-seleniumlibrary-demo`. The
`rundemo.py` script is used for executing tests,
`demoapp` directory contains two versions of the [#Systems_under_test system under test],
and actual test cases are in the `login_tests`
directory.

To run the test cases execute the following command in the extracted directory:

```
    python rundemo.py login_tests
```

This should work in most environments if you have Firefox installed. See chapter executing tests for more information about running the tests with different browsers.


# Systems under test

The system under test in the demo is a very simple application
that only has login functionality. There are two versions of this application,
one implemented as HTML pages and the other an Adobe Flex application. Both of these should run without special preconditions, but see [FlexTesting these instructions] if you want to test your own Flex application.

The different versions of the application are shown in the below screenshots. The correct user name and password combination to both applications is `demo/mode` and using them will show you a welcome page. Otherwise an error page or dialog is shown.

(http://wiki.robotframework-seleniumlibrary.googlecode.com/hg/demoapp_html.png)

(http://wiki.robotframework-seleniumlibrary.googlecode.com/hg/demoapp_flex.png)


The demo applications are normally started and stopped automatically by
the `rundemo.py` script when tests are executed. The same script can
also be used to start and stop the applications so that those can be
investigated manually:

```
    python rundemo.py demoapp start
    python rundemo.py demoapp stop
```

After starting the demo application, the HTML version can be accessed from URL http://localhost:7272/html

The application source codes are located in the `demoapp/html` directory inside the extracted zip file.


# Selenium Server

Running tests using the `SeleniumLibrary` requires
[http://seleniumhq.org/projects/remote-control/ Selenium Server]
to be running. A version of the server is bundled with the library, and starting and stopping it is handled by the `rundemo.py` script automatically when it is used
for executing tests. It is possible to also start/stop the server separately:

```
    python rundemo.py selenium start
    python rundemo.py selenium stop
```


= Test cases =

The test cases distributed with the demo are in the `login_tests`
directory and visible also  [http://robotframework-seleniumlibrary.googlecode.com/hg/demo/login_tests online]. They are in plain text format (Robot Framework support also HTML and TSV formats), and can be edited using any text editor. There exists also a special Robot Framework test data editor [http://code.google.com/p/robotframework-ride RIDE].

The simplest test case file is
[http://robotframework-seleniumlibrary.googlecode.com/hg/demo/login_tests/valid_login.txt valid_login.txt],
which contains only one test case `Valid Login`. This test case has a
simple workflow, created using keywords, that starts from opening the browser
and ends with verifying that the welcome page has been opened.

The other test case file,
[http://robotframework-seleniumlibrary.googlecode.com/hg/demo/login_tests/invalid_login.txt invalid_login.txt],
has several test cases that verify different invalid login scenarios
such as invalid or empty user name. These tests are data-driven in their
nature and each of them only has one keyword that encapsulates
the needed workflow.

Both of these test case files use domain specific high-level
keywords, such as `Open Browser To Login Page`. These keywords use lower level keywords internally, such as `Title Should Be` and `Open Browser`. In this demo the higher level keywords are created in technology specific resource files
[http://robotframework-seleniumlibrary.googlecode.com/hg/demo/login_tests/html_resource.txt html_resource.txt] and [http://robotframework-seleniumlibrary.googlecode.com/hg/demo/login_tests/flex_resource.txt flex_resource.txt]. In addition, there is a common resource file [http://robotframework-seleniumlibrary.googlecode.com/hg/demo/login_tests/common_resource.txt common_resource.txt], which defines some variables, for example to determine which version of the application to test against.
The lowest level keywords always come from test libraries, in this case from the `SeleniumLibrary` that provides
generic keywords for web testing.


# Executing test cases

## Using `rundemo.py`

The easiest way to run the test cases is using the already mentioned
`rundemo.py` script, which automatically starts and stops both the
[#System_under_test system under test] and the
[#Selenium_Server Selenium Server].
Tests are executed by giving a path to tests to run as an argument to
`rundemo.py`. It is possible to run either a single test case file by giving
a path to that file, or all test case files in a directory by
giving a path to the directory:

```
    python rundemo.py login_tests/valid_login.txt
    python rundemo.py login_tests
```

When tests are executed, `rundemo.py` passes arguments it gets
directly to the `pybot` command that is normally used for running
Robot Framework test cases. The `pybot` command supports various
command line options (run `pybot --help` for a full list), and when
they are needed they must be given before the test data path as
in these examples:

```
    python rundemo.py --name New_name login_tests/
    python rundemo.py --outputdir results --loglevel DEBUG login_tests/
```

## Using different browsers

By default tests are executed using the Firefox browser. The browser to use
is defined as a `${BROWSER}` variable in the
[http://robotframework-seleniumlibrary.googlecode.com/hg/demo/login_tests/common_resource.txt common_resource.txt]
file, and it can be easily overridden from the command line:

```
    python rundemo.py --variable BROWSER:IE login_tests/
    python rundemo.py --variable BROWSER:GoogleChrome login_tests/
```

What browsers are supported and how to use them is explained in the
[http://code.google.com/p/robotframework-seleniumlibrary/wiki/LibraryDocumentation documentation]
of the `Open Browser` keyword.

== Selecting application to test ==

By default, the test cases are run against the HTML version of the test application. This can be changed by overriding `${SUT}` variable from the command line:

```
    python rundemo.py --variable SUT:flex login_tests/
```

== Slowing down executing speed ==

Typically the tests run so fast (except for opening the browser) that
it is impossible to see what is happening. The execution speed can be slowed
down by overriding the `${DELAY}` variable:

```
    python rundemo.py --variable DELAY:0.5 login_tests/
```

## Running tests using `pybot`

It is possible to run the tests also using the normal `pybot` start-up
script, but that requires that the [#System_under_test demo application]
and the [#Selenium_Server Selenium Server] are started before. This might
be a good idea if starting the demo application and Selenium Server takes
a lot of time and you want to run tests multiple times.

This example shows a possible workflow:

```
    python rundemo.py selenium start
    python rundemo.py demoapp start
    pybot --variable BROWSER:Firefox --outputdir firefox login_tests
    pybot --variable BROWSER:IE --outputdir ie login_tests
    python rundemo.py demoapp stop
    python rundemo.py selenium stop
```


# Viewing logs and reports

After tests have been executed, Robot Framework creates a detailed log
file listing all the executed keywords with their possible log
messages. Another important output is the test report that has a
higher level summary of the test execution. By default these files are
created into the directory where tests are executed from, and exact
locations are shown on the console after the execution.

Example outputs generated when these tests are run are available online:

  * [log file] (http://robotframework-seleniumlibrary.googlecode.com/hg/demo/log.html)
  * [report] (http://robotframework-seleniumlibrary.googlecode.com/hg/demo/report.html)


# Where to find more information

Robot Framework documentation is available on the project pages at
http://robotframework.org. If you are new to the framework you may want to
start from the
[introduction slides] (http://code.google.com/p/robotframework/wiki/IntroductionSlides) and then look at the
[Quick Start Guide] (http://code.google.com/p/robotframework/wiki/QuickStartGuide),
which also acts as another executable demo. All the Robot Framework features
are documented in the comprehensive
[User Guide] (http://code.google.com/p/robotframework/wiki/UserGuide).

More information about the `SeleniumLibrary` is available here in the library's
[wiki] (http://code.google.com/p/robotframework-seleniumlibrary/w/list).
Most importantly the library documentation documents all the available keywords.