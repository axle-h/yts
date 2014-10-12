__author__ = 'Alex'

from distutils.core import setup

setup(
    name='yts',
    version='0.1',
    packages=['axh', 'axh.yts'],
    url='axh.pwnz.org',
    license='',
    author='Alex Haslehurst',
    author_email='alex.haslehurst@gmail.com',
    description='Parser for http://www.yify-torrent.org/.',
    requires=['humanfriendly', 'beautifulsoup4', 'html5lib'],
    install_requires=['humanfriendly', 'beautifulsoup4', 'html5lib']
)
