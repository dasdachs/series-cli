Series-cli
==========

A simple CLI programm written in Python that uses the
TvMaze API (http://www.tvmaze.com/api).

This project rests on the shoulders of two great libraries:
    Requests https://github.com/kennethreitz/requests
    Click    https://github.com/pallets/click

Quick install:
--------------

Obviously first get [Git](https://git-scm.com/). Follow this [tutorial](https://help.github.com/articles/set-up-git/). Of course you could just download this repository without the use of Git, but that would just be boring.

Since it is a Python project, make sure you have Python installed. Use Python 3.4 or later. It's an easy install, just
go to [Python.org](http://python.org)

### Install using setup.py

To use this app as a script (from anywhere in your command line or in a virtual environment) do the following:

1. Move to the directory where you want to work from and clone this repository
 `git clone https://github.com/dasdachs/series-cli.git`
2. CD into the directory `series-cli` with `cd series-cli`
3. Run `python setup.py install`
4. Run the app: `show` and type in the name of the show as is

### Virtual environment

If you do not wish to install globally, create a virtual environment and install the dependencies using `pip`.

1. Move to the directory where you want to work from and clone this repository
 `git clone https://github.com/dasdachs/series-cli.git`
2. Create a virtual environment `python -m venv virtualenv`
3. Install packages `pip install -r requirements.txt`
4. Run the app: `python series/base.py` (or move series/base.py to your root)

Misc:
-----

I am working on a API wrapper fot TVMaze, so improvements for Python users are coming.

If you have any wishes, suggestions or anything else, contact me: <jani.sumak@gmail.com>
