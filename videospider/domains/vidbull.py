__author__ = 'jmeireles'
import re
from fetcher import AbstractFetcher
from ..requester import IOS_USER_AGENT


class Fetcher(AbstractFetcher):


    def fetch(self, url):
        headers = {'User-Agent': IOS_USER_AGENT}
        soup = self.requester.get(url, headers=headers)
        source = soup.select("video > source")

        if not source:
            return

        source = source[0].get('src')

        if re.match("^\/\/", source):
            source = "http:" + source

        return source