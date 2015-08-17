__author__ = 'jmeireles'
import re
from fetcher import AbstractFetcher
from urllib import unquote


class Fetcher(AbstractFetcher):
    rootApi = "/api/player.api.php"

    keys = {
        "domain": "undefined",
        "file": "undefined",
        "filekey": "undefined",
        "cid": "undefined",
    }

    def fetch(self, url):
        soup = self.requester.get(url)

        for key in self.keys:
            tmp = re.search('(?<=flashvars.'+key+'=)"?(?P<match>[^";]+)', soup.text)
            if tmp:
                self.keys[key] = unquote(tmp.group("match")).decode('utf8')

        if self.keys['filekey'] == 'fkz':
            tmp = re.search('fkz="?(?P<match>[^";]+)', soup.text)
            if tmp:
                self.keys['filekey'] = unquote(tmp.group("match")).decode('utf8')

        params = {'cid': self.keys['cid'], 'file': self.keys['file'], 'key': self.keys['filekey']}
        url = self.requester.build_url(self.keys['domain'] + self.rootApi, params)

        '''
            Api request
        '''
        response = self.requester.get(url, True)

        found = re.search('[domain|url]=(?P<url>.*?)&', response.text)

        if found:
            found = unquote(found.group("url")).decode('utf8')

        return found


