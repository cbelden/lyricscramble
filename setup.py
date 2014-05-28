#!/usr/bin/env python

from distutils.core import setup


setup(name='lyricscrambler',
      version='1.0',
      description='Generates silly phrases from song lyrics.',
      author='Cal Belden',
      author_email='calvinbelden@gmail.com',
      packages=['lyricscramble'],
      require_installs=['markovchain',
                        'lyricfetch'],
      dependency_links=['git+git://github.com/cbelden/markovchain@master',
                        'git+git://github.com/cbelden/lyricfetch@master'])
