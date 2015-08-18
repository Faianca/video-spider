__author__ = 'jmeireles'
import re, urllib
from fetcher import AbstractFetcher


class Fetcher(AbstractFetcher):

    def fetch(self, url):
        soup = self.requester.get(url)
        source = soup.select("#video > source")

        if not source:
            return

        source = source[0].get('src')

        if re.match("^\/\/", source):
            source = "http:" + source

        return source