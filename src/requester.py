__author__ = 'jmeireles'

import bs4
import requests
import dryscrape
import urlparse
from urllib import urlencode, quote, unquote
from collections import OrderedDict


class Requester:
    def __init__(self):
        pass

    def send(self, url):
        return requests.get(url)

    def get(self, url, pageLoad=False):
        """
        Get with javascript loaded
        :param url:
        :param pageLoad:
        :return:
        """
        if pageLoad:
            session = dryscrape.Session()
            session.visit(url)
            response = session.body()
        else:
            response = requests.get(url).text

        return bs4.BeautifulSoup(response)


    @staticmethod
    def build_url(url, params):
        url_parts = list(urlparse.urlparse(url))

        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update(params)

        url_parts[4] = urlencode(query)
        url = urlparse.urlunparse(url_parts)

        return url
