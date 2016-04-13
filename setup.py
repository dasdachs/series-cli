from setuptools import setup, find_packages


setup(
    name="series",
    version="0.1",
    author="dasDachs",
    license="MIT",
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
