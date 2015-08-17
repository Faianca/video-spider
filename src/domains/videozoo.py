__author__ = 'jmeireles'
import re, urllib
from fetcher import AbstractFetcher
import jsbeautifier.unpackers.packer as packer

class Fetcher(AbstractFetcher):


    def fetch(self, url):
        soup = self.requester.get(url)

        test = re.search(r"eval(?:.+fullscreen.+\))", soup.text)

        if test is None:
             return

        unpack = packer.unpack(test.group())

        test = re.search("http:\/\/[^\s\"]+.\.(?:mp4|mpg|avi|flv)", unpack)

        if test is None:
             return

        info = self.requester.send(test.group())

        info = re.search(r"(['\"])(?P<url>https:.+)\1", info.text)

        if info is None:
             return

        return info.group("url")