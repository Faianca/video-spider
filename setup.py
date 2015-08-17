from videospider import __version__

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="VideoSpider",
    version=__version__,
    author="Jorge Faianca",
    author_email="jorgefaianca@gmail.com",
    description=("Fetch the video url from some famous providers"),
    license="MIT",
    keywords="video scrapper fetcher youtube novamov",
    url="https://github.com/Faianca/video-spider",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Internet",
        "Topic :: Multimedia :: Video"
    ]
)
