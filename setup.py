# Entry point für das pyEleven package.
from setuptools import setup

setup(
    name = 'pyEleven',
    version = 'v0.1.0',
    packages = ['pyEleven'],
    entry_points = {
        'console_scripts': [
            'pyEleven = pyEleven.__main__:main'
        ]
    })