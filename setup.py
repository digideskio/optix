#name =!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='jinx',
    version='0.0.1',
    author='Doug Black',
    author_email='doug@dougblack.io',
    description='Stronger curses',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['clint'],
)
