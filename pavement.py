import os
import sys
from os.path import join, pardir, abspath, dirname, split

from paver.easy import *
from paver.setuputils import setup

from setuptools import find_packages

VERSION = (0, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

setup(
    name = 'esus',
    version = __versionstr__,
    description = 'Esus',
    long_description = '\n'.join((
        'Esus',
        '',
        'discussion software for Django',
    )),
    author = 'Lukas Linhart',
    author_email='bugs@almad.net',
    license = 'BSD',
    url='http://git.netcentrum.cz/projects/django/GIT/esus/',

    packages = find_packages(
        where = '.',
        exclude = ('docs', 'tests')
    ),

    include_package_data = True,

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires = [
        'setuptools>=0.6b1',
    ],
)

options(
    citools = Bunch(
        rootdir = abspath(dirname(__file__))
    ),
)

try:
    from citools.pavement import *
except ImportError:
    pass

@task
def install_dependencies():
    sh('pip install -r requirements.txt')

@task
def bootstrap():
    options.virtualenv = {'packages_to_install' : ['pip']}
    call_task('paver.virtual.bootstrap')
    sh("python bootstrap.py")
    path('bootstrap.py').remove()


    print '*'*80
    if sys.platform in ('win32', 'winnt'):
        print "* Before running other commands, You now *must* run %s" % os.path.join("bin", "activate.bat")
    else:
        print "* Before running other commands, You now *must* run source %s" % os.path.join("bin", "activate")
    print '*'*80

@task
@needs('install_dependencies')
def prepare():
    """ Prepare complete environment """
