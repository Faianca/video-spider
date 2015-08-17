__author__ = 'jmeireles'

import bs4
import requests
import dryscrape


class Requester:

    def __init__(self):
        pass

    def send(self, url):
        return requests.get(url)

    def get(self, url, pageLoad = False):
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
