#!/usr/bin/env python

from distutils.core import setup


setup(name='lyricscramble',
      version='1.0',
      description='Generates silly phrases from song lyrics.',
      author='Cal Belden',
      author_email='calvinbelden@gmail.com',
      packages=['lyricscramble',
                'lyricscramble.markovchain',
                'lyricscramble.lyricfetch'],
      install_requires=['requests==2.3.0',
                        'beautifulsoup4==4.3.2'])
