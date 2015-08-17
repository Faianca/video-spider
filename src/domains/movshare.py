__author__ = 'jmeireles'
import re
import urllib
from fetcher import AbstractFetcher


class Fetcher(AbstractFetcher):

    def fetch(self, url):
        soup = self.requester.get(url, True)
        print soup.text
        movshareDomain = re.search('(?<=flashvars.domain=)"?(?P<match>[^";]+)', soup.text)
        movshareDomain = urllib.unquote(movshareDomain.group("match")).decode('utf8')

        movshareFile = re.search('(?<=flashvars.file=)"?(?P<match>[^";]+)', soup.text)
        movshareFile = urllib.unquote(movshareFile.group("match")).decode('utf8')

        movshareKey = re.search('(?<=flashvars.filekey=)"?(?P<match>[^";]+)', soup.text)
        movshareKey = urllib.unquote(movshareKey.group("match")).decode('utf8')

        movshareCID = re.search('(?<=flashvars.cid=)"?(?P<match>[^";]+)', soup.text)
        movshareCID = urllib.unquote(movshareCID.group("match")).decode('utf8')

        return self.requester.send("dsa")

