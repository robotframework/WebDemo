Instructions to create releases
===============================


Preconditions
-------------

Operating system and Python requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Generating releases has only been tested on Linux, but it ought to work the
same way also on OSX and other unixes. Creating releases is only supported
with Python 3.6 or newer.

The ``pip`` and ``invoke`` commands below are also expected to run on Python
3.6+. Alternatively, it's possible to use the ``python3.6 -m pip`` approach
to run these commands.

Python dependencies
~~~~~~~~~~~~~~~~~~~

Many steps are automated using the generic `Invoke <http://pyinvoke.org>`_
tool with a help by our `rellu <https://github.com/robotframework/rellu>`_
utilities, but also other tools and modules are needed. A pre-condition is
installing all these, and that's easiest done using `pip
<http://pip-installer.org>`_ and the provided `<requirements.txt>`_ file::

    pip install -r requirements.txt

Using Invoke
~~~~~~~~~~~~

Invoke tasks are defined in the `<tasks.py>`_ file and they are executed from
the command line like::

    inv[oke] task [options]

Creating release
----------------

1. Test that everything works::

     python demoapp/server.py
     robot login_tests

2. Move regenerated log and report to docs::

     inv move-docs

5. If README.rst has changed, generate project documentation based on it::

     inv project-docs
