__author__ = 'jmeireles'
import re, urllib
from fetcher import AbstractFetcher


class Fetcher(AbstractFetcher):

    def fetch(self, url):
        soup = self.requester.get(url)

        test = re.search(r"(?<=file:)([\"'])(?P<url>https?.+)\1", soup.text)
        print test
        if test is None:
            return

        return urllib.unquote(test.group("url")).decode('utf8')