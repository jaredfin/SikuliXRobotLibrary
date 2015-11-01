Custom SikuliX Library For Robot Framework
==================================================

TLDR
-----------
Prerequisites: java 8, jython, robotframework, jybot, sikulixapi.jar with tesseract

Setup CLASSPATH AND JYTHONPATH in environment variables:

      CLASSPATH = <path to sikulixapi.jar>
      JYTHONPATH = <path to sikulixapi.jar>\Lib

Install the SikuliXRobotLibrary:

      git clone https://github.com/jaredfin/SikuliXRobotLibrary.git
      cd SikuliXRobotLibrary
      jython setup.py install

Run The Demo:

      jybot -d LOGS -i Demotest demo\calc_test_suite

Introduction
------------

SikuliXRobotLibrary is a gui recognition testing library for Robot Framework
that leverages the SikuliX version 1.1.0 methods.

It is modeled after the Selenium2Library library.

- More information about this library can be found in the `Keyword Documentation`_.
- Installation information is found in the `INSTALL.rst` file.


Directory Layout
----------------

demo/
    A simple demonstration, with calculator application in Windows 8

doc/
    Keyword documentation

src/
    Python source code


Usage
-----

To write tests with Robot Framework and SikuliXRobotLibrary, 
SikuliXRobotLibrary must be imported into your Robot test suite.
See `Robot Framework User Guide`_ for more information.

Preconditions
-------------

SikuliXRobotLibrary supports Jython interpreters supported by the
Robot Framework.

SikuliXRobotLibrary depends on a few other Jython libraries, including
of course Robot Framework. All dependencies are declared in setup.py.

SikuliX must be installed with the Tesseract based OCR features. When running the sikulixsetup-1.1.0.jar,
make sure to select the second and third options.


Installing from source
----------------------

The source code can be retrieved either as a source distribution or as a clone
of the main source repository. The installer requires Jython version 2.7 or
newer. Install by running:

    jython setup.py install

Note: In most linux systems, you need to have root privileges for installation.

Uninstallation is achieved by deleting the installation directory and its
contents from the file system. The default installation directory is
`[JythonLibraries]/site-packages/robotframework_SikuliXRobotLibrary-1.0.0-py2.7.egg`.


Verifying Installation
----------------------

Once you have installed SikuliXRobotLibrary it is a good idea to verify the installation. To verify installation start jython::

     C:\> jython

and then at the Python prompt type::

    >> import SikuliXRobotLibrary
    >>

If the python command line interpretor returns with another prompt ('>>' as shown above) then your installation was successful.

Troubleshooting Installation
----------------------------

The most common issue with installing SikuliXRobotLibrary is missing dependencies. An error like::

    ImportError: No module named sikuli

indicates that you are missing the sikulixapi.jar package.  To correct this problem, install the sikulixapi.jar with tesseract
then add the following in the environment variables::

      CLASSPATH = <path to sikulixapi.jar>
      JYTHONPATH = <path to sikulixapi.jar>\Lib

Similarly if you receive "No module named ..." error message then you have another missing dependency.  To correct, use easy_install to install the missing package.

.. _pip: http://www.pip-installer.org
.. _easy_install: http://pypi.python.org/pypi/setuptools

Running the Demo
----------------

The demo directory contains an easily executable demo for Robot Framework
using SikuliXRobotLibrary. To run the demo, run::

    jybot -d <output directory> -i <tag> <suite directory>

E.g.::

    jybot -d C:\SikuliXRobotLibrary\demo\logs -i CalculatorTest C:\SikuliXRobotLibrary\demo\calc_test_suite
    Note: C:\demo\logs directory must be created before running the script
	

.. _Keyword Documentation: https://pybot.wordpress.com/2015/10/31/sikulixrobotlibrary-keyword-documentation/
.. _Robot Framework User Guide: http://code.google.com/p/robotframework/wiki/UserGuide
