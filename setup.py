#!/usr/bin/env python

from distutils.core import setup


setup(name='lyricscrambler',
      version='1.0',
      description='Generates silly phrases from song lyrics.',
      author='Cal Belden',
      author_email='calvinbelden@gmail.com',
      packages=['lyricscramble'],
      install_requires=['markovchain==1.0',
                        'lyricfetch==1.0'],
      dependency_links=['https://github.com/cbelden/markovchain/tarball/master#egg=markovchain-1.0',
                        'https://github.com/cbelden/lyricfetch/tarball/master#egg=lyricfetcher-1.0'])
