#!/usr/bin/env python
'''
Setup for pynos
'''
from setuptools import setup, find_packages

setup(name='pynos',
      version='0.5',
      description='Brocade NOS Library.',
      author='Matthew Stone',
      author_email='mstone@brocade.com',
      url='https://www.github.com/bigmstone/pynos',
      packages=find_packages(),
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking'
        ]
     )
