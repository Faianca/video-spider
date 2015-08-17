__author__ = 'jmeireles'
import re
import urllib
from fetcher import AbstractFetcher


class Fetcher(AbstractFetcher):

    def fetch(self, url):
        soup = self.requester.get(url)
        test = re.search(r"(?<=url:\s)(['\"])(?P<url>https.+)\1", soup.text)

        if test is None:
            return

        return urllib.unquote(test.group("url")).decode('utf8')