import distutils.core
import setup
import py2exe

import sys; sys.argv.append('py2exe')


py2exe_options = dict(
    excludes=['_ssl',  # Exclude _ssl
              'pyreadline',
              'difflib',
              'doctest',
              'locale',
              'optparse',
              'pickle',
              'calendar'
    ],
    dll_excludes=['msvcr71.dll'],
    compressed=True,
)

setup (
    name='Series-cli',
    version='0.1',
    description="""
        A simple CLI programm written in Python that uses the
        TvMaze API (http://www.tvmaze.com/api).
                """,
    author='dasDachs',
    licence='GNU',
    console=['series-cli.py'],
    options={'py2exe': py2exe_options},
)
