from setuptools import setup, find_packages


setup(
    name="series",
    version="0.1",
    author="dasDachs",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    include_package_data=True,
    setup_requires=["pytest-runner",],
    install_requires=[
        "Click",
        "Requests",
        "Colorama",
        "pytest",
    ],
    entry_points = {
        'console_scripts': [
            'show = series.base:main',
        ],
    },
)
